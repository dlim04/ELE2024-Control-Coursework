class Electromagnet:
    """
    Class to define the electromagnet object which is used as a struct to store the instance variables for the
    electromagnet.
    """
    def __init__(self, nominal_inductance=120, inductance1=25, inductance_constant=1.2, resistance=53,
                 magnetic_constant=6.815):
        """
        Constructor for the Electromagnet object.
        :param nominal_inductance: (L_0) The nominal inductance of the inductor in millihenries as an integer
        :param inductance1: (L_1) The second component of the inductance of the inductor in millihenries as an integer
        :param inductance_constant: (alpha) The inductance constant as a float
        :param resistance: (R) The resistance of the electromagnet in ohms as an integer
        :param magnetic_constant: (c) The magnetic constant in ((kg m^3)/(A^2 s^2)) as an integer
        """
        self.nominal_inductance = nominal_inductance
        self.inductance1 = inductance1
        self.inductance_constant = inductance_constant
        self.resistance = resistance
        self.magnetic_constant = magnetic_constant
