# BMS Emulator
BMS emulator that mimics the battery pack and BMS firmware

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

## Battery Pack

## BMS logic

## Simulation and Logging
