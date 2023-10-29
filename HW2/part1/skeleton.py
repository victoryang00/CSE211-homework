import argparse
import sys

sys.path.append("../../HW1/part1/")
import ply.lex as lex
import ply.yacc as yacc

tokens = ["OP", "VAR", "SEMI", "ASSIGN"]
t_SEMI = ";"
t_ASSIGN = "="
t_OP = r"\+ | \-"
t_VAR = r"[a-zA-Z_][a-zA-Z0-9_]*"
t_ignore = " "

# Global variable
counter = 0
replaced = 0
var_dict = {}


def increase_counter():
    global counter
    counter += 1
    return counter


# This lambda calls the function which modifies the global variable.
lambda_counter = lambda: increase_counter()


def revar(var):
    global counter
    global var_dict
    var_dict[var] = counter
    new_var = var + str(counter)
    counter += 1
    return new_var


# This lambda calls the function which modifies the global variable.
lambda_revar = lambda x: revar(x)


def t_NEWLINE(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    pass


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def p_error(p):
    print("Syntax error in input!")
    print(p)
    pass


lexer = lex.lex()


# STM_LIST -> STM STM_LIST | STM
# STM -> VAR ASSIGN VAR OP VAR SEMI
def p_stm_list(p):
    """STM_LIST : STM STM_LIST
    | STM"""
    pass


def p_stm(p):
    """STM : VAR ASSIGN VAR OP VAR SEMI"""
    global counter
    print(p[1] + " = " + p[3] + " " + p[4] + " " + p[5] + ";")
    op1 = p[3]
    op2 = p[5]
    var = p[1]
    if op1 not in var_dict:
        var_dict[op1] = lambda_counter()  # Know the current counter
        print("int " + var + " = " + op1 + var_dict[op1] + ";")
    op1 += str(var_dict[op1])
    if op2 not in var_dict:
        var_dict[op2] = lambda_counter()
        print("int " + var + " = " + op2 + var_dict[op2] + ";")
    op2 += str(var_dict[op2])

    # Assign each time the new number
    new_var = lambda_revar(var)

    expr = op1 + p[4] + op2
    expr1 = new
    # Check if the variable is already in the dictionary
    pass


def local_value_numbering(f):
    f = open(f)
    s = f.read()
    f.close()

    pre = s.split("// Start optimization range")[0]
    post = s.split("// Start optimization range")[1].split("// End optimization range")[
        1
    ]
    to_optimize = s.split("// Start optimization range")[1].split(
        "// End optimization range"
    )[0]
    lexer = lex.lex()
    parser = yacc.yacc()
    # init
    global replaced
    # hint: perform the local value numbering optimization here on to_optimize
    # local variable
    print(pre)

    parser.parse(to_optimize)
    # hint: print out any new variable declarations you need here
    # hint: print out the optimized local block here
    # hint: store any new numbered variables back to their unumbered counterparts here
    revar()
    print(post)

    # You should keep track of how many instructions you replaced
    print("// replaced: " + str(replaced))


# if you run this file, you can give it one of the python test cases
# in the test_cases/ directory.
# see solutions.py for what to expect for each test case.
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cppfile", help="The cpp file to be analyzed")
    args = parser.parse_args()
    local_value_numbering(args.cppfile)
