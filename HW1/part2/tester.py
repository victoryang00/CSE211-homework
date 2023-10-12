from skeleton import match_regex
from importlib import import_module
import sys

if len(sys.argv) != 2:
    print("Please provide a test file")
    exit(0)
    
Tests = import_module(sys.argv[1]).Tests

failed = 0
total = len(Tests)
for t in Tests:
    result = match_regex(t[0], t[1])
    if result != t[2]:
        failed += 1
        print("--")
        print("failed: matching string " + t[1] + " to regex " + t[0])
        print("expected " + str(t[2]))
        print("got " + str(result))
        print("--")

print("total tests: " + str(total))
print("passed: " + str(total - failed))
print("failed: " + str(failed))

    
    






