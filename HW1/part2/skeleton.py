import ply.lex as lex
import ply.yacc as yacc

# Build the lexer
lexer = lex.lex()
tokens = ['LPAREN','RPAREN','STAR','OR','QUES','CH',"DOT","UNION"]
t_CH = r'[a-zA-Z]'
t_UNION = r'\|'
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STAR = r'\*'
t_OR = r'\|'
t_QUES = r'\?'

from typing import TypedDict, Unpack
class Leaf(TypedDict):
    charactor: str

class Op(TypedDict):
    lhs :str
    rhs :str
    op :str

def get_leaf(**kwargs: Unpack[Leaf])-> None:
    for k in kwargs.items():
        return Leaf(k)

def get_op(**kwargs: Unpack[Op])-> None:
    for k,v1,v2 in kwargs.items():
        return Op(k,v1,v2)

def make_leaf(re1)-> Leaf:
    return get_leaf(charactor=char)

def make_star(re1)-> Leaf:
    if re1 is None:
        return None
    if is_epsilon(re1):
        return re1
    return get_leaf(charactor=char)
## Nullable function starting here:

# Top level Nullable function: this function takes an RE (re) as an
# AST and returns:
# (1) an RE AST for the empty string (epsilon) if the re matches the empty string (epsilon).
# (2) an RE AST for the empty set if the re does NOT match the empty string.

# Implement this function
def nullable(re):
    if isinstance(re,Leaf):
        if re is None:
            return re
        else:
            return None
    elif isinstance(re,Op):
        if re.op == "CONCAT":
            return nullable(re.lhs) and nullable(re.rhs)
        elif re.op == "OR":
            return nullable(re.lhs) or nullable(re.rhs)
        elif re.op == "STAR":
            return make_leaf("")

# derivative function starting here:

# This function takes a character (char) and an RE AST (re). It
# returns the RE (as an AST) that is the derivative of re with respect
# to char.

# More specifically: say the input RE (re) accepts the set of strings S.
# The derivative of re with respect to char is all strings in S that began
# with char, and now have char ommitted. Here are some examples:

# Given a RE (call it re) that matches the language {aaa, abb, ba, bb,
# ""}, the derivative of re with respect to 'a' is {aa, bb}. These are
# the original strings that began with 'a' (namely {aaa, abb}), with
# the first 'a' character removed. Please review the lecture or the
# "Regular-expression derivatives reexamined" for more information

# implement this function:
def derivative_re(char, re):
    if re is None:
        return None
    elif isinstance(re, Leaf):
        pass
parser = yacc.yacc()

# High-level function to match a string using regular experession
# derivatives:
def match_regex_ast(re, to_match):

    # create the derivative for each character of the string in sequence
    for char in to_match:
        re =  derivative_re(char, re)

    # the string matches if and only if the empty string is matched by the derivative RE
    return False # you will need to write something like: is_epsilon(nullable(re)) here

# Keep this function exactly how it is for grading to use with the tester scripts.
def match_regex(reg_ex, string):
    return match_regex_ast(parser.parse(reg_ex), string)

# Use this conditional to test your script locally
if __name__ == "__main__":
    d_re = parser.parse("(h.i)* | c.s.e*.2.1.1")

    # should pass
    print(parse_re(d_re, "hi") == True)    
    print(parse_re(d_re, "hihi") == True)
    print(parse_re(d_re, "cse211") == True)
    print(parse_re(d_re, "cs211") == True)
    print(parse_re(d_re, "cseee211") == True)

    # should fail
    print(parse_re(d_re, "hhh") == False)
    print(parse_re(d_re, "cseee21") == False)
    print(parse_re(d_re, "211") == False)
