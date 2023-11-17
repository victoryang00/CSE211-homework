import ast
import argparse
import z3
from typing import Tuple


# Some example functions on how to use the python ast module:
def pp_expr(node):
    # print("node: ", node)
    if is_NAME_node(node):
        return node.id
    if is_NUM_node(node):
        return str(node.n)
    if is_MULTIPLY_node(node):
        return f"({pp_expr(node.left)}*{pp_expr(node.right)})"
    if is_ADDITION_node(node):
        return f"({pp_expr(node.left)}+{pp_expr(node.right)})"


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
    # print("loop_var: ", loop_var)
    lower_bound = pp_expr(FOR_node.iter.args[0])
    upper_bound = pp_expr(FOR_node.iter.args[1])
    # print(
    #     "loop_var: ",
    #     loop_var,
    #     " lower_bound: ",
    #     lower_bound,
    #     " upper_bound: ",
    #     upper_bound,
    # )
    # return the for loop information in some structure
    return (loop_var, lower_bound, upper_bound)


# Check if an ast node is a for loop
def is_FOR_node(node):
    return str(node.__class__) == "<class 'ast.For'>"


def is_NAME_node(node):
    return str(node.__class__) == "<class 'ast.Name'>"


def is_NUM_node(node):
    return str(node.__class__) == "<class 'ast.Constant'>"


def is_MULTIPLY_node(node):
    return str(node.op.__class__) == "<class 'ast.Mult'>"


def is_ADDITION_node(node):
    return str(node.op.__class__) == "<class 'ast.Add'>"


def is_SUBSCRIPT_node(node):  # RHS
    return str(node.value.__class__) == "<class 'ast.Subscript'>"

def is_ASSIGN_node(node):  # RHS
    return str(node.value.__class__) == "<class 'ast.Assign'>"

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
    read_index, write_index = "", ""

    # get for loop node
    while cur_node:
        for_nodes.append(get_loop_constraints(cur_node))
        # Check if the first element in the body is a FOR node
        if is_FOR_node(cur_node.body[0]):
            cur_node = cur_node.body[0]
        else:
            break
        
    print(len(cur_node.body),for_nodes)
    # get outermost for loop
    for expr in cur_node.body:
        # print('sbb:'+str(expr.value.__class__))
        if is_SUBSCRIPT_node(expr):
            write_index = pp_expr(expr.targets[0].slice)
            print("write_index: ", write_index)
        # if is_ASSIGN_node(expr):
        #     # print(expr.value)
            read_index = pp_expr(expr.value.slice)
            # write_index = pp_expr(expr.value.args[2])
            # print("read_index: ", read_index)
            # print("write_index: ", write_index)
            
    for i, func in enumerate(for_nodes):
        variables.append(func[0])
        # variables.append("r" + str(i))
        # variables.append("w" + str(i))
        reader_var = z3.Int("r_" + str(i))
        writer_var = z3.Int("w_" + str(i))
        reader_vars[func[0]] = reader_var
        writer_vars[func[0]] = writer_var

        if i == 0:
            smt_solver_rw.add(reader_vars != writer_vars)
        lower_bound = func[1]
        upper_bound = func[2]
        # add constraints Buggy
        # smt_solver_rw.add(z3.ForAll(
        #     [reader_var, writer_var],
        #     z3.Implies(
        #         z3.And(reader_var >= reader_vars.get(lower_bound, lower_bound),
        #                reader_var < reader_vars.get(upper_bound, upper_bound)),
        #         z3.And(
        #             writer_var >= writer_vars.get(lower_bound, lower_bound),
        #             writer_var <= writer_vars.get(lower_bound, lower_bound),
        #             z3.Not(reader_var == writer_var),
        #         ),
        #     ),
        # ))
        # smt_solver_ww.add(z3.ForAll(
        #     [reader_var, writer_var],
        #         z3.And(
        #             writer_var >= writer_vars.get(lower_bound, lower_bound),
        #             writer_var <= writer_vars.get(lower_bound, lower_bound),
        #             z3.Not(reader_var == writer_var),
        #         ),
        # ))
        smt_solver_rw.add(reader_var >= reader_vars.get(lower_bound, lower_bound))
        smt_solver_rw.add(reader_var < reader_vars.get(upper_bound, upper_bound))

        smt_solver_rw.add(writer_var >= writer_vars.get(lower_bound, lower_bound))
        smt_solver_rw.add(writer_var < writer_vars.get(upper_bound, upper_bound))

        smt_solver_ww.add(writer_var >= writer_vars.get(lower_bound, lower_bound))
        smt_solver_ww.add(writer_var < writer_vars.get(upper_bound, upper_bound))

    for loop_var in variables:
        read_index = read_index.replace(
            loop_var, f"reader_vars[\"{loop_var}\"]"
        )  # latest reader
        write_index = write_index.replace(
            loop_var, f"writer_vars[\"{loop_var}\"]"
        )  # latest writer
    # THis node's assignment
    print(read_index + " == " + write_index)
    
    smt_solver_rw.add(eval(write_index + " == " + read_index ))
    smt_solver_ww.add(eval(write_index + " == " + read_index ))
    
    # print(smt_solver_rw)
    if smt_solver_rw.check() == z3.sat:
        # print(smt_solver_rw.model())
        rw_conflict = True
    else:
        rw_conflict = False

    # print(smt_solver_ww)
    if smt_solver_ww.check() == z3.sat:
        # print(smt_solver_ww.model())
        ww_conflict = True
    else:
        ww_conflict = False
    print(ww_conflict, rw_conflict)
    return ww_conflict, rw_conflict


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pythonfile", help="The python file to be analyzed")
    args = parser.parse_args()
    ww_conflict, rw_conflict = analyze_file(args.pythonfile)
    print("Does the code have a write-write conflict? ", ww_conflict)
    print("Does the code have a read-write conflict?  ", rw_conflict)
