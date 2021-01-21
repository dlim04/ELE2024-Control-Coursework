from math import exp, sqrt, sin

from System import System


class LinearSystem(System):
    """
    Class to define the LinearSystem object which will be the target of the model.
    """
    def _system_dynamics(self, t, z, voltage):
        x_equilibrium = (0.75 * (self.delta + ((self.ball.mass * self.gravitational_acceleration * sin(
            self.plane_angle)) / self.spring.stiffness))) + (0.25 * self.delta)
        I_equilibrium = sqrt((((self.ball.mass * self.gravitational_acceleration * sin(self.plane_angle)) - (
            self.spring.stiffness * (x_equilibrium - self.d))) / (-self.electromagnet.magnetic_constant)) * (
                                         self.delta - x_equilibrium) ** 2.0)
        voltage_equilibrium = I_equilibrium * self.electromagnet.resistance

        x1 = z[0]
        x2 = z[1]
        I = z[2]

        a_equation = ((10 * self.electromagnet.magnetic_constant * I_equilibrium) / (
                    3 * self.ball.mass * ((self.delta - x_equilibrium) ** 2)))
        b_equation = ((10 * self.electromagnet.magnetic_constant * I_equilibrium ** 2) / (
                    3 * self.ball.mass * ((self.delta - x_equilibrium) ** 3))) - (
                                 (5 * self.spring.stiffness) / (3 * self.ball.mass))
        c_equation = (5 * self.spring.damping_coefficient) / (3 * self.ball.mass)

        return [x2,
                (a_equation*(I - I_equilibrium)) + (b_equation*(x1-x_equilibrium)) - (c_equation*x2),
                ((voltage - voltage_equilibrium) - (I - I_equilibrium) * self.electromagnet.resistance) / (
                            self.electromagnet.nominal_inductance + (self.electromagnet.inductance1 * exp(
                        -self.electromagnet.inductance_constant * (self.d - x1))))]
