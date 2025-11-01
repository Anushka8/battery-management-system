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

### Functions
- `ocv_from_soc`: Calculates open-circuit voltage using state-of-charge (SOC). Although the relationship between OCV and SOC is non-linear. For simplicity, we have considered this formula. The formula indicates a voltage range of 3.0 - 4.2 V indiciating it is. Li-ion battery.
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
