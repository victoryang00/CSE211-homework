import skeleton as solution
from importlib import import_module
import sys

if len(sys.argv) != 2:
    print("Please provide a test file")
    exit(0)
    
Tests = import_module(sys.argv[1]).Tests

for t in Tests:
    print("Running test ", t["Name"])
    
    if t["Outcome"] is "SymbolTableException":
        try:
            solution.parse_string(t["Program"])
        except solution.SymbolTableException:
            print("  Passed")
        else:
            assert(False)

    elif t["Outcome"] is "ParsingException":
        try:
            solution.parse_string(t["Program"])
        except solution.ParsingException:
            print("  Passed")
        else:            
            assert(False)

    else:
        assert(type(t["Outcome"]) == list)
        x = solution.parse_string(t["Program"])
        compare = t["Outcome"]
        for v in zip(x,compare):
            assert(str(v[0]) == str(v[1]))
        print("  Passed")
