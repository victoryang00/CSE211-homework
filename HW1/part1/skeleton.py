import ply.lex as lex

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
        pass
    
    def insert(self,name,value):
        pass

    def lookup(self, name):
        pass
    
    def push_scope(self):
        pass

    def pop_scope(self):
        pass

# define tokens here
tokens = []

lexer = lex.lex()

#define production rules here

parser = yacc.yacc(debug=True)

# Global variables I suggest you use (although you are not required)
to_print = []
ST = SymbolTable()

def parse_string(s):
    global to_print
    global ST
    ST = SymbolTable()
    to_print = []
    parser.parse(s)
    return to_print
    
# Example on how to test locally in this file:

#parser.parse("""
#x = 5 + 4 * 5;
#i = 1 + 1 * 0;
#print(i);
#{
#  l = 5 ^ x;
#{
#    k = 5 + 7;
#}
#}
#q = x / i;
#print(q);
#""")

#for p in to_print:
#    print(p)
