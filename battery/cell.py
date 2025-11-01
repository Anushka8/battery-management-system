import numpy as np

class BatteryCell:
    def __init__(self, capacity_ah=3.0, r_int=0.05, soc_int=1.0):
        self.capacity = capacity_ah
        self.r_int = r_int
        self.soc = soc_int
        self.voltage = self.ocv_from_soc(self.soc)
        self.temperature=25.0

    def ocv_from_soc(self, soc):
        return 3.0 + 1.2 * soc
    
    def update(self, current, dt):
        # update SOC using Coulomb counting
        self.soc -= (current * dt) / (self.capacity * 3600)
        self.soc = np.clip(self.soc, 0, 1)
        
        # calculate terminal voltage with internal resistance (V = OCV - I*R)
        self.voltage = self.ocv_from_soc(self.soc) - current * self.r_int