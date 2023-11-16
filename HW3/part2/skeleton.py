import ast
import argparse
import z3
from typing import Tuple


# Some example functions on how to use the python ast module:
def pp_expr(node):
    if is_MULTIPLY_node(node):
        return ("(", pp_expr(node.left), "*", pp_expr(node.right), ")")
    elif is_ADDITION_node(node):
        return ("(", pp_expr(node.left), "+", pp_expr(node.right), ")")
    elif is_NAME_node(node):
        return node.id
    elif is_NUM_node(node):
        return str(node.n)


# Given a python file, return an AST using the python ast module.
def get_ast_from_file(fname):
    f = open(fname, "r")
    s = f.read()
    f.close()
    module_ast = ast.parse(s)
    body_ast = module_ast.body[0]
    return body_ast


# Example of how to get information for the ast FOR_node
def get_loop_constraints(FOR_node) -> Tuple[str, str, str]:
    loop_var = FOR_node.target.id
    lower_bound = pp_expr(FOR_node.iter.args[0])
    upper_bound = pp_expr(FOR_node.iter.args[1])
    print(
        "loop_var: ",
        loop_var,
        " lower_bound: ",
        lower_bound,
        " upper_bound: ",
        upper_bound,
    )
    # return the for loop information in some structure
    return (loop_var, lower_bound, upper_bound)


# Check if an ast node is a for loop
def is_FOR_node(node):
    return str(node.__class__) == "<class '_ast.For'>"


def is_NAME_node(node):
    return str(node.__class__) == "<class '_ast.Name'>"


def is_NUM_node(node):
    return str(node.__class__) == "<class '_ast.Constant'>"


def is_MULTIPLY_node(node):
    return str(node.op.__class__) == "<class '_ast.Mult'>"


def is_ADDITION_node(node):
    return str(node.op.__class__) == "<class '_ast.Add'>"


def is_READ_node(node):
    return node.value.func.id == "read_index"


def is_WRITE_node(node):
    return node.value.func.id == "write_index"


# Top level function. Given a python file name, it parses the file,
# and analyzes it to determine if the top level for loop can be done
# in parallel.
#
# It returns True if it is safe to do the top loop in parallel,
# otherwise it returns False.
def analyze_file(fname):
    ast = get_ast_from_file(fname)

    # Suggested steps:
    # 1. Get loop constraints (variables and bounds)
    # 2. Get expressions for read_index and write_index
    # 3. Create constraints and check them
    smt_solver_ww = z3.Solver()
    smt_solver_rw = z3.Solver()
    writer_vars = {}
    reader_vars = {}
    variables = []
    # Set these variables to True if there is a write-write (ww)
    # conflict or a read-write (rw) conflict
    ww_conflict = False
    rw_conflict = False
    
    cur_node = ast
    for_nodes = []
    # get for loop node
    while True:
        for_nodes.append(get_loop_constraints(cur_node))
        if is_FOR_node(cur_node.body[0]):
            cur_node = cur_node.body[0]
        else:
            break
    # get loop read and write index node
    for node in cur_node.body:
        if is_FOR_node(node):
            loop_var, lower_bound, upper_bound = get_loop_constraints(node)
        elif is_WRITE_node(node):
            writer_vars[node.args[0].id] = node.args[1].id
        elif is_READ_node(node):
            reader_vars[node.args[0].id] = node.args[1].id

    if smt_solver_rw.check() == z3.sat:
        print(smt_solver_rw.model())
        rw_conflict = False
    else:
        rw_conflict = True

    if smt_solver_ww.check() == z3.sat:
        print(smt_solver_ww.model())
        ww_conflict = False
    else:
        ww_conflict = True

    return ww_conflict, False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pythonfile", help="The python file to be analyzed")
    args = parser.parse_args()
    ww_conflict, rw_conflict = analyze_file(args.pythonfile)
    print("Does the code have a write-write conflict? ", ww_conflict)
    print("Does the code have a read-write conflict?  ", rw_conflict)
