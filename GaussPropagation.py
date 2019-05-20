from sympy import diff
from pytexit import py2tex


class GaussPropagation:
    # formula = "D_e*(1-e**(-alpha*(r-r_e)))**2"
    """
    propagates error with respect to [error variables]

    >>> gp = GaussPropagation()
    >>> eq = "1/2*k*x**2"
    >>> ev = ['x']
    >>> gp.propagate_error("E_pot", eq, ev)
    's_E_pot = sqrt((k*x*s_x)**2)'

    print out equation as latex formula
    >>> gp.get_latex_equation("s_E_pot = sqrt((k*x*s_x)**2)")
    '$$s_{E,pot}=\\\\sqrt{\\\\left(k x s_x\\\\right)^2}$$'
    """
    def propagate_error(self, base_var, equation, error_variables):
        gauss_error = ""
        for i in error_variables:
            derivative = str(diff(equation, i))
            # print(derivative)
            if derivative == "0":
                continue
            if gauss_error == "":
                gauss_error += '(' + derivative + "*s_{})**2".format(i)
            else:
                gauss_error += '+ (' + derivative + "*s_{})**2".format(i)

        gauss_error = 's_{} = sqrt({})'.format(base_var, gauss_error)
        return gauss_error

    def get_latex_equation(self, equation_string):
        latex_string = py2tex(equation_string, print_latex=False,
                              print_formula=False)
        # print("{}".format(latex_string))
        return latex_string
