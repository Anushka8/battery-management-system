# BMS Emulator
BMS emulator that mimics the battery pack and BMS firmware

A Battery Management System monitors the SoC, SoH, internal and external temperatures to maintain a healthy battery and notify anomalies.
There are various methods to determine SoC and SoH that includes and not limited to the chemistry of the batter, electronics (voltage, current, internal resistence) and ML algorithms (Kalman Filter, classification to determine battery state, regression analysis, time-series analysis to predict future battery readings).

This emulator focuses on the basic physical logging for voltage, current, internal resistence. Using these features to calculate the SoC and SoH (primitive methods) and plotting the battery behavior over time.

## Project Structure
```bash
battery_management_system/
│
├── battery/
│   ├── cell.py          # Simulates one cell
│   ├── pack.py          # Combines multiple cells
│
├── bms/
│   ├── logic.py         # Fault detection, balancing
│   ├── soc.py           # SOC estimation algorithms
│
├── simulation.py        # Main control loop
├── config.py            # Parameters (cell count, dt, etc.)
├── logger.py            # File + console logging
└── requirements.txt     # (matplotlib, numpy, etc.)
```

## Battery Cell
### Overview
- Tracks the SOC (0-1) and computes open-circuit voltage (OCV) from the SOC.
- A typical Li-ion cell has a nominal capacity of 2.8-3.2 Ah so the default here is set to `capacity_ah = 3.0`

### Functions
- `ocv_from_soc`: Calculates open-circuit voltage using state-of-charge (SOC). The relationship between OCV and SOC is non-linear. For 
- `update`: Updates SOC using Coulomb counting and voltage using OCV and internal resistance

## Battery Pack
### Overview
- Creates pack using `n_cell` cells.

### Functions
- `update`: Updates cell voltage and SOC in the pack 
- `get_pack_voltage`: Returns the total pack voltage
- `get_cell_voltage`: Returns voltage for every cell in a list

## BMS logic
### Overview 
- Controller logic will have monitoring, fault detection, SOC estimation, balancing, logging.

## Simulation and Logging
- Simulate battery functioning and display logs

## References
[Battery Management System](https://www.integrasources.com/blog/battery-management-systems-software-development/)
