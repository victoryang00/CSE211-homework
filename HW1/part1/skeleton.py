import ply.lex as lex
import ply.yacc as yacc
import sys



# def remove_tailing_zeros(float):
#     if int(float) == float:
#         return int(float)
#     else:
#         return float
    
    
# You don't need to implement any more of these
# exceptions; just throw them when required.
class SymbolTableException(Exception):
    pass

class ParsingException(Exception):
    pass

# Implement this class, i.e. provide some class members and implement
# the functions.
class SymbolTable:

    def __init__(self):
        self.scope = [{}]
    
    def insert(self,name,value):
        self.scope[-1][name] = value

    def lookup(self, name):
        for i in self.scope[::-1]:
            if name in i:
                return i[name]
        print(f"Could not find {name} in {self.scope}!", file=sys.stderr)
        raise SymbolTableException()
    
    def push_scope(self):
        self.scope.append({})

    def pop_scope(self):
        self.scope.pop()

# Global variables I suggest you use (although you are not required)

to_print = []
ST = SymbolTable()

# define tokens here

reserved = {
   'print' : 'PRINT'
}

tokens = ["PLUS", "MINUS", "MULT", "DIV", "CARROT", "ASSIGN", "NUM", "LPAR", "RPAR", "LBRAC", "RBRAC", "ID", "SEMI"] + list(reserved.values())

t_PLUS = "\+"
t_MINUS = "\-"
t_MULT = "\*"
t_DIV = "/"
t_CARROT = "\^"
t_ASSIGN = "="
t_NUM = "(([1-9][0-9]*)|0)(\.[0-9]*[1-9])?"
t_LPAR = "\("
t_RPAR = "\)"
t_LBRAC = "\{"
t_RBRAC = "\}"
t_SEMI = ";"
t_ignore = " "

def t_error(t):
    print(f"Token Error!, {t}", file=sys.stderr)
    raise ParsingException()
    
def t_ID(t):
    r'[a-zA-Z][a-zA-Z]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
lexer = lex.lex()

#define production rules here

# I don't understand really why this is needed but found it in the PLY documentation to fix unreachability errors.
start = 'statement_list'

# From PLY Documentation
def p_empty(p):
    'empty :'
    pass

def p_statement_list(p):
    """
    statement_list : statement statement_list
                   | empty 
    """
    # or statment instead of empty if we dont allow empty programs.
    pass

def p_statement(p):
    """
    statement : assignment
              | print
              | scope
    """
    pass

def p_assignment(p):
    "assignment : ID ASSIGN expr SEMI"
    ST.insert(p[1], p[3])

def p_print(p):
    "print : PRINT LPAR ID RPAR SEMI"
    # to_print.append(remove_tailing_zeros(ST.lookup(p[3])))
    to_print.append(ST.lookup(p[3]))

def p_scope(p):
    "scope : scope_start statement_list scope_end"
    pass

def p_scope_start(p):
    "scope_start : LBRAC"
    ST.push_scope()
    
def p_scope_end(p):
    "scope_end : RBRAC"
    ST.pop_scope()

def p_expr(p):
    """
    expr : expr PLUS term
         | expr MINUS term
         | term
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    else:
        print("WTF???", p[2])

def p_term(p):
    """
    term : term MULT expo
         | term DIV expo
         | expo
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    else:
        print("WTF???", p[2])
    
def p_expo(p):
    """
    expo : factor CARROT expo
         | factor
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '^':
        p[0] = p[1] ** p[3]
    else:
        print("WTF???", p[2])
    
def p_factor(p):
    """
    factor : LPAR expr RPAR
           | NUM
    """
    if len(p) == 2:
        p[0] = float(p[1])
    else:
        p[0] = float(p[2])

def p_factor_id(p):
    "factor : ID "
    p[0] = ST.lookup(p[1])

def p_error(p):
    print(f"Parse Error!, {p}", file=sys.stderr)
    raise ParsingException()

parser = yacc.yacc(debug=True)

def parse_string(s):
    global to_print
    global ST
    ST = SymbolTable()
    to_print = []
    parser.parse(s)
    return to_print
    

# Example on how to test locally in this file:

# res = parser.parse("""
# x = 5 + 4 * 5;
# i = 3 - 4 - 5;
# print(i);
# {
# x = 5 + 4 * 5;
# }
# {}{}{}{{{}}}

# """)

# print(res)

# parser.parse("""
# x = 5 + 4 * 5;
# i = 1 + 0 - 1;
# print(i);
# {
#  l = 5 ^ x;
# {
#    k = 5 + 7;
# }
# }
# q = x / i;
# print(q);
# """)

# for p in to_print:
#    print(p)
