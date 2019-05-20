from ParseCmdArgs import ParseCmdArgs
from GaussPropagation import GaussPropagation
from EquationHandler import EquationHandler

if __name__ == "__main__":
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
