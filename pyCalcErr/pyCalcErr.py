from __future__ import absolute_import

from pyCalcErr.ParseCmdArgs import ParseCmdArgs
from pyCalcErr.GaussPropagation import GaussPropagation
from pyCalcErr.EquationHandler import EquationHandler


def main():
    parser = ParseCmdArgs()
    gp = GaussPropagation()
    eh = EquationHandler()
    base_var, equation, err_var = parser.get_args()
    error_eq = gp.propagate_error(base_var, equation, err_var)
    needed_values = eh.extract_variables(error_eq, equation)
    print(needed_values)
    value_dic = parser.accept_user_input(needed_values)
    eh.define_vars(value_dic)
    result = eh.evaluate_equation(equation)
    error_result = eh.evaluate_equation(error_eq)
    error_eq_latex = gp.get_latex_equation(error_eq)
    eq_latex = gp.get_latex_equation(base_var + " = " + equation)
    print(equation + ' = {}'.format(result))
    print(eq_latex)
    print(error_eq + ' = {}'.format(error_result))
    print(error_eq_latex)
    del parser, gp, eh

"""
run script from another python script

>>> run("Epot", "1/2*k*x**2", "x", {'x': 2, 's_x': 2, 'k': 2})
0
"""
def run(base_var, equation, err_var, value_dic):
    parser = ParseCmdArgs()
    gp = GaussPropagation()
    eh = EquationHandler()
    error_eq = gp.propagate_error(base_var, equation, err_var)
    eh.define_vars(value_dic)
    result = eh.evaluate_equation(equation)
    error_result = eh.evaluate_equation(error_eq)
    error_eq_latex = gp.get_latex_equation(error_eq)
    eq_latex = gp.get_latex_equation(base_var + " = " + equation)
    res1 = equation + ' = {}'.format(result)
    res2 = error_eq + ' = {}'.format(error_result)
    res = [res1, eq_latex, res2, error_eq_latex]
    return result
    del parser, gp, eh


if __name__ == "__main__":
    main()
