# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

mb-acoustix automates Room EQ Wizard (REW) tasks via its HTTP API. The main script level-matches multiple speakers to a reference speaker (Front Left) by iteratively adjusting EQ target levels until the 500Hz-2kHz average matches.

## Commands

```bash
uv run rew_automate.py    # Run the REW automation script
uv add <package>          # Add a dependency
uv sync                   # Install dependencies from lockfile
```

## Prerequisites

REW must be running with the API enabled: `java -jar REW.jar -api`

## Architecture

**rew_automate.py** - Single-file script that:
1. Connects to REW API at `http://127.0.0.1:4735`
2. Processes the reference speaker (FL) first, calculating its 500Hz-2kHz average dB
3. Iteratively adjusts other speakers' target levels until their predicted measurements match the reference average (within 0.1 dB tolerance)
4. Height speakers (FDL, FDR) skip level matching due to their limited frequency range (20-1000Hz)

**Key functions:**
- `get_frequency_response()` - Fetches Base64-encoded frequency data from REW and decodes it
- `calculate_average_db()` - Computes average dB in a frequency range using RMS averaging
- `match_speaker_level_to_reference()` - Core iteration loop that adjusts target level in 0.1 dB steps until predicted measurement matches reference
- `process_speaker()` - Handles single speaker EQ: set house curve, match target, generate predicted measurement

**Target curves** are stored in `magic-beans/` directory as CSV-like text files (frequency, dB pairs) per speaker channel.

## REW API Notes

- API docs served at `localhost:4735` when REW is running with `-api` flag
- Enable blocking mode (`POST /application/blocking`) for synchronous script operation
- Frequency response data is Base64-encoded 32-bit big-endian floats
- Measurements accessed by UUID (preferred) or index number
- Predicted measurements are named "EQ {original_name}"
- See `rew-api.md` for full API documentation
