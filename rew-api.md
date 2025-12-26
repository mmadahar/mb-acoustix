Title: API

URL Source: https://www.roomeqwizard.com/help/help_en-GB/html/api.html

Markdown Content:
REW has an API accessible over http at localhost (127.0.0.1), the default port is 4735. It cannot be accessed outside the machine REW is running on. To start the API server use the button on the API preferences or run REW with the -api argument. On Windows with the default REW installation that could be done using

C:\Program Files\REW\roomeqwizard.exe -api

On macOS it could be done from a terminal using

open -a REW.app --args -api

To specify a different port, e.g. 4567, add -port 4567. Port numbers below 1024 will be ignored. The default port will be assumed in the examples which follow. To specify a different IP address, e.g. 0.0.0.0, add -host "0.0.0.0", "localhost" is the default.

To run REW without a GUI use the -nogui argument, but if you do that you must use the [application](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#application) shutdown command to close REW when done.

All API GET methods are available whenever the API is running, allowing the API to be used to retrieve data from REW. PUT and POST are also supported by default for most endpoints, but to control REW via the API to make automated sweep measurements requires a [Pro upgrade license](https://www.roomeqwizard.com/upgrades.html).

The API documentation is served by swagger-ui and can be accessed by browsing to localhost:4735. The OpenAPI specification for the API can be accessed at localhost:4735/doc.json or localhost:4735/doc.yaml for JSON or YAML formats. Setting values using the data models can be done with POST or, for models with multiple fields, PUT, however both methods will accept data models with a subset of the defined fields.

### [Index](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

1.   [Usage](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#usage)
    *   [Blocking behaviour for scripting](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#blocking)
    *   [Inhibit graph updates](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#inhibitgraphupdates)
    *   [Message logging](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#logging)
    *   [Array encoding](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#arrays)
    *   [Subscriptions](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions)

2.   [Application](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#application)
3.   [Audio](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#audio)
    *   [Java settings](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#java)
    *   [ASIO settings](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#asio)

4.   [Input levels](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#input-levels)
5.   [Measurements](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#measurements)
    *   [Measurements commands](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#measurements-commands)
    *   [Change measurement name or notes](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#change-summary)
    *   [Frequency response](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#freqresp)
    *   [Group delay](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#groupdelay)
    *   [Impulse response](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#impulseresp)
    *   [IR window settings](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#irwindows)
    *   [Distortion data](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#distortion)
    *   [Commands for individual measurements](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#singlecommands)
        *   [Generate waterfall](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#waterfall)
        *   [Generate spectrogram](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#spectrogram)
        *   [Generate minimum phase](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#generateminphase)
        *   [Minimum or excess phase version](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#minphase)
        *   [Smooth](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#smooth)
        *   [Offset t=0](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#offsettzero)
        *   [Add SPL offset](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#addsploffset)
        *   [Unwrap phase](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#unwrap)
        *   [Generate RT60](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#rt60)

    *   [Processing measurements](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#process-measurements)
        *   [Align SPL](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#alignspl)
        *   [Arithmetic](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#arithmetic)

    *   [EQ and filters](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#eqandfilters)

6.   [Groups](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#groups)
7.   [Measure](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#measure)
8.   [Alignment tool](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#alignment-tool)
9.   [EQ defaults](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#eq)
    *   [EQ matching progress](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#eqprogress)

10.   [Generator](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#generator)
11.   [SPL meter](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#spl-meter)
12.   [RTA](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#rta)
13.   [Stepped measurement](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#stepped-measurement)
14.   [Import](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#import)
    *   [Import frequency response](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#importfrequencyresponse)
    *   [Import impulse response](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#importimpulseresponse)
    *   [Import frequency response data](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#importfreqresponsedata)
    *   [Import impulse response data](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#importimpulseresponsedata)
    *   [Import RTA file](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#importrtafile)
    *   [Import sweep recordings](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#importsweeprecordings)

15.   [Room simulator](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#roomsim)

### [Usage](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

#### [Blocking behaviour for scripting](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

By default, the response to a POST to an endpoint that runs a command may be 200 (OK) or 202 (Accepted). If the command can be completed quickly there will be an OK response. If it will take time complete an Accepted response is issued. An attempt to POST to an endpoint that would run another command while one is already in progress will return Bad Request, with a message that indicates which command is in progress. Commands that take time to complete will generally have an optional resultUrl which REW will POST to when the command completes, but that requires the caller to run a server. Alternatively there are endpoints which can be polled to monitor progress, such as the /measurements/process-result endpoint. A numeric ID is assigned to each command to allow results to be linked to the specific command that generated them when the same command is used repeatedly.

To avoid having to poll the API or to run a server a blocking mode can be enabled by POST to /application/blocking. The endpoint accepts a boolean to enable or disable the blocking behaviour. When blocking is enabled the API will not respond until the requested action is completed, but that may mean the response is delayed by several seconds for long-running tasks. The response will include the result of the action as a ProcessResult.

#### [Inhibit graph updates](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

An /application/inhibit-graph-updates endpoint flag can be set to inhibit any graph updates. This may be useful when running actions which delete or modify measurements to prevent graphs being updated with partial data or errors caused by trying to plot data which is no longer available.

#### [Message logging](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

An /application/logging endpoint flag can be set to log API messages to rew_output.txt in the REW log files folder. This may be useful when debugging.

#### [Array encoding](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Arrays are transferred as Base64-encoded strings generated from the raw bytes of the 32-bit float sample values. Note that byte order is big-endian, data may need to be byte-swapped before encode or after decode. Base64 decoding is well supported in programming languages, here is how to recover the arrays in Java:

    public static float[] decodeArray(String base64Encoded) {
        byte[] bytes = Base64.getDecoder().decode(base64Encoded);
        FloatBuffer buf = ByteBuffer.wrap(bytes).asFloatBuffer();
        float[] floatArray = new float[buf.limit()];
        buf.get(floatArray);
        return floatArray;
    }

Here is some example data to validate Base64 decoding:

Base64 string: PgAAAD6AAAA+wAAAPwAAAA==
Float array:   {0.125f,  0.25f,  0.375f,  0.5f}  

#### [Subscriptions](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Some endpoints allow subscriptions to be added to be notified of changes. That is done by making a POST to its subscribe endpoint. The body contains a _Subscriber_ object which has a URL string and an optional set of parameters. For example, to have notifications posted to a /mysubscriptions endpoint a subscription could be:

{
  "url": "http://127.0.0.1:5374/mysubscriptions"
}

If REW does not get an OK response to an update the subscription will be cancelled. It can also be removed by posting the same _Subscriber_ data to the unsubscribe endpoint. The list of subscribers can be read from subscribers.

### [Application](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /application endpoint provides application-level control of REW. A GET at the /application/commands endpoint returns the list of commands, to issue a command POST it to the /application/command endpoint. There is a shutdown command for use when REW is run without a GUI. There is a "Clear command in progress" command to reset the API's internal record of a command that has been previously accepted by an endpoint. That record is used to prevent commands being run before a previous command has completed, the "Clear command in progress" is a fallback in case an error has prevented a command from completing and clearing the record.

Any errors that have been logged can be read from the /application/errors endpoint, that returns a list of ErrorMessage structures. The most recent error can be read from /application/last-error. Rather than polling for errors with GET a [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified if an error occurs. There are no subscription parameters for error subscriptions.

Any warnings that have been logged can be read from the /application/warnings endpoint, that returns a list of WarningMessage structures. The most recent warning can be read from /application/last-warning. Rather than polling for warnings with GET a [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified if an warning occurs.

To avoid having to poll the API or to run a server a blocking mode can be enabled by POST ing to /application/blocking. The endpoint accepts a boolean to enable or disable the blocking behaviour. When blocking is enabled the API will not respond until the requested action is completed, but that may mean the response is delayed by several seconds for long-running tasks. Once the OK response has been received the result can be read from the response body as a ProcessResult. If REW has not responded within 10 seconds an internal error response will be issued. The setting is persistent, it will remain as set for the next startup.

A flag can be set to inhibit any graph updates by POST ing to /application/inhibit-graph-updates. This may be useful when running actions which delete or modify measurements to prevent graphs being updated with partial data or errors caused by trying to plot data which is no longer available.

A flag can be set to log API messages by POST ing to /application/logging. Messages are logged to rew_output.txt in the REW log files folder. This may be useful when debugging.

### [Audio](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /audio endpoint provides full control of REW's audio input and output selections and associated controls. A GET at the audio endpoint returns its current status, including whether audio is enabled (true unless the -noaudio command line option was used) and whether the audio endpoints are ready for use, which becomes true a few seconds after REW starts up.

On Windows REW has a choice of Java or ASIO audio drivers, on other platforms Java is the only choice. The /audio/driver endpoint allows the driver to be read (GET) or set (POST). The driver choices are available at /audio/driver-types. All Java-related items are under /audio/java/, ASIO-related items are under /audio/asio/. Items under those paths are only accessible when the respective driver has been selected.

The sample rate can be read and set at the /audio/samplerate endpoint. When setting sample rate the unit can be Hz, kHz or absent. If absent Hz is assumed. If the current audio interface cannot support the requested sample rate a 400 Bad Request status will be returned with a list of the rates that are available for selection. The sample rates supported for the current interface selection can be read from /audio/samplerates.

The global option to [treat 32-bit data as 24-bit](https://www.roomeqwizard.com/help/help_en-GB/html/soundcard.html#treat32as24) can be read and set at the /audio/configuration endpoint.

The current input calibration configuration, including any mic cal file(s) being used, can be read at the /audio/input-cal endpoint. This endpoint only supports PUT to make changes since the current input selection the cal data relates to is determined by the driver, input device and input selections. Although the current input selection field in the returned InputCalConfiguration structure is read-only it is recommended that it be included when changing settings, REW will check that it still corresponds to the input in use and reject the request if the input has changed. To clear a cal file set its file path to an empty string. Note that backslashes in file paths must be escaped (meaning a double backslash is required), or forward slashes may be used.

The current output ("soundcard") calibration configuration, including any cal file being used, can be read at the /audio/output-cal endpoint. This endpoint only supports PUT to make changes since the current output selection the cal data relates to is determined by the driver, output device and output selections. Although the current output selection field in the returned OutputCalConfiguration structure is read-only it is recommended that it be included when changing settings, REW will check that it still corresponds to the output in use and reject the request if the output has changed. To clear a cal file set its file path to an empty string. Note that backslashes in file paths must be escaped (meaning a double backslash is required), or forward slashes may be used.

#### [Java settings](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

All Java driver items are under /audio/java/. After selecting the Java driver the current input device, input, output device and output can be read or set at /audio/java/input-device, /audio/java/input, /audio/java/output-device and /audio/java/output. The lists of available devices, inputs and outputs to choose from are at /audio/java/input-devices, /audio/java/inputs, /audio/java/output-devices and /audio/java/outputs. The input and output are specific to their respective device, if the device is changed the list of inputs or outputs available will also change.

By default REW will select the first named (i.e. non default) input or output available when a device is selected, which for many devices will be the only option. After the device and input or output have been selected the input channel and output channel may be selected. If applicable (depending on the timing reference mode for measurement) the timing reference output channel and the input reference (loopback) channel may also be selected. If multiple inputs are being captured ([Pro upgrade](https://www.roomeqwizard.com/help/help_en-GB/html/proupgrades.html)) the last input channel of the input range may be selected. If using [Virtual balanced](https://www.roomeqwizard.com/help/help_en-GB/html/soundcard.html#virtualbalanced) mode the ref input channel is the second channel used to form the balanced pair. The channel endpoints are /audio/java/input-channel, /audio/java/ref-input-channel, /audio/java/last-input-channel, /audio/java/output-channel and /audio/java/ref-output-channel. Input channels are numeric, indexed from 1. The number of input channels can be read from /audio/java/num-input-channels. Output channels are strings and have a L+R option to select the front pair as output. The output channel choices can be read from /audio/java/output-channels, the ref output channel choices from /audio/java/ref-output-channels.

REW supports up to 16 java output channels. Those channels can be mapped to any 16 of the hardware channels on an interface through the /audio/java/output-channel-mapping endpoint. A GET returns the list of the current mappings, the length of the list will be the number of output channels on the currently selected output device up to a maximum of 16. The mappings can be changed by POST of a mapping list to the endpoint. If an empty string is provided as the channel label the hardware channel will be used as the label. If the list posted has more channel entries than the output device supports any mappings outside the range of the output device hardware channel count will be ignored.

The Java driver can be restricted to only accesses the audio interface in stereo by setting the stereoOnly flag at /audio/java/stereo-only. Note that on Windows only the WASAPI-exclusive Java device entries (names starting "EXCL:") support multichannel operation, other entries only offer mono or stereo connections to the interface.

#### [ASIO settings](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

All ASIO driver items are under /audio/asio/. After selecting the ASIO driver the current device, input and output can be read or set at /audio/asio/device/audio/asio/input and /audio/asio/output. The lists of available devices, inputs and outputs to choose from are at /audio/asio/devices, /audio/asio/inputs, and /audio/asio/outputs. The input and output are specific to their respective device, if the device is changed the list of inputs or outputs available will also change.

If applicable (depending on the timing reference mode for measurement) the timing reference output channel and the input reference (loopback) channel may also be selected. If multiple inputs are being captured ([Pro upgrade](https://www.roomeqwizard.com/help/help_en-GB/html/proupgrades.html)) the last input of the input range may be selected. If using [Virtual balanced input](https://www.roomeqwizard.com/help/help_en-GB/html/soundcard.html#virtualbalanced) mode the ref input is the second channel used to form the balanced pair. A second ASIO output can be selected by first enabling it at /audio/asio/secondary-output-enable then selecting it at /audio/asio/secondary-output.

A forced reload of the ASIO driver can be triggered by posting a reload command to /audio/asio/command.

### [Input levels](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /input-levels endpoint provides access to the current input level via [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) whenever the inputs are being monitored. Monitoring is started or stopped by posting a command to the /input-levels/command endpoint. The list of commands is retrieved from the The /input-levels/commands  endpoint. Sending a command to start monitoring input levels will start audio capture if it is not already running. Audio capture will continue until a command is sent to stop monitoring input levels.

The last input levels update can be read from the /input-levels/last-levels endpoint. That will return the last InputLevels object generated by an input levels update. More commonly levels would be monitored through a subscription.

A subscription can be added by making a POST to the /input-levels/subscribe endpoint. The body contains a _Subscriber_ object which has a URL string and an optional "unit" parameter that specifies the units of the input level values. The accepted units can be read from the /input-levels/units endpoint. If the unit is omitted levels are returned as dBFS. To have input level updates posted to a /input-levels endpoint a subscription could be:

{
  "url": "http://127.0.0.1:5374/input-levels",
  "parameters": {"unit": "dBV"}
}

Levels are returned as an InputLevels object which has the unit, arrays of the rms and peak levels for each input since the last update and a timeSpanSeconds value with the time period over which the values were calculated.

### [Measurements](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /measurements endpoint provides access to any measurements REW has generated or loaded. Measurements may be referenced by their index number (starting from 1) or by their UUID. **Using index numbers for measurements is NOT recommended**. Index numbers change when measurements are added to or removed from a [group](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#groups) or when other measurements are deleted or added to or removed from a group. The UUID for a measurement is available from the measurement summary.

**N.B.** If a measurement is loaded more than once each will have the same UUID.

A GET at the /measurements endpoint returns a summary list of the current measurements. A GET at the /measurements/:id gets the summary for the measurement at index id or with UUID id. A DELETE at the /measurements/:id endpoint deletes that measurement, DELETE at the /measurements endpoint deletes all the measurements. **N.B. There are no delete confirmations, use with care!**

A [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified of any changes made to the list of measurements, including measurements being added or deleted, the contents of a measurement changing, or a measurement becoming selected. There are no parameters for measurement subscriptions. The change notifications are conveyed in a MeasurementsListChange object, which has a string with a description of the type of change and indices for the range of measurements the change affects.

A GET at the /measurements/selected-uuid endpoint returns the UUID of the currently selected measurement. To select a measurement POST its UUID to /measurements/selected-uuid.

A GET at the /measurements/selected endpoint returns the index of the currently selected measurement. To select a measurement POST its index to /measurements/selected.

#### [Measurements commands](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

A GET at the /measurements/commands endpoint returns a list of commands, to issue a command POST it to the /measurements/command endpoint. The "Sort alphabetically" command sorts the list of measurements by measurement name, and by date if the names are the same. The "Save all" command has a parameter for the path to the file to be saved to, if the file exists it will be overwritten. A note to be saved with the measurement can optionally be specified as a second parameter. The "Load" command has a list of the filenames to load as parameters in the command. Note that if a file path has backslash as the path separator the string for the path will need to escape the backslash entries, i.e. use a double backslash instead or replace backslash by forward slash. Here are examples of loading two mdat files and of saving all files:

{
  "command": "Load",
  "parameters": [
    "C:/Users/myusername/REW/file1.mdat",
    "C:/Users/myusername/REW/file2.mdat"
  ]
}
    {
  "command": "Save all",
  "parameters": [
    "C:/Users/myusername/REW/latest.mdat",
    "These are my latest files"
  ]
}
    
The "Dirac" command generates a new measurement with a pure impulse (dirac delta). The parameters are the sample rate for the measurement, the total number of samples for the response and the zero-based index of the peak. Here is an example:

{
  "command": "Dirac",
  "parameters": [
    "48000", "131072", "65536"
  ]
}
    
#### [Change name or notes](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

A measurement's name and/or notes can be changed by a PUT at the /measurements/:id endpoint, putting a MeasurementSummary object which has the title and/or notes field set to the new value.

#### [Frequency response](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The frequency response for a measurement can be obtained by a GET at /measurements/:id/frequency-response. A FrequencyResponse object is returned, with a smoothing setting, a start frequency, a points-per-octave figure (for log-spaced data) or a frequency step value (for linear-spaced data), and Base64-encoded strings of response magnitudes and phases generated from the raw bytes of the 32-bit float magnitude and phase values at each frequency.

The default unit for the magnitude data is SPL but other units can be requested by including a unit query value in the url, e.g. ?unit=dBFS. The list of units available can be read from /measurements/frequency-response/units. Phase values are in degrees.

The default smoothing is whatever the measurement currently uses, but other smoothings can be requested by including a smoothing query value in the url, e.g. ?smoothing="1/12". The list of smoothing choices can be read from /measurements/frequency-response/smoothing-choices.

Whether the returned data is log-spaced or linear-spaced depends on the measurement, but log-spaced data can be forced by including a ppo query value in the url, e.g. ?ppo=96. Note that to avoid sampling artefacts log-spaced data will be smoothed to ppo/2 if a greater smoothing has not already been applied. The frequency axis for the result data starts at the start frequency in Hz returned in the FrequencyResponse object and the frequency values corresponding to the magnitude array entries are either linearly spaced from the start frequency, with a corresponding freqStep Hz value to give the interval, or log spaced with a corresponding points-per-octave value, which can be used to calculate the ratio between successive values, 2^(1.0/ppo). Alternatively the frequency at any zero-based index for log spaced data is startFreq*e^(index*ln(2)/ppo).

#### [Group delay](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The group delay for a measurement can be obtained by a GET at /measurements/:id/group-delay. A FrequencyResponse object is returned, with a smoothing setting, a start frequency, a points-per-octave figure (for log-spaced data) or a frequency step value (for linear-spaced data), and Base64-encoded strings of the group delay in the magnitudes field. The unit for the group delay data is seconds. Smoothing and ppo options are the same as frequency response queries.

#### [Impulse response](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The impulse response for a measurement (if it has one) can be obtained by a GET at /measurements/:id/impulse-response. An ImpulseResponse object is returned, with a start time, a description of the timing reference used, a sample interval in seconds, a sample rate in Hz and a Base64-encoded string of response data. The default unit for the data is Percent but other units can be requested by including a unit query value in the url, e.g. ?unit=dBFS. The list of units available can be read from /measurements/impulse-response/units. Impulse response queries can return the windowed portion of the data by including a query value ?windowed=true in the url. Data is normalised by default, for data that is not normalised include a query value ?normalised=false in the url.

The impulse response for a measurement's filters (if there are any) can be obtained by a GET at /measurements/:id/filters-impulse-response. An ImpulseResponse object is returned, with a start time, a sample interval in seconds, a sample rate in Hz and a Base64-encoded string of response data. The sample rate and length of the response must be specified by including query values in the url, e.g. ?samplerate=48000&length=65536. The maximum length accepted is 4,194,304 samples.

#### [IR window settings](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

A measurement's impulse response window settings can be accessed at the /measurements/:id/ir-windows endpoint. The settings are in an IRWindows object, there is an example below. The FDW width can be in cycles or octaves according to the current selection in the REW View preferences. Either can be used when changing window setting by PUT or POST.

{
  "leftWindowType": "Tukey 0.25",
  "rightWindowType": "Tukey 0.25",
  "leftWindowWidthms": 125,
  "rightWindowWidthms": 500,
  "refTimems": 0,
  "addFDW": true,
  "fdwWidthCycles": 15
}
    
#### [Distortion data](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

A measurement's distortion data can be accessed at the /measurements/:id/distortion endpoint. The data is returned in a Distortion object which has a String describing the type of data, an array of column header strings and a 2D array of Doubles with the data. The default unit for the data is percent but other units can be requested by including a unit query value in the url, e.g. ?unit=dBr. The list of units can be read from /measurements/distortion-units. Sweep distortion data is returned at the PPO value included in the url, e.g. ?ppo=12, or at 3 PPO if not specified. PPO is not required for other types of distortion data. The list of PPO choices can be read from /measurements/distortion-ppo-choices.

#### [Commands for individual measurements](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

An individual measurement can be processed by POST of a ProcessSingleMeasurement object to the /measurements/:id/command endpoint. The list of commands for individual measurements can be retrieved from the /measurements/:id/commands endpoint. They include commands to Save, generate a minimum phase version, generate an excess phase version, generate a Mic in box correction, make a response copy, merge cal data to IR, Trim IR to windows, smooth, generate waterfalls, generate spectrograms, Estimate IR delay, offset t=0, add an SPL offset, invert, wrap phase, unwrap phase and generate RT60 data. Some of those commands produce a new measurement (generate a minimum phase version, generate an excess phase version, generate a Mic in box correction, make a response copy, merge cal data to IR, Trim IR to windows), others make changes to the measurement itself.

The commands may have associated parameters, for example the save command requires a "filename" parameter with the filename to save to, smooth requires a "smoothing" setting. Note that if a file path has backslash as the path separator the string for the path will need to escape the backslash entries, i.e. use a double backslash instead or replace backslash by forward slash. Here is an example of a save command:

{
  "command": "Save",
  "parameters": {filename: "c:/users/myusername/downloads/myfile.mdat"}
}
    
The command has an optional resultUrl, if included the result of the process will be posted to the URL. The process result can be read from /measurements/process-measurements-result but may not be available immediately, some processes take time to complete. The ProcessMeasurementsResult object has the name of the process it relates to, a message (which may be absent or empty) and a set of results for each measurement that was processed which are returned as a map of result names and result values, all strings. For individual measurements there will be one map entry.

#### [Generate waterfall](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Generate waterfall and generate equalised waterfall require a "mode" parameter ("Fourier" or "Burst decay"), a parameter "slices" for the number of slices to generate and a set of additional parameters the depend on the mode. Fourier requires "left window type", "right window type", "window width ms", "time range ms", "rise time ms" and "use csd mode" parameters. Burst decay requires "bandwidth" and "periods" parameters. Here are some examples of commands to generate a waterfall:

{
  "command": "Generate waterfall",
  "parameters": {
    "mode": "Fourier",
    "slices": "101",
    "left window type": "Hann",
    "right window type": "Tukey 0.25",
    "window width ms": "300",
    "time range ms": "500",
    "rise time ms": "150",
    "use csd mode": "false",
    "ppo": "48",
    "smoothing": "1/48"},
  "resultUrl": "http://127.0.0.1:5374/waterfalls"
}
    {
  "command": "Generate waterfall",
  "parameters": {
    "mode": "Burst decay",
    "slices": "101",
    "periods": "30",
    "ppo": "48",
    "bandwidth": "1/3"},
  "resultUrl": "http://127.0.0.1:5374/waterfalls"
}
    
#### [Generate spectrogram](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Generate spectrogram also requires a "mode" parameter ("Fourier", "Wavelet, "Airy CWT, "Morlet CWT, "Burst decay"), a parameter "slices" for the number of slices to generate, a "ppo" parameter for the frequency resolution of the result, an "amplitude" parameter for the data values and a set of additional parameters the depend on the mode. Fourier requires "window type", "window width ms", "before ms" and "after ms" parameters. Burst decay requires "bandwidth" and "periods" parameters. The wavelet modes require "bandwidth", "before ms" and "after ms" parameters. Here are some examples of commands to generate a spectrogram:

{
  "command": "Generate spectrogram",
  "parameters": {
    "mode": "Fourier",
    "slices": "551",
    "amplitude": "Log (dB SPL)",
    "window type": "Gaussian",
    "window width ms": "300",
    "before ms": "50",
    "after ms": "500",
    "ppo": "48"},
  "resultUrl": "http://127.0.0.1:5374/spectrograms"
}
    {
  "command": "Generate spectrogram",
  "parameters": {
    "mode": "Morlet CWT",
    "slices": "551",
    "amplitude": "Linear (% peak)",
    "before ms": "5",
    "after ms": "50",
    "bandwidth": "1/3",
    "ppo": "48"},
  "resultUrl": "http://127.0.0.1:5374/spectrograms"
}
    
The generate waterfall and spectrogram commands return the 2D data in a ProcessResult in key "0". The result includes an array of the frequencies, an array of the times (or periods for Burst Decay) and a set of arrays of SPL data vs frequency for each time index. It is best to specify a resultUrl for those as the generation can take some time. Note that the commands do not affect the REW GUI and will not produce a result in the GUI, they are provided as a way to generate and extract data.

#### [Generate minimum phase](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Generate minimum phase runs a minimum phase calculation for the measurement. It require parameters for "include cal", "append lf tail" and "append hf tail" which are boolean values. If "append lf tail" is true the parameters must include an "lf tail start" frequency in Hz and an "lf tail slope" in dB/octave, which must be ≥ 0. If "append hf tail" is true the parameters must include an "hf tail start" frequency in Hz and an "hf tail slope" in dB/octave, which must be ≤ 0, along with a "frequency warping" boolean. If either "append lf tail" or "append hf tail" are false a "replicate data" boolean is required. Here is an example of a command to generate minimum phase:

{
  "command": "Generate minimum phase",
  "parameters": {
    "include cal": "true",
    "append lf tail": "true",
    "lf tail start": "27",
    "lf tail slope": "12.0",
    "append hf tail": "true",
    "hf tail start": "15000",
    "hf tail slope": "-18.0",
    "frequency warping": "false",
    "replicate data": "false"},
  "resultUrl": "http://127.0.0.1:5374/minphase"
}
    
#### [Minimum or excess phase version](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Minimum phase version and Excess phase version create new measurements with the minimum or excess phase of the source measurement. They require parameters for "include cal", "append lf tail" and "append hf tail" which are boolean values. If "append lf tail" is true the parameters must include an "lf tail start" frequency in Hz and an "lf tail slope" in dB/octave, which must be ≥ 0. If "append hf tail" is true the parameters must include an "hf tail start" frequency in Hz and an "hf tail slope" in dB/octave, which must be ≤ 0, along with a "frequency warping" boolean. If either "append lf tail" or "append hf tail" are false a "replicate data" boolean is required. Here is an example of a command to generate a minimum phase version

{
  "command": "Minimum phase version",
  "parameters": {
    "include cal": "true",
    "append lf tail": "true",
    "lf tail start": "27",
    "lf tail slope": "12.0",
    "append hf tail": "true",
    "hf tail start": "15000",
    "hf tail slope": "-18.0",
    "frequency warping": "false",
    "replicate data": "false"},
  "resultUrl": "http://127.0.0.1:5374/minphase"
}
    
#### [Smooth](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Smooth requires a smoothing parameter:

{
  "command": "Smooth",
  "parameters": {
    "smoothing": "1/3"
  }
}
    
#### [Offset t=0](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Offset t=0 requires parameters for "offset" and "unit", where unit is for the offset value and may be seconds, metres, feet or samples. Here is an example of a command to offset t=0

{
  "command": "Offset t=0",
  "parameters": {
    "offset": "0.5",
    "unit": "metres"},
  "resultUrl": "http://127.0.0.1:5374/result"
}
    
#### [Add SPL offset](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Add SPL offset requires an offset parameter:

{
  "command": "Add SPL offset",
  "parameters": {
    "offset": -3.2
  }
}
    
#### [Unwrap phase](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Unwrap phase requires a frequency parameter to set the reference frequency, where the unwrapped phase will be within -180 .. 180 degrees. The frequency must be within the range of the measurement.

{
  "command": "Unwrap phase",
  "parameters": {
    "frequency": 1000
  }
}
    
#### [Generate RT60](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Generate RT60 requires an octave fraction (one or one-third), a filter order and parameters for zero phase or reverse filtering. One-third octave can be specified as "3" or "1/3", the former avoiding the "/" character.

{
  "command": "Generate RT60",
  "parameters": {
    "octaveFrac": 3,
    "filterOrder": 6,
    "zeroPhaseFiltered": true,
    "reverseFiltered": false
  }
}
    
The RT60 results (including other ISO 3382 parameters) can be read from the /measurements/:id/rt60  endpoint, specifying the octave fraction as a query parameter, e.g. ?octaveFrac=1. The results are returned as a map of frequency versus parameter values, the first entry with frequency 0 being the unfiltered (full band) result.

#### [Processing measurements](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

A set of measurements can be processed by POST of a ProcessMeasurements object to the /measurements/process-measurements endpoint. The list of process commands can be read from /measurements/process-commands and includes:

        
    "Align SPL",
    "Time align",
    "Align IR start",
    "Cross corr align",
    "Vector average",
    "RMS average",
    "dB average",
    "Magn plus phase average",
    "dB plus phase average",
    "Vector sum",
    "Smooth",
    "Arithmetic",
    "Remove IR delays"
    
The command parameters will vary according to the process to be carried out, see details below. The ProcessMeasurements object has a list of either the numeric indices or a list of the UUID strings of the measurements to be processed. It also has an optional URL, if included the result of the process will be posted to the URL. The process result can be read from /measurements/process-result but may not be available immediately, some processes take time to complete. The ProcessMeasurementsResult object has the name of the process it relates to, a message (which may be absent or empty) and a set of results for each measurement that was processed which are returned as a map of result names and result values, all strings.

The Align SPL process has these parameters:

*   targetdB: either "average" to align to the average SPL of the measurements or an SPL value in dB, e.g. "75.0" 
*   frequencyHz: the centre frequency for the alignment in Hz, e.g. "1000" 
*   spanOctaves: the alignment span in octaves, e.g. "2" 

#### [Align SPL](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Here is an example of a ProcessMeasurements object to align SPL:

{
  "processName": "Align SPL",
  "measurementIndices": [1,3,4],
  "parameters": {"targetdB": "85.0", "frequencyHz": "1000", "spanOctaves": 2},
  "resultUrl": ""
}
    
The results of Align SPL are available as soon as the process command is acknowledged.

#### [Arithmetic](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The Arithmetic process operates on pairs of measurements, the first measurement is designated A, the second B. Arithmetic has these parameters, function is mandatory but others are optional if applicable to the specified function:

*   function: The arithmetic function to perform, the list of functions can be read from /measurements/arithmetic-functions
*   maxGain: gain limit in dB for division and inversion functions, omit for no limiting 
*   lowerLimit: the lower frequency limit in Hz for band limited functions (division or inversion) 
*   upperLimit: the lower frequency limit in Hz for band limited functions (division or inversion) 
*   mergeFrequency: the frequency at which to perform a merge function 
*   mergeBlend: true if a merge function is to be blended over a span 
*   targetLevel: target level in dB for an inversion function 
*   autoTarget: true if target level is to be set automatically for an inversion function 
*   excludeNotches: true if notches are to be excluded for an inversion function 

Here is an example of a ProcessMeasurements object to perform A * B trace arithmetic:

{
  "processName": "Arithmetic",
  "measurementIndices": [1,3],
  "parameters": {"function": "A * B"},
  "resultUrl": ""
}
    
Here is an example of a ProcessMeasurements object to perform 1 / A trace arithmetic:

{
  "processName": "Arithmetic",
  "measurementIndices": [1,2],
  "parameters": {
    "function": "1 / A",
    "maxGain": "3.0",
    "lowerLimit": "100",
    "upperLimit": "1000",
    "targetLevel": "75.0",
    "autoTarget": "false",
    "excludeNotches": "true"
  },
  "resultUrl": ""
}    
    
#### [EQ and filters](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

A measurement's equaliser selection can be read from the /measurements/:id/equaliser endpoint and changed by a POST to that endpoint. The available equalisers can be read from the /eq/equalisers endpoint.

A measurement's target settings can be read from the /measurements/:id/target-settings endpoint and changed by a POST or PUT to that endpoint.

A measurement's target level can be read from the /measurements/:id/target-level endpoint and changed by a POST to that endpoint.

A measurement's room curve settings can be read from the /measurements/:id/room-curve-settings endpoint and changed by a POST or PUT to that endpoint.

A measurement's filters can be read from the /measurements/:id/filters endpoint. A list of FilterSetting objects is returned with the current settings for each filter of the measurement's equaliser. Note that the number and type of filters available depend on the equaliser. The settings for an individual filter can be changed by a PUT of a FilterSetting object to the endpoint. Multiple (or all) filters can be changed by a POST of a FilterList object to the endpoint.

A measurement's EQ target response can be read from the /measurements/:id/target-response endpoint. A FrequencyResponse object is returned, with a start frequency, a points-per-octave figure and a Base64-encoded string of response magnitudes. The default unit for the response data is SPL but other units can be requested by including a unit query value in the url, e.g. ?unit=dBFS. The list of units available can be read from /measurements/frequency-response/units. The data returned is log spaced at 96 PPO unless there is a ppo query value in the url, e.g. ?ppo=48.

The frequency response for the predicted result of a measurement's EQ filters can be obtained by a GET at /measurements/:id/eq/frequency-response. A FrequencyResponse object is returned, with a smoothing setting, a start frequency, a points-per-octave figure (for log-spaced data) or a frequency step value (for linear-spaced data), and Base64-encoded strings of response magnitudes and phases generated from the raw bytes of the 32-bit float magnitude and phase values at each frequency. The default unit for the magnitude data is SPL but other units can be requested by including a unit query value in the url, e.g. ?unit=dBFS. The list of units available can be read from /measurements/frequency-response/units. The default smoothing is whatever the measurement currently uses, but other smoothings can be requested by including a smoothing query value in the url, e.g. ?smoothing="1/12". The list of smoothing choices can be read from /measurements/frequency-response/smoothing-choices. Whether the returned data is log-spaced or linear-spaced depends on the measurement, but log-spaced data can be forced by including a ppo query value in the url, e.g. ?ppo=96. Note that to avoid sampling artefacts log-spaced data will be smoothed to ppo/2 if a greater smoothing has not already been applied.

The group delay for the predicted result of a measurement's EQ filters can be obtained by a GET at /measurements/:id/eq/group-delay. A FrequencyResponse object is returned, with a smoothing setting, a start frequency, a points-per-octave figure (for log-spaced data) or a frequency step value (for linear-spaced data), and Base64-encoded strings of the group delay in the magnitudes field. The unit for the group delay data is seconds. Smoothing and ppo options are the same as frequency response queries.

The impulse response for for the predicted result of a measurement's EQ filters (if the measurement itself has an impulse response) can be obtained by a GET at /measurements/:id/eq/impulse-response. An ImpulseResponse object is returned, with a start time, a description of the timing reference used, a sample interval in seconds, a sample rate in Hz and a Base64-encoded string of response data. The default unit for the data is Percent but other units can be requested by including a unit query value in the url, e.g. ?unit=dBFS. The list of units available can be read from /measurements/impulse-response/units. Impulse response queries can return the windowed portion of the data by including a query value ?windowed=true in the url. Data is normalised by default, for data that is not normalised include a query value ?normalised=false in the url.

A GET at the /measurements/eq/commands endpoint returns a list of EQ commands, including "Calculate target level", "Match target", "Optimise gains", "Optimise gains and Qs", "Optimise gains, Qs and Fcs", "Generate predicted measurement", "Generate filters measurement" and "Generate target measurement". To issue a command POST it to the /measurements/:id/eq/command endpoint. None of the commands require parameters. The commands have an optional URL, if included the result of the command will be posted to the URL. The result can also be read from /measurements/process-result but may not be available immediately, some commands take time to complete. To add a subscription to be notified of progress during EQ target matching see the [/eq/subscribe](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#eqprogress) endpoint.

### [Groups](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

Measurements may be part of a group. The /groups endpoint provides access to any groups REW has generated or loaded. Groups are referenced by their UUID, as group names may be changed by the user. The UUID for a group is available from the GroupInfo. If a measurement is in a group the group name, notes and UUID will be included in the measurement's summary. The current list of measurements in a group can be obtained by a GET at the /groups/:uuid/measurements endpoint. A measurement can be placed in a group by posting a MeasurementSummary containing the measurement's UUID to /groups/:uuid/measurements or by posting a MeasurementSummary with the required group UUID at the /measurements/:id/ endpoint for the measurement. The MeasurementSummary only needs to contain the measurement's UUID, other fields may be omitted.

A new group can be created by posting a GroupInfo object to the /groups endpoint. Any UUID in the GroupInfo object will be ignored. The new group will be returned as a GroupInfo object including its UUID. If the name in the GroupInfo object already exists in a group there will be a bad request response.

Individual groups may be accessed by including their UUID in the path. A group's name or notes may be changed by PUT of a GroupInfo object with the fields to change to the /groups/:uuid endpoint.

A DELETE at the /groups/:uuid endpoint deletes that group, DELETE at the /groups endpoint deletes all the groups. **N.B. There are no delete confirmations, use with care!**

A [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified of any changes that are made to the list of groups, including groups being added or deleted. There are no parameters for group subscriptions. The change notifications are conveyed in a GroupsListChange object, which has a string with a description of the type of change and the ID, name and notes for the group changed.

### [Measure](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /measure endpoint provides access to REW's measurement capabilities. A GET at the /measure/commands endpoint returns the list of commands, to issue a command POST it to the /measure/command endpoint. The commands allow different types of measurement (SPL, impedance, impedance calibration) to be made. There is also a command to cancel a measurement that is in progress.

The /measure/naming endpoint provides access to the naming settings. They can be changed by POST or PUT, the response will show the format of the next measurement name. The options for naming can be read from /measure/naming/naming-options. If a date or time is being added to the measurement name the formats for that can be read from /measure/naming/date-time-formats. The empty string format option "" uses the default date and time format for the machine.

The /measure/notes endpoint provides access to the notes that will be included in the next measurement made. They can be changed or set by POST.

The measurement level can be read and set at the /measure/level endpoint. A variety of units are supported, the list of accepted units is available at /measure/level/units. The default unit is dBFS, if a unit is not specified when setting level dBFS will be assumed.

The /measure/protection-options endpoint provides access to the options to abort measurements if heavy clipping is detected on the input or if the SPL exceeds a limit. They can be changed by POST or PUT.

The /measure/sweep/configuration endpoint provides access to the measurement sweep configuration, including start frequency, end frequency, length and whether to fill silence with dither. The configuration can be changed using POST or PUT.

The /measure/sweep/repetitions endpoint provides access to the number of sweep repetitions. The number can be changed using POST. Note that multiple sweeps cannot be used with USB mics or when using the acoustic or wired timing reference modes.

The /measure/timing endpoint provides access to settings for the timing reference. There are endpoints to get and set the reference (/measure/timing/reference) and further endpoints to configure the options for the chosen reference.

The /measure/timing-offset endpoint provides access to the timing offset to apply when using a timing reference. The value can be changed using POST.

The /measure/playback-mode endpoint provides access to the playback mode. The value can be changed using POST, the options can be read from /measure/playback-mode/choices. The stimulus file for file playback is set by POST ing the path to /measure/file-playback-stimulus.

The /measure/measurement-mode endpoint provides access to the measurement mode, for single, repeated, ramped or sequential measurements. The value can be changed using POST, the options can be read from /measure/measurement-mode/choices.

The /measure/number-of-repetitions endpoint provides access to the number of measurements that will be made when measuring SPL in repeated or ramped measurement mode with playback from REW. The value can be changed using POST.

The start and end levels for ramped measurements can be read and set at the /measure/start-level and /measure/end-level endpoints. A variety of units are supported, the list of accepted units is available at /measure/level/units. The default unit is dBFS, if a unit is not specified when setting level dBFS will be assumed.

The /measure/sequential-channels endpoint provides access to the list of channels that will be measured when measuring SPL in sequential measurement mode with playback from REW. The list can be changed using POST. The full list of channel choices can be read from /measure/sequential-choices.

The /measure/start-delay endpoint provides access to the delay in seconds before a measurement starts. The value can be changed using POST.

The /measure/invert-second-output endpoint provides access to whether to invert the second output when two outputs are driven. The value can be changed using POST.

The /measure/fill-silence-with-dither endpoint provides access to setting for whether to fill silent parts of the output with 16-bit dither to ensure the replay path is active. The value can be changed using POST.

The /measure/capture-noise-floor endpoint provides access to setting for whether to capture the noise floor before an SPL measurement. The value can be changed using POST.

A [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified of progress during a measurement. There are no parameters for measure subscriptions. The change notifications are conveyed as a string.

### [Alignment tool](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /alignment-tool endpoint provides access to REW's alignment tool. See [Alignment tool](https://www.roomeqwizard.com/help/help_en-GB/html/graph_allspl.html#alignmenttool) for details of the operation of the tool.

A GET at /alignment-tool/commands returns the list of commands the tool accepts. Use POST to send a command to /alignment-tool/command. The alignment mode is at the /alignment-tool/mode endpoint. The choice of modes can be read from /alignment-tool/modes. The frequency at which the alignment is performed is at the /alignment-tool/frequency endpoint. The alignment is performed on a pair of measurements A and B, the endpoints for the index of each of those measurements are /alignment-tool/index-a and /alignment-tool/index-b. The gain, delay and invert for each measurement have individual endpoints to GET them, they can be changed by POST. The allowed delay range can be read from /alignment-tool/max-positive-delay and /alignment-tool/max-negative-delay and changed by POST. After carrying out an alignment the new delay in milliseconds for measurement B can be read from the /alignment-tool/delay-b endpoint. A FrequencyResponse object for the aligned sum can be read from /alignment-tool/aligned-frequency-response. If the impulse alignment mode is being used the filtered impulse responses can be read from /alignment-tool/filtered-impulse-response-a and /alignment-tool/filtered-impulse-response-b.

If the alignment command has a "resultUrl" parameter the result of the command will be posted to the URL as a ProcessResult object. The result can also be read from /alignment-tool/result.

### [EQ defaults](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /eq endpoint provides access to the default EQ settings. The list of equalisers can be read from the /eq/equalisers endpoint, results for a specific manufacturer can be requested by including a manufacturer query value in the url, e.g. ?manufacturer="miniDSP". The list of equaliser manufacturers can be read from the /eq/manufacturers endpoint. The default equaliser to use for new measurements can be read from /eq/default-equaliser and changed by posting to that endpoint. Note that changing the default equaliser will not alter the equaliser selection for any existing measurements.

The default target settings can be read from the /eq/default-target-settings endpoint and changed by a POST or PUT to that endpoint.

The default target level can be read from the /eq/default-target-level endpoint and changed by a POST to that endpoint.

The default room curve settings can be read from the /eq/default-room-curve-settings endpoint and changed by a POST or PUT to that endpoint.

The path to any house curve file being used can be read from the /eq/house-curve endpoint and changed by a POST to that endpoint. It can be cleared by a DELETE at that endpoint or by posting an empty string. The log interpolation flag can be set or cleared by POSTing true or false to /eq/house-curve-log-interpolation, that should be done before setting the file path.

The settings used when matching a response to a target can be read from the /eq/match-target-settings endpoint and changed by a POST or PUT to that endpoint.

#### [EQ matching progress](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

A [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified of progress during EQ matching. There are no parameters for EQ subscriptions.

### [Generator](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /generator endpoint provides full control of REW's [signal generator](https://www.roomeqwizard.com/help/help_en-GB/html/siggen.html). A GET at the /generator/status endpoint returns its current status, including whether it is enabled, whether it is playing, the current signal selected and the output level. The generator is not enabled if there is no available audio output.

The /generator/signal endpoint is for signal selection and configuration. A GET at the signal endpoint returns the currently selected signal, a PUT selects a new signal. The list of available signals can be retrieved by a GET at /generator/signals.

Each signal has an associated set of configuration options. For the current signal they are at /generator/signal/configuration. The configurations for other signals can be accessed at /generator/signals/{signalname}/configuration. Details of the effect of the configuration settings are in the [signal generator help](https://www.roomeqwizard.com/help/help_en-GB/html/siggen.html). Note that some settings are shared between signals. For example, the addDither setting for the sine signal is also used by the square signal and the sawtooth signal, the ditherBits setting for the sine signal is also used for other signals that have an option to add dither. Configuration options can be updated collectively or individually by POST or PUT to the configuration endpoint using the setting names and types returned in the GET response. Partial configuration are accepted by both PUT and POST. The full configuration will often contain settings that are specific to a particular mode of a signal and do not need to be included when using other modes, for example the noise configurations have setting for custom noise filtering which are only applicable when using the custom option.

Some signals accept commands, currently these are the tone group of signals which have commands to step to the previous or next one-third octave centre frequency. A GET at /generator/signal/commands returns the list of commands the current signal accepts, which may be empty. The commands for other signals can be accessed at /generator/signals/{signalname}/commands. Only the current signal can accept commands, use POST to send a command to /generator/signal/command.

The generator output level can be read and set at the /generator/level endpoint. The generator supports a variety of units for output level, the list of accepted units is available at /generator/level/units. The default unit is dBFS, if a unit is not specified when setting level dBFS will be assumed.

The generator output frequency can be read and set at the /generator/frequency endpoint. When setting frequency the unit can be Hz, kHz or absent. If absent Hz is assumed. If the current signal does not have a frequency setting a 400 Bad Request status will be returned.

The /generator/invert-second-output endpoint provides access to whether to invert the second output when two outputs are driven. The value can be changed using POST.

The generator has two protection settings that will stop the generator if the input signal exceeds a dB SPL threshold or if excessive clipping is detected on the input. Those settings can be read and configured at the /generator/protection endpoint.

The generator is started and stopped by using POST to send a command to /generator/commands. A GET at the commands endpoint returns the list of commands the generator accepts.

### [SPL meter](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /spl-meter/ endpoint provides access to the REW SPL meters and the SPL readings. REW can have up to four SPL meters with a Pro upgrade or one without. The meter being addressed is identified by a numeric ID after the endpoint, e.g. /spl-meter/1/ for the first SPL meter. An SPL meter is started or stopped by posting a command to the /spl-meter/{id}/command endpoint. The list of commands can be read from the /spl-meter/commands  endpoint.

SPL meters are configured by sending an SPLMeterConfiguration to the /spl-meter/{id}/configuration endpoint. The SPLMeterConfiguration includes a display mode, weighting and filter setting. Note that the display mode only affects the meter display, data read from the meter always include SPL, Leq and SEL values. The list of display modes can be read from the /spl-meter/modes endpoint. The list of weightings can be read from the /spl-meter/weightings endpoint. The list of filters can be read from the /spl-meter/filters endpoint. Here is an example configuration:

{
  "mode": "SPL",
  "weighting": "C",
  "filter": "Slow",
  "highPassActive": false,
  "rollingLeqActive": true,
  "rollingLeqMinutes": 15
}
The last SPL meter update can be read from the /spl-meter/{id}/levels endpoint. That will return the last SPLValues object generated by an update. More commonly levels would be monitored through a [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions). SPLValues includes SPL, Leq and SEL figures.

{
  "meterNumber": 1,
  "weighting": "C",
  "filter": "Slow",
  "spl": 96.9540023803711,
  "leq": 96.91223907470703,
  "isRollingLeq": true,
  "rollingLeqMinutes": 15,
  "leq1m": 96.91223907470703,
  "leq10m": 96.91223907470703,
  "sel": 110.3396232402612,
  "elapsedTime": 22.015999999999995}

### [RTA](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /rta endpoint provides control of REW's [RTA](https://www.roomeqwizard.com/help/help_en-GB/html/spectrum.html). A GET at the /rta/commands endpoint returns the list of commands, to issue a command POST it to the /rta/command endpoint.

Among the RTA commands is "Save graph image". The image capture settings can be read and configured using the /rta/image-capture-settings endpoint.

The RTA graph Y axis unit can be read and set from the /rta/y-axis endpoint. The list of axis units available can be read from /rta/y-axis/units. The graph limits can be read and set from the /rta/graph-limits endpoint. The graph cursor X position can be read and set from the /rta/cursor-x endpoint.

The RTA setup can be queried or set via the /rta/configuration, /rta/appearance-configuration and /rta/distortion-configuration endpoints.

The current status of the RTA (whether it is enabled and whether it is running) can be read from the /rta/status endpoint. Rather than polling status with GET a [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified whenever the RTA status is updated. There are no parameters for status updates.

The current RTA input level can be read from the /rta/levels endpoint, that returns a list of RTALevel structures. The list has one RTALevel entry unless stereo inputs are being captured, when there are two. The data has a nanosecond timestamp and a running sum of the number of samples processed by the RTA since it was last started or restarted. The default unit for the level data is SPL but other units can be requested by including a unit query value in the url, e.g. ?unit=dBFS. The list of units available can be read from /rta/levels/units. Rather than polling levels with GET a [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified whenever the RTA levels are updated. The subscription parameters can contain the required unit, for example:

{
  "url": "http://127.0.0.1:5374/levels",
  "parameters": {unit: "dBFS"}
}            

The rms and peak RTA responses can be read from the /rta/captured-data and /rta/captured-peak-data endpoints respectively. A FrequencyResponse object is returned, with a nanosecond timestamp, a running sum of the number of samples processed by the RTA since it was last started or restarted, a smoothing setting, a start frequency, a points-per-octave figure (for fractional octave RTA captures) or a frequency step value (for spectrum captures), and a Base64-encoded string of response magnitudes generated from the raw bytes of 32-bit float magnitude values at each frequency. The default unit for the magnitude data is SPL but other units can be requested by including a unit query value in the url, e.g. ?unit=dBFS. The list of units available can be read from /rta/captured-data/units. Rather than polling with GET a [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified whenever the RTA captured or captured peak data are updated. The subscription parameters can contain the required unit, for example:

{
  "url": "http://127.0.0.1:5374/captured",
  "parameters": {unit: "dBFS"}
}            

When multiple inputs are being captured the parameters can contain an input index between 1 and the number of inputs, e.g index: 2. If there is no input index the rms average of the inputs is returned.

The current [RTA input distortion](https://www.roomeqwizard.com/help/help_en-GB/html/api.html) results can be read from the /rta/distortion endpoint, that returns a list of RTADistortion structures. The list has one RTADistortion entry unless stereo inputs are being captured, when there are two. The data has a nanosecond timestamp and a running sum of the number of samples processed by the RTA since it was last started or restarted. The default unit for the level values is SPL but other units can be requested by including a unit query value in the url, e.g. ?unit=dBFS. The list of units available can be read from /rta/distortion/units. The default unit for the relative distortion values is dB but percent can be requested by including a distortion query value in the url, e.g. ?distortion=percent. The list of relative distortion units available can be read from /rta/distortion/relative-units. Rather than polling with GET a [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified whenever the RTA distortion results are updated. The subscription parameters can contain the required units, for example:

{
  "url": "http://127.0.0.1:5374/distortion",
  "parameters": {unit: dBFS, distortion: percent}
}            

### [Stepped measurement](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /stepped-measurement endpoint provides control of REW's [Stepped measurement](https://www.roomeqwizard.com/help/help_en-GB/html/spectrum.html#steppedsine) features.

A GET at the /stepped-measurement/types endpoint returns the list of measurement types. A GET at the /stepped-measurement/type endpoint returns the currently selected type, to select a type POST it to the /stepped-measurement/type endpoint.

A GET at the /stepped-measurement/frequency-span endpoint returns the current start frequency (Hz), end frequency (Hz) and PPO step for a measurement vs frequency as a SteppedFreqSpan object. To change the span POST a SteppedFreqSpan object to the /stepped-measurement/frequency-span endpoint. The list of accepted PPO values can be read from /stepped-measurement/ppo-values.

A GET at the /stepped-measurement/level-span endpoint returns the current start level (dBFS), end level (dBFS) and level step (dB) for a measurement vs level as a SteppedLevelSpan object. To change the span POST a SteppedLevelSpan object to the /stepped-measurement/level-span endpoint.

A GET at the /stepped-measurement/fft-configuration endpoint returns the current FFT configuration for stepped measurements. To change the configuration POST a SteppedFFTConfiguration object to the /stepped-measurement/fft-configuration endpoint.

A GET at the /stepped-measurement/options endpoint returns the current option settings for stepped measurements. To change the options POST a SteppedOptions object to the /stepped-measurement/options endpoint. Other RTA-related options such as distortion HP or LP should be configured through the /rta endpoint.

A GET at the /stepped-measurement/commands endpoint returns the list of commands, to issue a command POST it to the /stepped-measurement/command endpoint. The Start command requires a settlingTimems parameter and either a leveldBFS, frequencyHz or imdStimulus parameter depending on the type of measurement. Here is an example of starting a THD vs frequency measurement:

{
  "command": "start",
  "parameters": {
    "settlingTimems": 0,
    "leveldBFS": -1.0
  }
}

The progress of a stepped measurement can be read from the /stepped-measurement/progress endpoint. That returns a SteppedProgress object, like the example below

{
  "point": 5,
  "points": 31,
  "message": "5/31, approx 1m 8s remaining",
  "timeRemainingSeconds": 68
}

Rather than polling for progress, a [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified of progress updates. There are no parameters for progress subscriptions.

A [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified of the distortion results for each point as they are generated. That is done by making a POST to the /stepped-measurement/results/subscribe endpoint. The results are returned as RTADistortion objects, see the [RTA section](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#rtadistortion) for the associated parameters. For example, to have updates posted to a /stepped-results endpoint a subscription could be:

{
  "url": "http://127.0.0.1:5374/stepped-results",
  "parameters": {unit: dBFS, distortion: percent}
}

### [Import](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /import endpoint provides access to import functionality.

Importing can take some time, a [subscription](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#subscriptions) can be added to be notified of import completion. There are no parameters for import subscriptions. Alternatively the [blocking](https://www.roomeqwizard.com/help/help_en-GB/html/api.html#blocking) mode can be used, in which case the API will not respond until the import has completed.

#### [Import frequency response](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /import/frequency-response endpoint allows the path to a text frequency response file to be set via a FilePath object. Note that backslashes in file paths must be escaped (meaning a double backslash is required), or forward slashes may be used. FilePath has a string for the path to the response file and an optional string for the channels that should be read from the file, not used for frequency response files. When the file is loaded it will generate a new measurement, that can be monitored by subscribing to the /measurements endpoint. The import may take some time. An import completed message will be posted to subscribers when an import has finished. A GET at the /import/frequency-response endpoint will return the path of the last file that finished importing. Any back slash in the path will be replaced by forward slash. An internal queue allows multiple imports to be requested without waiting for each to finish, up to 9 imports can be pending.

#### [Import impulse response](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /import/impulse-response endpoint allows the path to an impulse response file to be set via a FilePath object. Note that backslashes in file paths must be escaped (meaning a double backslash is required), or forward slashes may be used. FilePath has a string for the path to the response file and an optional string for the channels that should be read from the file if it has more than one channel. If the channels string is omitted or set to "All" all of the channels will be loaded, otherwise the specified channels will be loaded. Channels are numbered from 1 and channels to be loaded may be specified individually separated by commas or as a range separated by a dash, for example "1, 3, 5" or "2-4" or "1-3, 5, 7". As channels of data are loaded they will generate new measurements, that can be monitored by subscribing to the /measurements endpoint. The import may take some time. An import completed message will be posted to subscribers when an import has finished. A GET at the /import/impulse-response endpoint will return the path of the last file that finished importing. Any back slash in the path will be replaced by forward slash. An internal queue allows multiple imports to be requested without waiting for each to finish, up to 9 imports can be pending.

#### [Import frequency response data](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /import/frequency-response-data endpoint allows a frequency response to be set via a FrequencyResponseData object which contains the data as Base64-encoded strings generated from arrays of 32-bit float values. The FrequencyResponseData object has fields for an identifier, which is used as the name of the resulting measurement; a boolean to indicate whether the data is impedance (ohms) or SPL; a start frequency; the number of points per octave if the data is log spaced or the frequency step if it is linearly spaced; a Base64-encoded string for the magnitude values (ohms or dB SPL) and an optional Base64-encoded string for the corresponding phase values in degrees. The import may take some time. An import completed message will be posted to subscribers when an import has finished. A GET at the /import/frequency-response-data endpoint will return the ID of the last data that finished importing. An internal queue allows multiple imports to be requested without waiting for each to finish, up to 9 imports can be pending. Here is an example, omitting the base 64 data for brevity:

{
  "identifier": "my import",
  "isImpedance": false,
  "startFreq": 20,
  "ppo": 48,
  "magnitude": "..."
}

#### [Import impulse response data](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /import/impulse-response-data endpoint allows an impulse response to be set via an ImpulseResponseData object which contains the data as a Base64-encoded string generated from an array of 32-bit float values. The ImpulseResponseData object has fields for an identifier, which is used as the name of the resulting measurement; a start time for the data; the sample rate; the SPL offset (the dB value to add to the data to obtain SPL) and a boolean to indicate whether the calibration files for the current measurement input should be applied. The import may take some time. An import completed message will be posted to subscribers when an import has finished. A GET at the /import/impulse-response-data endpoint will return the ID of the last data that finished importing. An internal queue allows multiple imports to be requested without waiting for each to finish, up to 9 imports can be pending. Here is an example, omitting the base 64 data for brevity:

{
  "identifier": "my import",
  "startTime": -1,
  "sampleRate": 48000,
  "splOffset": 0,
  "applyCal": false,
  "data": "..."
}

#### [Import RTA file](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /import/rta-file endpoint allows the path to a file for the RTA to process to be set via an RTAFilePath object. Note that backslashes in file paths must be escaped (meaning a double backslash is required), or forward slashes may be used. FilePath has a string for the path to the response file and an integer for the channel that should be read from the file. A string specifies the save option, whether the save the current, peak or both current and peak RTA results. Completion of RTA file import will generate a new measurement, that can be monitored by subscribing to the /measurements endpoint.

RTA file import may take some time. Import progress and an import completed message will be posted to subscribers. The percentage completion can be read from the /import/rta-file/progress endpoint. A GET at the /import/rta-file endpoint will return the path of the last file that finished importing. Any back slash in the path will be replaced by forward slash. An internal queue allows multiple imports to be requested without waiting for each to finish, up to 9 imports can be pending.

#### [Import sweep recordings](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /import/sweep-recordings/stimulus endpoint allows the path to the sweep stimulus file to be read or set. If the file is set successfully the response will contain a summary of the stimulus parameters. If the path has not been set reading the endpoint will return an empty string, otherwise it will return the file path. Note that backslashes in file paths must be escaped (meaning a double backslash is required), or forward slashes may be used.

The /import/sweep-recordings/response endpoint allows the path to the sweep response file to be read or set via a FilePath object. If the path has not been set reading the endpoint will return an empty string, otherwise it will return the last file path set. Note that backslashes in file paths must be escaped (meaning a double backslash is required), or forward slashes may be used. FilePath has a string for the path to the response file and an optional string for the channels that should be read from the file if it has more than one channel. If the channels string is omitted or set to "All" all of the channels will be loaded, otherwise the specified channels will be loaded. Channels are numbered from 1 and channels to be loaded may be specified individually separated by commas or as a range separated by a dash, for example "1, 3, 5" or "2-4" or "1-3, 5, 7". As channels of data are loaded they will generate new measurements, that can be monitored by subscribing to the /measurements endpoint. The import may take some time. An import completed message will be posted to subscribers when an import has finished. An internal queue allows multiple imports to be requested without waiting for each to finish, up to 9 imports can be pending.

### [Room simulator](https://www.roomeqwizard.com/help/help_en-GB/html/api.html)

The /roomsim endpoint provides full control of REW's [room simulator](https://www.roomeqwizard.com/help/help_en-GB/html/modalsim.html). The /roomsim/room-size endpoint provides access to the room dimensions. The /roomsim/room-is-sealed endpoint provides access to whether the room should be treated as a sealed volume. The /roomsim/absorptions endpoint provides access to the room surface absorptions. The /roomsim/sources endpoint is used to retrieve or set the list of sources in the simulation. The list of recognised source names can be retrieved from the /roomsim/source-names endpoint.

The offsets to mic positions around the main position can be read and set at the /roomsim/mic-posn-offsets endpoint.

The calculation options for the simulator can be read and set at the /roomsim/options endpoint.

Each source can be queried and configured at paths below /roomsim/:src, where :src is one of the recognised source names. The source position in the room can be read or set at /roomsim/:src/position. The configuration of the source (its low frequency extension, enclosure type etc.) can be read or set at /roomsim/:src/configuration.

The frequency response for all sources summed can be read from /roomsim/frequency-response. The response for an individual source can be read from /roomsim/:src/frequency-response. The mic position for which the response is generated must be specified as a query parameter, e.g. ?micposition="Main".
