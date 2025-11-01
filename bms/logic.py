class BMSLogic:
    def __init__(self, v_min=3.0, v_max=4.2):
        self.v_min = v_min
        self.v_max = v_max
        self.fault = None

    def check_faults(self, cell_voltages):
        for i, v in enumerate(cell_voltages):
            if v > self.v_max:
                self.fault = f"Overvoltage on cell {i}"
            elif v < self.v_min:
                self.fault = f"Undervoltage on cell {i}"
        return self.fault
