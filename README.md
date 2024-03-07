# WXProc

Simple Python library for processing data from [AMMETS SSWA Weather Sensors](https://github.com/aidanbxyz/WXLogs)

[![DOI](https://zenodo.org/badge/768431185.svg)](https://zenodo.org/doi/10.5281/zenodo.10791452)

## Setup

Move the sswa.py file into your project's directory or your working directory and `import sswa`

## Usage

### `sswa.parse`

#### `sswa.parse.rabbit1`

Takes a Rabbit I log file and cleans it up.

Importing data:
```
import sswa
rlog = sswa.parse.rabbit1("2023-08-12_002941-013845.log")
...
```
and using it:
```
...
print("Log (warn+):")
for line in rlog.log:
  if line[0] > 0: print(str(line[0]) + ": " + line[1])
print()
print("Last 5 packets:")
for line in rlog.stream[-5:]:
  print(line)
print()
print("Sensor located at " + str(rlog.location[-1][0]) + "," + str(rlog.location[-1][1]) + " as of " + str(rlog.time[-1][0]) + ":" + str(rlog.time[-1][1]) + ":" + str(rlog.time[-1][2]) + " UTC")
print(str(rlog.temperature[-1]) + "C " + str(rlog.humidity[-1]) + "% " + str(rlog.pressure[-1]/100) + "hPa")
```
