import argparse
import sys
import io

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
var_dict = {}  # Dictionary to store the variables
stmt_dict = {}  # Dictionary to store the statements
declare = "    double "
stmts = ""


def print_to_string(*args, **kwargs):
    output = io.StringIO()
    print(*args, file=output, **kwargs)
    contents = output.getvalue()
    output.close()
    return contents


def increase_counter():
    global counter
    counter += 1
    # print(counter)
    return counter


# This lambda calls the function which modifies the global variable.
lambda_counter = lambda: increase_counter()


def revar(var):
    global counter
    global var_dict
    global declare
    var_dict[var] = counter
    new_var = var + str(counter)
    counter += 1

    declare += new_var + ","
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
    global replaced
    global stmts
    # print(p[1] + " = " + p[3] + " " + p[4] + " " + p[5] + ";")
    op1 = p[3]
    op2 = p[5]
    e = p[4]
    var = p[1]
    if op1 not in var_dict:
        var_dict[op1] = lambda_counter()  # Know the current counter
        stmts += print_to_string("    double", op1 + str(var_dict[op1]), "=", op1 + ";")
    op1 += str(var_dict[op1])

    if op2 not in var_dict:
        var_dict[op2] = lambda_counter()
        stmts += print_to_string("    double", op2 + str(var_dict[op2]), "=", op2 + ";")
    op2 += str(var_dict[op2])

    # Assign each time the new number
    new_var = lambda_revar(var)
    new_expr = new_var + " = " + op1 + e + op2 + ";"
    # Check if the variable is already in the dictionary
    expr = op1 + e + op2
    expr1 = new_var + " = " + e + ";"
    expr2 = op2 + "+" + op1

    if expr in stmt_dict.keys():
        replaced += 1
        # print(new_var + " = " + stmt_dict[expr] + ";")
        stmt_dict[expr1] = stmt_dict[expr]
        new_expr = new_var + " = " + stmt_dict[expr] + ";"
    # elif e.__contains__("+") and stmt_dict.keys().__contains__(expr):
    elif e == "+" and expr2 in stmt_dict.keys():
        replaced += 1
        new_expr = new_var + " = " + stmt_dict[expr2] + ";"
    else:
        # print(expr1)
        stmt_dict[expr] = new_var
        # print(stmt_dict)
    stmts += print_to_string("   ", new_expr)

    return


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
    global declare
    global stmts
    # hint: perform the local value numbering optimization here on to_optimize
    # local variable
    print(pre)
    # hint: print out any new variable declarations you need here
    # hint: print out the optimized local block here
    # hint: store any new numbered variables back to their unumbered counterparts here
    parser.parse(to_optimize)
    print("    // Start declaration stmt\n"+declare[:-1] + ";\n\n    // Start assignment stmt")
    print(stmts+"    // Start Reassignment stmt\n")
    for key, value in var_dict.items():
        print("   ", key, "=", key + str(value) + ";")  # a = a5
    print(post)

    # You should keep track of how many instructions you replaced
    # print("// replaced: " , str(replaced))


# if you run this file, you can give it one of the python test cases
# in the test_cases/ directory.
# see solutions.py for what to expect for each test case.
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cppfile", help="The cpp file to be analyzed")
    args = parser.parse_args()
    local_value_numbering(args.cppfile)
