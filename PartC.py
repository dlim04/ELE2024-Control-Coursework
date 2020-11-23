import sympy.core
import sympy.functions
import sympy.integrals
import sympy.printing


class PartC:
    """
    A static class to contain procedures that solve the mathematical problems described in part c of the coursework.
    """
    @staticmethod
    def problem_c1():
        """
        A procedure to calculate the solution to problem c1.
        """
        s, t = sympy.symbols('s, t')

        f = sympy.ln(t**3)
        f_laplace = sympy.laplace_transform(f, t, s)
        sympy.pprint(f_laplace)
        print(sympy.latex(f_laplace))

    @staticmethod
    def problem_c2():
        """
        A procedure to calculate the solution to problem c2.
        """
        omega, t = sympy.symbols('omega t')

        f = sympy.Abs(sympy.cos(omega))
        f_laplace = sympy.laplace_transform(f, t, omega)
        # f_laplace.pprint(f_laplace)  # This will not work as omega is not printable.
        # # Change the sympy symbol in line 27 for pretty print.
        print(sympy.latex(f_laplace))


if __name__ == '__main__':
    PartC.problem_c1()
    PartC.problem_c2()
