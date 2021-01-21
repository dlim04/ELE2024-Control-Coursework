from abc import ABC, abstractmethod
from math import radians

from numpy import linspace
from scipy.integrate import solve_ivp

from Ball import Ball
from Electromagnet import Electromagnet
from Spring import Spring


class System(ABC):
    def __init__(self, x, d=0.42, delta=0.65, plane_angle=radians(42), gravitational_acceleration=9.81, ball=Ball(),
                 electromagnet=Electromagnet(), spring=Spring()):
        """
        Constructor for class NonLinearSystem.
        :param x: (x) The distance of the centre of the ball from the wall in meters as a float
        :param d: (d) The natural length of the spring where no restoring force is applied in meters as a float
        :param delta: (delta) The distance of the centre of the electromagnet from the wall in meters as a float
        :param plane_angle: (phi) The angle of the plane that the ball is placed on in radians as a float
        :param gravitational_acceleration: (g) The acceleration due to gravity in m/s^2 as a float
        :param ball: The ball object that stores all the instance data for the ball
        :param electromagnet: The electromagnet object that stores all the instance data for the electromagnet
        :param spring: The spring object that stores all the instance data for the spring and damper
        """
        self.x = x
        self.d = d
        self.delta = delta
        self.plane_angle = plane_angle
        self.gravitational_acceleration = gravitational_acceleration
        self.ball = ball
        self.electromagnet = electromagnet
        self.spring = spring

        self.x1 = x
        self.x2 = 0
        self.I = 0

    def move(self, voltage, dt):
        """
        Public method to find the velocity of the ball in the x plane with respect to time.
        :param voltage: The voltage being applied across the electromagnet in volts as a float
        :param dt: The time the move takes place over as a float in seconds
        :return: The solution for the movement as a solve_ivp object
        """
        z_initial = [self.x1,
                     self.x2,
                     self.I]

        number_of_points = 100
        solution = solve_ivp(self._system_dynamics, [0, dt], z_initial, args=[voltage],
                             t_eval=linspace(0, dt, number_of_points))

        self.x1 = solution.y[0][-1]
        self.x2 = solution.y[1][-1]
        self.I = solution.y[2][-1]

        return solution

    @abstractmethod
    def _system_dynamics(self, t, z, voltage):
        """
        Private helper method to be used by move to describe the system of the car at a point in time.
        :param t: An array where the first element is the start time and the second element is the end time as floats
        :param z: An array containing the state space of the system
        :param voltage: The voltage being applied across the electromagnet in volts as a float
        :return: A new state space based on the previous state space and the voltage applied to the electromagnet
        """
        pass
