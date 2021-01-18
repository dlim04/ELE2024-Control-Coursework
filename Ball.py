class Ball:
    """
    Class to define the ball object which stores the instance variables for the ball in the model.
    """
    def __init__(self, mass=0.425, radius=0.125):
        """
        Constructor for the ball object.
        :param mass: (m) The mass of the ball in kilograms as a float
        :param radius: (r) The radius of the ball in meters as a float
        """
        self.mass = mass
        self.radius = radius
