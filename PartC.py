import sympy as sympy


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


if __name__ == '__main__':
    PartC.problem_c1()
