# skeleton file for UCSC CSE211 Homework 2: part 1

from pycfg.pycfg import PyCFG, CFGNode, slurp
import argparse
import re

# Acks: I used
# https://www.geeksforgeeks.org/draw-control-flow-graph-using-pycfg-python/
# to get started with PyCFG.
result = []


# Given a node, returns the instruction as a string
# instructions are of the form:
def get_node_instruction(n):
    return n.attr["label"]


# Given a CFG and a node, return a list of successor nodes
def get_node_successors(CFG, n):
    return CFG.successors(n)


# use PyCFG to get a CFG of the python input file.  Graph is returned
# as a PyGraphviz graph.  Don't worry too much about this function. It
# just uses the PyCFG API
def get_graph(input_file):
    cfg = PyCFG()
    cfg.gen_cfg(slurp(input_file).strip())
    arcs = []
    return CFGNode.to_graph(arcs)


def postorder_dfs(CFG, n, visited):
    global result
    visited[n] = True
    for succ in get_node_successors(CFG, n):
        if visited[succ] is False:
            postorder_dfs(CFG, succ, visited)
    result.append(n)
    return


# You can use get_node_successors(CFG, n) to get a list of n's
# successor nodes.
def compute_LiveOut(CFG, UEVar, VarKill, VarDomain, mode="PO"):
    global result
    result = []
    LiveOut = {n: set() for n in CFG.nodes()}  # set of set
    visited = {n: False for n in CFG.nodes()}
    # hint: you will eventually implement a fixed point iteration. It
    # should look a lot like figure 8.14b in the EAC book.
    # workqueue

    if mode == "PO":
        postorder_dfs(CFG, CFG.get_node(0), visited)
    elif mode == "RPO":
        postorder_dfs(CFG, CFG.get_node(0), visited)
        result.reverse()
    elif mode == "RPOR":
        postorder_dfs(CFG, CFG.get_node(0), visited)
        result.reverse()
        result.pop(0)
        result.append(CFG.get_node(0))
    else:
        result = CFG.nodes()

    counter = 0
    changed = True
    while changed:
        changed = False
        counter += 1
        for n in result:
            temp = set()
            for succ in get_node_successors(CFG, n):
                temp = temp.union(
                    UEVar[succ],
                    LiveOut[succ].intersection(VarDomain.difference(VarKill[succ])),
                )
            # print(temp.__type__)
            if temp != LiveOut[n]:
                changed = True
                LiveOut[n] = temp
    print("counter", counter)
    return LiveOut


# The uninitialized variables are the LiveOut variables from the start
# node. It is fine if your implementation needs to change this
# function. It simply needs to return a set of uninitialized variables
def get_uninitialized_variables_from_LiveOut(CFG, LiveOut):
    return LiveOut[CFG.get_node(0)]


def parse_instruction(i):
    """
    Parses the instruction string and returns a tuple containing:
    - The instruction type (if, while, input, start, stop, assignment)
    - The variable being read (if any)
    - The variable being written (if any)
    """
    if "if" in i:
        return (re.match("\d+:\s*if:\s*(\S+)", i)[1], None)

    if "while" in i:
        return (re.match("\d+:\s*while:\s*(\S+)", i)[1], None)

    if "input" in i:
        return (re.match("\d+:\s*(\S+)\s*=\s*input\(\)", i)[1], None)

    if "start" in i or "stop" in i:
        return (None, None)

    return (
        re.match("\d+:\s*(\S+)\s*=\s*(\S+)", i)[1],
        re.match("\d+:\s*(\S+)\s*=\s*(\S+)", i)[2],
    )


def compute_UEVar(CFG) -> dict:
    UEVar = {f: set() for f in CFG.nodes()}
    for n in CFG.nodes():
        _, var = parse_instruction(get_node_instruction(n))
        if var:
            UEVar[n] = set([var])
    return UEVar


def compute_VarKill(CFG) -> dict:
    VarKill = {f: set() for f in CFG.nodes()}
    for n in CFG.nodes():
        var, _ = parse_instruction(get_node_instruction(n))
        if var:
            VarKill[n] = set({var})
    return VarKill


def compute_VarDomain(CFG):
    # Initialize VarDomain to be the empty set of variables
    VarDomain = set({})
    # for n in CFG.nodes():
    #     print(get_node_instruction(n))

    for n in CFG.nodes():
        var1, var2 = parse_instruction(get_node_instruction(n))
        VarDomain = VarDomain.union(var1) if var1 is not None else VarDomain
        VarDomain = VarDomain.union(var2) if var2 is not None else VarDomain
    return VarDomain


# The testing function. Keep the signature of this function the
# same as it will be used for grading. I highly recommend you keep the
# function exactly the same and simply implement the constituent
# functions.
def find_undefined_variables(input_python_file):
    # Convert the python file into a CFG
    CFG = get_graph(input_python_file)

    print("VarDomain", compute_VarDomain(CFG))
    print("UEVar", compute_UEVar(CFG))
    print("VarKill", compute_VarKill(CFG))

    # Get LiveOut
    LiveOut = compute_LiveOut(
        CFG, compute_UEVar(CFG), compute_VarKill(CFG), compute_VarDomain(CFG)
    )

    # Return a set of unintialized variables
    return get_uninitialized_variables_from_LiveOut(CFG, LiveOut)


# if you run this file, you can give it one of the python test cases
# in the test_cases/ directory.
# see solutions.py for what to expect for each test case.
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pythonfile", help="The python file to be analyzed")
    args = parser.parse_args()
    print(find_undefined_variables(args.pythonfile))
