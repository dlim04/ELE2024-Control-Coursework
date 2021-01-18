class Spring:
    """
    Class to define the spring object which is used as a struct to store the instance variables for the spring and
    damper.
    """
    def __init__(self, stiffness=1880, damping_coefficient=10.4):
        """
         Constructor for the Spring object.
        :param stiffness: (k) The stiffness of the spring in N/m as an integer
        :param damping_coefficient: (b) the damping coefficient of the damper in Ns/m as a float
        """
        self.stiffness = stiffness
        self.damping_coefficient = damping_coefficient
