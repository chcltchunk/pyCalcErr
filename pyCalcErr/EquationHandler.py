import re


class EquationHandler():
    """
    extract needed variables from equation string

    >>> eh = EquationHandler()

    >>> eh.extract_variables("s_V + D_e",
    ...                      "V = D_e*(1-exp(-alpha*(r-r_e)))**2")
    ['D_e', 'alpha', 'r', 'r_e', 's_V']

    # >>> eh.evaluate_equation("D_e*(1-e**(-alpha*(r-r_e)))**2", var_defs)
    >>> eh.define_vars({'a' : 3.4, 'b' : 2.6})
    >>> eh.evaluate_equation("a + b")
    6.0
    >>> round(eh.evaluate_equation("log(a) + sqrt(b)"), 2)
    2.84
    """
    def pre_process_equation():
        # TODO
        """
        ln -> log
        logN -> log/log(N)
        ^ -> **
        e** -> exp
        ...
        """
        return 0

    def extract_variables(self, error_eq, equation):
        equation = re.split(".*=", equation)[-1]
        error_eq = re.split(".*=", error_eq)[-1]
        regex = """[-*/()+0-9 ]+|ln|log|exp|ceil|copysign|fabs|factorial|floor
        |fmod|frexp|fsum|isfinite|isinf|isnan|ldexp|modf|trunc|exp|expm1|log
        |log1p|log2|log10|pow|sqrt|acos|asin|atan|atan2|cos|hypot|sin|tan
        |degrees|radians|acosh|asinh|atanh|cosh|sinh|tanh|erf|erfc|gamma
        |lgamma|pi"""
        variables = list(set(filter(None, re.split(regex,
                                    error_eq + ' ' + equation))))
        return sorted(variables)

    def define_vars(self, definitions):
        self.definitions = definitions

    def evaluate_equation(self, equation):
        result = "operation not defined, try again"
        equation = re.split(".*=", equation)[-1]
        for var, val in self.definitions.items():
            exec(var + ' = val')
        while True:
            try:
                result = eval(equation)
                break
            except Exception as e:
                try:
                    missing_import = re.search("'.*'",
                                               str(e)).group(0).split("'")[1]
                    exec("from math import {}".format(missing_import))
                    continue
                except AttributeError:
                    break
                break
        return result
