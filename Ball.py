class Ball:
    """
    Class to define the ball object which stores the instance variables for the ball in the model.
    """
    def __init__(self, mass=425, radius=12.5):
        """
        Constructor for the ball object.
        :param mass: (m) The mass of the ball in grams as an integer
        :param radius: (r) The radius of the ball in centimeters as a float
        """
        self.mass = mass
        self.radius = radius
