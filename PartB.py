from matplotlib import pyplot

import math
import numpy as np
import sympy as sym
import control as ctrl
import matplotlib.pyplot as plt


from LinearSystem import LinearSystem
from NonLinearSystem import NonLinearSystem


class PartB:
    """
    A static class to contain procedures that solve the problems described in part b of the coursework.
    """
    @staticmethod
    def system_plotter(solution):
        """
        Helper procedure to display the results from a simulation of a ball moving.
        :param solution: The solution for the movement of the ball as a solve_ivp object
        """
        fig, (ax1, ax2, ax3) = pyplot.subplots(1, 3)

        ax1.plot(solution.t, solution.y[0])
        ax1.grid()
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('$x_1$ (m)')

        ax2.plot(solution.t, solution.y[1])
        ax2.grid()
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('$x_2$ (m/s)')

        ax3.plot(solution.t, solution.y[2])
        ax3.grid()
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('I (A)')

        pyplot.show()

    @staticmethod
    def problem_b2():

        # Non Linear System
        non_linear_system = NonLinearSystem(0.46)

        non_linear_solution = non_linear_system.move(36.04, 100)
        PartB.system_plotter(non_linear_solution)

        # Linear System
        linear_system = LinearSystem(0.46)

        linear_solution = linear_system.move(36.04, 100)
        PartB.system_plotter(linear_solution)

    @staticmethod
    def problem_b3():
        m_val = 0.425  # mass
        g_val = 9.81  # acceleration due to gravity
        d_val = 0.42  # natural length of spring
        delta_val = 0.65  # x(max) - distance to electromagnet
        r_val = 0.125  # ball radius
        R_val = 53  # resistance of electromagnet
        L0_val = 0.12  # inductance
        L1_val = 0.025  # positive constant
        alpha_val = 1.2  # positive constant
        c_val = 6.815
        k_val = 1880  # spring
        b_damper_val = 10.4  # damper
        phi_val = np.deg2rad(42)  # 90 - angle of slope
        slope_val = np.deg2rad(48)  # angle of slope

        m, g, d, delta, r, R, L0, L1, a, c, k, b_damper, b, phi, x1, x2, x3, V = \
            sym.symbols('m, g, d, delta, r, R, L0, L1, a, c, k, b_damper, b, phi, x1, x2, x3, V', real=True,
                        positive=True)

        # Equations Used

        x_min = d + (m * g * (math.sin(np.deg2rad(48)))) / k
        x_max = delta
        x_min_val = x_min.subs([(d, d_val), (m, m_val), (g, g_val), (phi, phi_val), (k, k_val)])
        x_max_val = x_max.subs([(delta, delta_val)])
        x = (0.75 * x_min_val) + (0.25 * x_max_val)
        print("X: " + str(x))

        I = sym.sqrt(
            (((m_val * g_val * math.sin(slope_val)) - (k_val * (x - d_val))) / (-c_val)) * (delta_val - x) ** 2)
        print("I: " + str(I))

        a_equation = ((10 * c_val * I) / (3 * m_val * ((delta_val - x) ** 2)))
        b_equation = ((10 * c_val * I ** 2) / (3 * m_val * ((delta_val - x) ** 3))) - ((5 * k_val) / (3 * m_val))
        c_equation = (5 * b_damper_val) / (3 * m_val)

        a_equation_value = float(a_equation.subs([(c, c_val), (m, m_val)]))
        b_equation_value = float(b_equation.subs([(k, k_val), (m, m_val)]))

        f_equation = float(L0_val + (L1_val * math.exp(-alpha_val * (d_val - x))))

        transfer_function = ctrl.TransferFunction([a_equation_value], [f_equation,
                                                                       ((c_equation * f_equation) + R_val),
                                                                       ((-b_equation_value * f_equation) + (
                                                                                   c_equation * R_val)),
                                                                       (-b_equation_value * R_val)])

        t_final = 1
        sampling_rate = 2000
        sampling_time = 1 / sampling_rate
        n_points = t_final * sampling_rate
        t_span = np.linspace(0, t_final, n_points)

        t_imp, x1_imp = ctrl.impulse_response(transfer_function, t_span)
        t_step, x1_step = ctrl.step_response(transfer_function, t_span)

        plt.plot(t_imp, x1_imp, 'r', label='Impulse Response')
        plt.plot(t_step, x1_step, 'b', label='Step Response')
        plt.xlabel("Time (s)")
        plt.ylabel("Response (m)")
        plt.grid()
        plt.legend()
        plt.show()

    @staticmethod
    def problem_b4():
        m_val = 0.425  # mass
        g_val = 9.81  # acceleration due to gravity
        d_val = 0.42  # natural length of spring
        delta_val = 0.65  # x(max) - distance to electromagnet
        r_val = 0.125  # ball radius
        R_val = 53  # resistance of electromagnet
        L0_val = 0.12  # inductance
        L1_val = 0.025  # positive constant
        alpha_val = 1.2  # positive constant
        c_val = 6.815
        k_val = 1880  # spring
        b_damper_val = 10.4  # damper
        phi_val = np.deg2rad(42)  # 90 - angle of slope
        slope_val = np.deg2rad(48)  # angle of slope

        m, g, d, delta, r, R, L0, L1, a, c, k, b_damper, b, phi, x1, x2, x3, V = \
            sym.symbols('m, g, d, delta, r, R, L0, L1, a, c, k, b_damper, b, phi, x1, x2, x3, V', real=True,
                        positive=True)

        # Equations Used

        x_min = d + (m * g * (math.sin(np.deg2rad(48)))) / k
        x_max = delta
        x_min_val = x_min.subs([(d, d_val), (m, m_val), (g, g_val), (phi, phi_val), (k, k_val)])
        x_max_val = x_max.subs([(delta, delta_val)])
        x = (0.75 * x_min_val) + (0.25 * x_max_val)
        print("X: " + str(x))

        I = sym.sqrt(
            (((m_val * g_val * math.sin(slope_val)) - (k_val * (x - d_val))) / (-c_val)) * (delta_val - x) ** 2)
        print("I: " + str(I))

        a_equation = ((10 * c_val * I) / (3 * m_val * ((delta_val - x) ** 2)))
        b_equation = ((10 * c_val * I ** 2) / (3 * m_val * ((delta_val - x) ** 3))) - ((5 * k_val) / (3 * m_val))
        c_equation = (5 * b_damper_val) / (3 * m_val)

        a_equation_value = float(a_equation.subs([(c, c_val), (m, m_val)]))
        b_equation_value = float(b_equation.subs([(k, k_val), (m, m_val)]))

        f_equation = float(L0_val + (L1_val * math.exp(-alpha_val * (d_val - x))))

        transfer_function = ctrl.TransferFunction([a_equation_value], [f_equation,
                                                                       ((c_equation * f_equation) + R_val),
                                                                       ((-b_equation_value * f_equation) + (
                                                                                   c_equation * R_val)),
                                                                       (-b_equation_value * R_val)])

        t_final = 1
        sampling_rate = 2000
        sampling_time = 1 / sampling_rate
        n_points = t_final * sampling_rate
        t_span = np.linspace(0, t_final, n_points)

        t_imp, x1_imp = ctrl.impulse_response(transfer_function, t_span)
        t_step, x1_step = ctrl.step_response(transfer_function, t_span)

        mag, phase, omega = ctrl.bode(transfer_function)

        plt.show()

    @staticmethod
    def problem_b6():
        m_val = 0.425  # mass
        g_val = 9.81  # acceleration due to gravity
        d_val = 0.42  # natural length of spring
        delta_val = 0.65  # x(max) - distance to electromagnet
        r_val = 0.125  # ball radius
        R_val = 53  # resistance of electromagnet
        L0_val = 0.12  # inductance
        L1_val = 0.025  # positive constant
        alpha_val = 1.2  # positive constant
        c_val = 6.815
        k_val = 1880  # spring
        b_damper_val = 10.4  # damper
        phi_val = np.deg2rad(42)  # 90 - angle of slope
        slope_val = np.deg2rad(48)  # angle of slope

        m, g, d, delta, r, R, L0, L1, a, c, k, b_damper, b, phi, x1, x2, x3, V = \
            sym.symbols('m, g, d, delta, r, R, L0, L1, a, c, k, b_damper, b, phi, x1, x2, x3, V', real=True,
                        positive=True)

        # Equations Used

        x_min = d + (m * g * (math.sin(np.deg2rad(48)))) / k
        x_max = delta
        x_min_val = x_min.subs([(d, d_val), (m, m_val), (g, g_val), (phi, phi_val), (k, k_val)])
        x_max_val = x_max.subs([(delta, delta_val)])
        x = (0.75 * x_min_val) + (0.25 * x_max_val)
        print("X: " + str(x))

        I = sym.sqrt(
            (((m_val * g_val * math.sin(slope_val)) - (k_val * (x - d_val))) / (-c_val)) * (delta_val - x) ** 2)
        print("I: " + str(I))

        a_equation = ((10 * c_val * I) / (3 * m_val * ((delta_val - x) ** 2)))
        b_equation = ((10 * c_val * I ** 2) / (3 * m_val * ((delta_val - x) ** 3))) - ((5 * k_val) / (3 * m_val))
        c_equation = (5 * b_damper_val) / (3 * m_val)

        a_equation_value = float(a_equation.subs([(c, c_val), (m, m_val)]))
        b_equation_value = float(b_equation.subs([(k, k_val), (m, m_val)]))

        f_equation = float(L0_val + (L1_val * math.exp(-alpha_val * (d_val - x))))

        transfer_function = ctrl.TransferFunction([a_equation_value], [f_equation,
                                                                       ((c_equation * f_equation) + R_val),
                                                                       ((-b_equation_value * f_equation) + (
                                                                                   c_equation * R_val)),
                                                                       (-b_equation_value * R_val)])

        t_final = 1
        num_points = 5000

        def pid(Kp, Ki, Kd):
            Gc = ctrl.TransferFunction([Kp], [1])
            Gc += ctrl.TransferFunction([Kd, 0], [1])
            Gc += ctrl.TransferFunction([Ki], [1, 0])
            return Gc

        transfer_function_pid_impulse = pid(Kp=100, Ki=0.1, Kd=4)
        transfer_function_pid_step = pid(Kp=700, Ki=0.3, Kd=10)
        impulse_tf = ctrl.feedback(transfer_function, transfer_function_pid_impulse)
        step_tf = ctrl.feedback(transfer_function, transfer_function_pid_impulse)
        t_imp, x_imp = ctrl.impulse_response(impulse_tf, T=np.linspace(0, t_final, num_points))
        t_step, x_step = ctrl.step_response(step_tf, T=np.linspace(0, t_final, num_points))

        # plt.plot(t_imp, x_imp, 'r', label='Impulse Response')
        plt.plot(t_step, x_step, 'b', label='Step Response')
        plt.xlabel("Time (s)")
        plt.ylabel("Distance (m)")
        plt.grid()
        plt.legend()
        plt.show()


if __name__ == '__main__':
    # PartB.problem_b2()
    PartB.problem_b3()
    PartB.problem_b4()
    PartB.problem_b6()
