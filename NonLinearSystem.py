from math import sin

from System import System


class NonLinearSystem(System):
    """
    Class to define the NonLinearSystem object which will be the target of the model.
    """
    def _system_dynamics(self, t, z, voltage):
        x1 = z[0]
        x2 = z[1]
        I = z[2]
        return [x2,
                (5 * (((self.electromagnet.magnetic_constant * I ** 2) / ((self.delta - self.x) ** 2)) + self.ball.mass * self.gravitational_acceleration * sin(self.plane_angle) - self.spring.stiffness * (self.x - self.d) - self.spring.damping_coefficient * x1)) / (3 * self.ball.mass),
                (voltage - (I * self.electromagnet.resistance)) / (
                            self.electromagnet.nominal_inductance + self.electromagnet.inductance1 ** (
                                -self.electromagnet.inductance_constant * (self.delta - self.x)))]
