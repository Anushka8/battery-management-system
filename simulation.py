import time
from battery.pack import BatteryPack
from bms.logic import BMSLogic
import matplotlib.pyplot as plt

def main():
    dt = 30  # seconds
    sim_time = 150  # seconds
    current = 10  # discharge current (A)

    pack = BatteryPack(n_cells=4)
    bms = BMSLogic()

    # Storage lists
    time_log = []
    voltage_log = []  # average or per-cell
    soc_log = []

    t = 0
    while t < sim_time:
        pack.update(current, dt)

        voltages = pack.get_cell_voltage()
        rounded_voltages = [round(float(volt), 3) for volt in voltages]

        fault = bms.check_faults(voltages)

        soc = pack.get_cell_soc()
        rounded_soc = [round(float(charge), 2) * 100 for charge in soc]
        
        print(f"t={t:.1f}s | Voltages: {rounded_voltages} V | Fault: {fault} | SoC: {rounded_soc}")

        # Log data at each timestep
        time_log.append(t)
        voltage_log.append(sum(rounded_voltages) / len(rounded_voltages))  # average across cells
        soc_log.append(sum(rounded_soc) / len(rounded_soc))                # average across cells

        time.sleep(dt)
        t += dt

    # Plot
    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(time_log, voltage_log, color='royalblue', linewidth=2, label='Avg Cell Voltage (V)')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Voltage (V)', color='royalblue')
    ax1.tick_params(axis='y', labelcolor='royalblue')

    ax2 = ax1.twinx()  # second y-axis for SoC
    ax2.plot(time_log, soc_log, color='tomato', linewidth=2, label='Avg SoC (%)')
    ax2.set_ylabel('State of Charge (%)', color='tomato')
    ax2.tick_params(axis='y', labelcolor='tomato')

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

    plt.title('Battery Cell Voltage and SoC Over Time')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
