#!/usr/bin/env python3
"""
REW Automation Script
Automates EQ setup tasks in Room EQ Wizard via the API.

Features:
- Level-matches all speakers to Front Left (FL) reference
- Iteratively adjusts target levels until 500Hz-2kHz average matches FL
"""

import base64
import math
import struct
import time

import requests

BASE_URL = "http://127.0.0.1:4735"


def enable_blocking():
    """Enable blocking mode so API calls wait for completion."""
    response = requests.post(f"{BASE_URL}/application/blocking", json=True)
    response.raise_for_status()
    print("Blocking mode enabled")


def get_measurements():
    """Get list of all measurements as a dict keyed by index."""
    response = requests.get(f"{BASE_URL}/measurements")
    response.raise_for_status()
    return response.json()


def find_measurement_by_name(name: str):
    """Find a measurement by name and return its UUID."""
    measurements = get_measurements()
    # API returns dict with index keys, not a list
    for idx, m in measurements.items():
        if m.get("title") == name:
            return m.get("uuid")
    return None


def select_measurement(uuid: str):
    """Select a measurement by UUID."""
    response = requests.post(f"{BASE_URL}/measurements/selected-uuid", json=uuid)
    response.raise_for_status()
    print(f"Selected measurement: {uuid}")


def set_house_curve(file_path: str):
    """Set the house curve file path."""
    response = requests.post(f"{BASE_URL}/eq/house-curve", json=file_path)
    response.raise_for_status()
    print(f"House curve set to: {file_path}")


def set_match_target_settings(uuid: str, settings: dict):
    """Set the match target settings for a measurement."""
    response = requests.put(
        f"{BASE_URL}/measurements/{uuid}/target-settings", json=settings
    )
    response.raise_for_status()
    print("Match target settings updated")


def match_response_to_target(uuid: str):
    """Match the measurement response to the target curve."""
    command = {"command": "Match target"}
    response = requests.post(f"{BASE_URL}/measurements/{uuid}/eq/command", json=command)
    response.raise_for_status()
    print("Matched response to target")


def generate_predicted_measurement(uuid: str):
    """Generate predicted measurement from EQ filters."""
    command = {"command": "Generate predicted measurement"}
    response = requests.post(f"{BASE_URL}/measurements/{uuid}/eq/command", json=command)
    response.raise_for_status()
    print("Generated predicted measurement")


def get_eq_match_target_settings():
    """Get the default EQ match target settings."""
    response = requests.get(f"{BASE_URL}/eq/match-target-settings")
    response.raise_for_status()
    return response.json()


def set_eq_match_target_settings(settings: dict):
    """Set the default EQ match target settings."""
    response = requests.put(f"{BASE_URL}/eq/match-target-settings", json=settings)
    response.raise_for_status()
    print("EQ match target settings updated")


def decode_frequency_response(base64_string: str) -> list[float]:
    """Decode Base64-encoded frequency response data to float array.

    REW API returns 32-bit floats in big-endian byte order.
    """
    raw_bytes = base64.b64decode(base64_string)
    num_floats = len(raw_bytes) // 4
    # >f = big-endian float
    return list(struct.unpack(f">{num_floats}f", raw_bytes))


def get_frequency_response(
    uuid: str, ppo: int = 96, smoothing: str | None = None
) -> dict:
    """Get frequency response data for a measurement.

    Args:
        uuid: Measurement UUID
        ppo: Points per octave (default 96)
        smoothing: Smoothing type (e.g., "Var", "1/3", "1/6"). Default None uses measurement's current smoothing.

    Returns:
        Dict with 'magnitudes' (list of dB values), 'start_freq', and 'ppo'
    """
    url = f"{BASE_URL}/measurements/{uuid}/frequency-response?ppo={ppo}"
    if smoothing:
        url += f"&smoothing={smoothing}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    magnitudes = decode_frequency_response(data["magnitude"])

    return {
        "magnitudes": magnitudes,
        "start_freq": data["startFreq"],
        "ppo": data["ppo"],
    }


def calculate_average_db(
    magnitudes: list[float],
    start_freq: float,
    ppo: int,
    low_hz: float = 500,
    high_hz: float = 2000,
) -> float:
    """Calculate average dB level between two frequencies.

    Args:
        magnitudes: List of dB magnitude values
        start_freq: Starting frequency in Hz
        ppo: Points per octave
        low_hz: Lower frequency bound (default 500 Hz)
        high_hz: Upper frequency bound (default 2000 Hz)

    Returns:
        Average dB level in the specified frequency range
    """
    values_in_range = []

    for i, mag in enumerate(magnitudes):
        # Calculate frequency at this index: freq = start_freq * 2^(i/ppo)
        freq = start_freq * (2 ** (i / ppo))

        if low_hz <= freq <= high_hz:
            values_in_range.append(mag)
        elif freq > high_hz:
            break  # No need to continue past upper bound

    if not values_in_range:
        raise ValueError(f"No data points found between {low_hz}Hz and {high_hz}Hz")

    # RMS averaging (matches REW's averaging method)
    sum_sq = sum(10 ** (mag / 10) for mag in values_in_range)
    return 10 * math.log10(sum_sq / len(values_in_range))


def get_target_level(uuid: str) -> float:
    """Get the target level for a measurement."""
    response = requests.get(f"{BASE_URL}/measurements/{uuid}/target-level")
    response.raise_for_status()
    return response.json()


def set_target_level(uuid: str, level: float):
    """Set the target level for a measurement."""
    response = requests.post(f"{BASE_URL}/measurements/{uuid}/target-level", json=level)
    response.raise_for_status()
    print(f"Target level set to: {level:.1f} dB")


def find_predicted_measurement(original_name: str) -> str | None:
    """Find the predicted measurement UUID for an original measurement.

    REW names predicted measurements as "EQ {original_name}".

    Args:
        original_name: The original measurement name (e.g., "FLfinal")

    Returns:
        UUID of the predicted measurement, or None if not found
    """
    predicted_name = f"EQ {original_name}"
    return find_measurement_by_name(predicted_name)


def delete_measurement(uuid: str):
    """Delete a measurement by UUID."""
    response = requests.delete(f"{BASE_URL}/measurements/{uuid}")
    response.raise_for_status()
    print(f"Deleted measurement: {uuid}")


def process_speaker(
    measurement_name: str, target_curve_path: str, custom_settings: dict = None
):
    """Process a single speaker: select, set house curve, match target, generate predicted.

    Args:
        measurement_name: Name of the measurement in REW
        target_curve_path: Path to the target curve file
        custom_settings: Optional dict of settings to override defaults (e.g., frequency range)
    """
    print(f"\n{'=' * 60}")
    print(f"Processing: {measurement_name}")
    print(f"Target curve: {target_curve_path}")
    if custom_settings:
        print(f"Custom settings: {custom_settings}")
    print("=" * 60)

    # Apply custom settings if provided
    if custom_settings:
        print("\n--- Applying custom settings ---")
        current = get_eq_match_target_settings()
        updated = {**current, **custom_settings}
        set_eq_match_target_settings(updated)

    # Find and select the measurement
    uuid = find_measurement_by_name(measurement_name)
    if not uuid:
        print(f"ERROR: Could not find measurement named '{measurement_name}'")
        return False

    select_measurement(uuid)
    print(f"Selected '{measurement_name}' (UUID: {uuid})")

    # Set the House Curve
    print("\n--- Setting House Curve ---")
    set_house_curve(target_curve_path)

    # Match response to target
    print("\n--- Matching response to target ---")
    match_response_to_target(uuid)

    # Generate predicted measurement
    print("\n--- Generating predicted measurement ---")
    generate_predicted_measurement(uuid)

    print(f"\nCompleted: {measurement_name}")
    return True


def match_speaker_level_to_reference(
    uuid: str,
    measurement_name: str,
    target_curve_path: str,
    reference_avg_db: float,
    reference_target_level: float,
    custom_settings: dict = None,
    tolerance: float = 0.1,
    max_iterations: int = 20,
) -> dict:
    """Process a speaker and iteratively adjust target level to match reference.

    Uses a two-phase approach:
    1. Initial estimate: Generate predicted measurement at reference target level,
       calculate offset from reference, and jump directly to estimated target level
    2. Fine-tuning: Iterate in 0.1 dB steps to find the optimal match

    Args:
        uuid: Measurement UUID
        measurement_name: Name of the measurement in REW
        target_curve_path: Path to the target curve file
        reference_avg_db: Reference average dB (500Hz-2kHz) from FL speaker
        reference_target_level: FL's original target level to start from
        custom_settings: Optional dict of settings to override defaults
        tolerance: Acceptable difference in dB (default 0.1)
        max_iterations: Maximum fine-tuning iterations (default 20)

    Returns:
        Dict with 'success', 'final_avg_db', 'final_target_level', 'iterations'
    """
    print(f"\n{'=' * 60}")
    print(f"Level-matching: {measurement_name}")
    print(f"Target curve: {target_curve_path}")
    print(f"Reference avg dB: {reference_avg_db:.2f}")
    print(f"Reference target level: {reference_target_level:.1f}")
    if custom_settings:
        print(f"Custom settings: {custom_settings}")
    print("=" * 60)

    # Apply custom settings if provided
    if custom_settings:
        print("\n--- Applying custom settings ---")
        current = get_eq_match_target_settings()
        updated = {**current, **custom_settings}
        set_eq_match_target_settings(updated)

    # Select the measurement
    select_measurement(uuid)

    # Set the House Curve
    print("\n--- Setting House Curve ---")
    set_house_curve(target_curve_path)

    # =========================================================================
    # PHASE 1: Initial estimate - calculate offset and jump to estimated level
    # =========================================================================
    print("\n--- Phase 1: Initial estimate ---")
    print(f"Starting at reference target level: {reference_target_level:.1f} dB")
    set_target_level(uuid, reference_target_level)

    # Delete previous predicted measurement if it exists
    existing_predicted_uuid = find_predicted_measurement(measurement_name)
    if existing_predicted_uuid:
        print("Removing previous predicted measurement...")
        delete_measurement(existing_predicted_uuid)

    # Generate initial predicted measurement
    print("Matching response to target...")
    match_response_to_target(uuid)
    print("Generating predicted measurement...")
    generate_predicted_measurement(uuid)

    # Find and analyze the predicted measurement
    predicted_uuid = find_predicted_measurement(measurement_name)
    if not predicted_uuid:
        print(f"ERROR: Could not find predicted measurement 'EQ {measurement_name}'")
        return {
            "success": False,
            "final_avg_db": None,
            "final_target_level": reference_target_level,
            "iterations": 0,
        }

    # Get frequency response and calculate average
    freq_response = get_frequency_response(predicted_uuid, smoothing="Var")
    initial_avg_db = calculate_average_db(
        freq_response["magnitudes"],
        freq_response["start_freq"],
        freq_response["ppo"],
    )

    initial_offset = initial_avg_db - reference_avg_db
    print(f"Initial avg dB: {initial_avg_db:.2f}, Reference: {reference_avg_db:.2f}")
    print(f"Initial offset: {initial_offset:+.2f} dB")

    # Check if already within tolerance
    if abs(initial_offset) < tolerance:
        print(f"SUCCESS: Already within tolerance ({tolerance} dB)")
        return {
            "success": True,
            "final_avg_db": initial_avg_db,
            "final_target_level": reference_target_level,
            "iterations": 1,
        }

    # Calculate estimated target level: subtract offset to compensate
    # If speaker is 2dB louder than reference, lower target by 2dB
    estimated_target_level = reference_target_level - initial_offset
    # Round to nearest 0.1 dB for cleaner values
    estimated_target_level = round(estimated_target_level, 1)
    print(
        f"Estimated target level: {estimated_target_level:.1f} dB (offset: {-initial_offset:+.1f})"
    )

    # =========================================================================
    # PHASE 2: Fine-tuning - iterate in 0.1 dB steps
    # =========================================================================
    print("\n--- Phase 2: Fine-tuning ---")
    current_target_level = estimated_target_level
    set_target_level(uuid, current_target_level)

    # Track the best result seen during fine-tuning
    best_result = None
    best_diff = float("inf")

    iteration = 0
    while iteration < max_iterations:
        iteration += 1
        print(f"\n--- Fine-tune iteration {iteration}/{max_iterations} ---")

        # Delete previous predicted measurement
        existing_predicted_uuid = find_predicted_measurement(measurement_name)
        if existing_predicted_uuid:
            print("Removing previous predicted measurement...")
            delete_measurement(existing_predicted_uuid)

        # Match response to target
        print("Matching response to target...")
        match_response_to_target(uuid)

        # Generate predicted measurement
        print("Generating predicted measurement...")
        generate_predicted_measurement(uuid)

        # Find and analyze the predicted measurement
        predicted_uuid = find_predicted_measurement(measurement_name)
        if not predicted_uuid:
            print(
                f"ERROR: Could not find predicted measurement 'EQ {measurement_name}'"
            )
            return {
                "success": False,
                "final_avg_db": None,
                "final_target_level": current_target_level,
                "iterations": iteration + 1,  # +1 for initial estimate
            }

        # Get frequency response and calculate average
        freq_response = get_frequency_response(predicted_uuid, smoothing="Var")
        current_avg_db = calculate_average_db(
            freq_response["magnitudes"],
            freq_response["start_freq"],
            freq_response["ppo"],
        )

        difference = current_avg_db - reference_avg_db
        print(
            f"Current avg dB: {current_avg_db:.2f}, Reference: {reference_avg_db:.2f}, Diff: {difference:+.2f}"
        )

        # Track best result
        if abs(difference) < best_diff:
            best_diff = abs(difference)
            best_result = {
                "avg_db": current_avg_db,
                "target_level": current_target_level,
            }

        # Check if within tolerance
        if abs(difference) < tolerance:
            print(f"SUCCESS: Within tolerance ({tolerance} dB)")
            # Regenerate predicted measurement with final settings
            print("Regenerating final predicted measurement...")
            delete_measurement(predicted_uuid)
            match_response_to_target(uuid)
            generate_predicted_measurement(uuid)
            return {
                "success": True,
                "final_avg_db": current_avg_db,
                "final_target_level": current_target_level,
                "iterations": iteration + 1,  # +1 for initial estimate
            }

        # Adjust target level: if current is higher than reference, lower target level
        adjustment = -0.1 if difference > 0 else 0.1
        current_target_level = round(current_target_level + adjustment, 1)
        print(
            f"Adjusting target level by {adjustment:+.1f} dB to {current_target_level:.1f}"
        )
        set_target_level(uuid, current_target_level)

    # Max iterations reached - use best result if we found one
    print(f"WARNING: Max iterations ({max_iterations}) reached")
    if best_result:
        print(
            f"Using best result: {best_result['avg_db']:.2f} dB at target level {best_result['target_level']:.1f}"
        )
        # Restore best target level and regenerate
        if best_result["target_level"] != current_target_level:
            set_target_level(uuid, best_result["target_level"])
            existing_predicted_uuid = find_predicted_measurement(measurement_name)
            if existing_predicted_uuid:
                delete_measurement(existing_predicted_uuid)
            match_response_to_target(uuid)
            generate_predicted_measurement(uuid)
        return {
            "success": best_diff < tolerance,
            "final_avg_db": best_result["avg_db"],
            "final_target_level": best_result["target_level"],
            "iterations": iteration + 1,
        }

    return {
        "success": False,
        "final_avg_db": current_avg_db,
        "final_target_level": current_target_level,
        "iterations": iteration + 1,
    }


def main():
    print("=" * 60)
    print("REW Automation Script - Level-Matched EQ")
    print("=" * 60)

    # Speaker configurations: (measurement_name, target_curve_file, custom_settings)
    # custom_settings is optional - use None for default settings
    # IMPORTANT: FL must be first as it's the reference speaker
    base_path = "/Users/matthew/Python/mb-acoustix/magic-beans"

    # FDL and FDR (front height speakers) use limited frequency range: 20-1000 Hz
    height_speaker_settings = {"endFrequency": 1000}

    speakers = [
        ("FLfinal", f"{base_path}/Filters for Front Left.txt", None),
        ("FRfinal", f"{base_path}/Filters for Front Right.txt", None),
        (
            "FDLfinal",
            f"{base_path}/Filters for Front Height Left.txt",
            height_speaker_settings,
        ),
        (
            "FDRfinal",
            f"{base_path}/Filters for Front Height Right.txt",
            height_speaker_settings,
        ),
        ("SLAfinal", f"{base_path}/Filters for Surround Back Left.txt", None),
        ("SRAfinal", f"{base_path}/Filters for Surround Back Right.txt", None),
    ]

    # Enable blocking mode for synchronous operations
    enable_blocking()

    # List available measurements
    print("\n--- Available Measurements ---")
    measurements = get_measurements()
    print(f"Found {len(measurements)} measurements:")
    for idx, m in measurements.items():
        print(f"  - {m.get('title')} (UUID: {m.get('uuid')})")

    # Set the Filter Tasks (match target) settings once for all speakers
    print("\n--- Setting Filter Tasks settings ---")

    # First, get current settings to see the structure
    current_settings = get_eq_match_target_settings()
    print(f"Current match target settings: {current_settings}")

    # Configure the Filter Tasks settings:
    # - Match Range: 20 to 20,000 Hz
    # - Individual Max Boost: 6 dB
    # - Overall Max Boost: 6 dB
    # - Flatness Target: 1 dB
    # - Allow low shelf: checked, -3 to 3 dB
    # - Allow high shelf: checked, -3 to 3 dB
    # - Allow narrow filters below 200 Hz: checked
    # - Vary max Q above 200 Hz: checked

    filter_tasks_settings = {
        "startFrequency": 20,
        "endFrequency": 20000,
        "individualMaxBoostdB": 6,
        "overallMaxBoostdB": 6,
        "flatnessTargetdB": 1,
        "allowLowShelf": True,
        "lowShelfMin": -3,
        "lowShelfMax": 3,
        "allowHighShelf": True,
        "highShelfMin": -3,
        "highShelfMax": 3,
        "allowNarrowFiltersBelow200Hz": True,
        "varyQAbove200Hz": True,
    }

    set_eq_match_target_settings(filter_tasks_settings)

    # Results tracking
    results = []

    # =========================================================================
    # STEP 1: Process FL (Front Left) as reference speaker
    # =========================================================================
    fl_name, fl_target_curve, fl_custom_settings = speakers[0]

    print("\n" + "=" * 60)
    print("PROCESSING REFERENCE SPEAKER: FL (Front Left)")
    print("=" * 60)

    # Find FL measurement
    fl_uuid = find_measurement_by_name(fl_name)
    if not fl_uuid:
        print(f"ERROR: Could not find reference measurement '{fl_name}'")
        return

    # Get FL's initial target level (this will be the reference for all speakers)
    reference_target_level = get_target_level(fl_uuid)
    print(f"Reference target level: {reference_target_level:.1f} dB")

    # Process FL speaker
    if not process_speaker(fl_name, fl_target_curve, fl_custom_settings):
        print("ERROR: Failed to process reference speaker FL")
        return

    # Find the predicted measurement and calculate reference average dB
    fl_predicted_uuid = find_predicted_measurement(fl_name)
    if not fl_predicted_uuid:
        print(f"ERROR: Could not find predicted measurement 'EQ {fl_name}'")
        return

    fl_freq_response = get_frequency_response(fl_predicted_uuid, smoothing="Var")
    reference_avg_db = calculate_average_db(
        fl_freq_response["magnitudes"],
        fl_freq_response["start_freq"],
        fl_freq_response["ppo"],
    )

    print(f"\n*** REFERENCE VALUES ***")
    print(f"FL target level: {reference_target_level:.1f} dB")
    print(f"FL avg dB (500Hz-2kHz): {reference_avg_db:.2f} dB")

    results.append(
        {
            "name": fl_name,
            "success": True,
            "final_avg_db": reference_avg_db,
            "final_target_level": reference_target_level,
            "iterations": 1,
            "is_reference": True,
        }
    )

    # =========================================================================
    # STEP 2: Process remaining speakers with level matching
    # =========================================================================
    # Speakers that should NOT have target level adjusted (process without level matching)
    skip_level_matching = {"FDLfinal", "FDRfinal"}

    for measurement_name, target_curve_path, custom_settings in speakers[1:]:
        # Reset to default settings before each speaker
        set_eq_match_target_settings(filter_tasks_settings)

        # Find the measurement UUID
        uuid = find_measurement_by_name(measurement_name)
        if not uuid:
            print(f"\nERROR: Could not find measurement '{measurement_name}'")
            results.append(
                {
                    "name": measurement_name,
                    "success": False,
                    "final_avg_db": None,
                    "final_target_level": None,
                    "iterations": 0,
                    "is_reference": False,
                }
            )
            continue

        # Check if this speaker should skip level matching
        if measurement_name in skip_level_matching:
            print(f"\n{'=' * 60}")
            print(f"Processing (no level matching): {measurement_name}")
            print("=" * 60)

            # Reset target level to reference before processing
            print(
                f"\n--- Resetting target level to reference ({reference_target_level:.1f} dB) ---"
            )
            set_target_level(uuid, reference_target_level)

            # Process without level matching - just apply EQ
            success = process_speaker(
                measurement_name, target_curve_path, custom_settings
            )

            # Get final target level and predicted avg dB for reporting
            final_target_level = get_target_level(uuid)
            predicted_uuid = find_predicted_measurement(measurement_name)
            final_avg_db = None
            if predicted_uuid:
                freq_response = get_frequency_response(predicted_uuid, smoothing="Var")
                final_avg_db = calculate_average_db(
                    freq_response["magnitudes"],
                    freq_response["start_freq"],
                    freq_response["ppo"],
                )

            results.append(
                {
                    "name": measurement_name,
                    "success": success,
                    "final_avg_db": final_avg_db,
                    "final_target_level": final_target_level,
                    "iterations": 1,
                    "is_reference": False,
                }
            )
            continue

        # Level-match this speaker to FL
        result = match_speaker_level_to_reference(
            uuid=uuid,
            measurement_name=measurement_name,
            target_curve_path=target_curve_path,
            reference_avg_db=reference_avg_db,
            reference_target_level=reference_target_level,
            custom_settings=custom_settings,
            tolerance=0.1,
            max_iterations=50,
        )

        results.append(
            {
                "name": measurement_name,
                "success": result["success"],
                "final_avg_db": result["final_avg_db"],
                "final_target_level": result["final_target_level"],
                "iterations": result["iterations"],
                "is_reference": False,
            }
        )

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print("\n" + "=" * 60)
    print("LEVEL-MATCHED EQ COMPLETE - SUMMARY")
    print("=" * 60)
    print(f"\nReference: FL avg dB (500Hz-2kHz) = {reference_avg_db:.2f} dB")
    print(f"Reference target level: {reference_target_level:.1f} dB\n")

    print(
        f"{'Speaker':<12} {'Status':<10} {'Avg dB':<10} {'Target Level':<14} {'Iterations':<10}"
    )
    print("-" * 60)

    successful = 0
    for r in results:
        status = "OK" if r["success"] else "FAILED"
        avg_db = f"{r['final_avg_db']:.2f}" if r["final_avg_db"] is not None else "N/A"
        target_lvl = (
            f"{r['final_target_level']:.1f}"
            if r["final_target_level"] is not None
            else "N/A"
        )
        ref_marker = " (REF)" if r["is_reference"] else ""

        print(
            f"{r['name']:<12} {status:<10} {avg_db:<10} {target_lvl:<14} {r['iterations']:<10}{ref_marker}"
        )

        if r["success"]:
            successful += 1

    print("-" * 60)
    print(f"Successful: {successful}/{len(speakers)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
