class Ball:
    """
    Class to define the ball object which stores the instance variables for the ball in the model.
    """
    def __init__(self, mass=425, radius=12.5):
        """
        Constructor for the ball object.
        :param mass: The mass of the ball in grams as an integer
        :param radius: The radius of the ball in centimeters as a float
        """
        self.mass = mass
        self.radius = radius

    def get_mass(self):
        """
        Getter for the mass of the ball.
        :return: The mass of the ball in grams as an integer
        """
        return self.mass

    def get_radius(self):
        """
        Getter for the radius of tha ball.
        :return: The radius of the ball in centimeters as a float
        """
        return self.radius
