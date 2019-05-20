import sys


# parse command line arguments
class ParseCmdArgs:
    # return arguments
    def get_args(self):
        if len(sys.argv) < 4:
            print("Usage: pyCalcErr <equation left side>", end='')
            print("<equation_right_side> <deriveAfter_1,...>")
            # print("Usage: python pyCalcErr.py <equation left side>", end='')
            # print("Example: python pyCalcErr.py F 1/2*k*x**2 x") # obsolete
            print("Example: pyCalcErr E_pot 1/2*k*x**2 x")
            sys.exit(1)
        try:
            base_var = str(sys.argv[1])
            equation = str(sys.argv[2])
            error_variables = str(sys.argv[3]).split(",")
        except Exception as e:
            print(e, 'recheck your request')
            sys.exit(2)
        return base_var, equation, error_variables

    # accept user input to define several variables
    def accept_user_input(self, vars_to_define):
        var_definitions = {}
        print("Define the values and errors ", end='')
        print("of the following variables (float): ")
        for var in vars_to_define:
            input_var = input("{} = ".format(var))
            while True:
                try:
                    var_definitions[var] = float(input_var)
                    break
                except Exception as e:
                    print(e)
                    print("this is not a valid entry, ", end='')
                    print("please enter a float number")
                    pass
                input_var = input("{} = ".format(var))
        return var_definitions
