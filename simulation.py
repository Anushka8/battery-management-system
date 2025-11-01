import time
from battery.pack import BatteryPack
from bms.logic import BMSLogic

def main():
    dt = 0.1  # seconds
    sim_time = 10  # seconds
    current = 1.0  # discharge current (A)

    pack = BatteryPack(n_cells=4)
    bms = BMSLogic()

    t = 0
    while t < sim_time:
        pack.update(current, dt)
        voltages = pack.get_cell_voltage()
        fault = bms.check_faults(voltages)
        
        print(f"t={t:.1f}s | Voltages: {voltages} | Fault: {fault}")
        time.sleep(dt)
        t += dt

if __name__ == "__main__":
    main()
