from battery.cell import BatteryCell
import numpy as np

class BatteryPack:
    def __init__(self, n_cells):
        self.pack = [BatteryCell() for _ in range(n_cells)]

    def update(self, current, dt):
        for cell in self.pack:
            cell.update(current, dt)

    def get_pack_voltage(self):
        return sum(cell.voltage for cell in self.pack)

    def get_cell_voltage(self):
        return [cell.voltage for cell in self.pack]
    
    def get_cell_soc(self):
        return [cell.soc for cell in self.pack]
