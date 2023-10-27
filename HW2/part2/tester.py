import test_cases.solutions
import sys
import os

import skeleton as candidate

test_num = int(sys.argv[1])
test_file = os.path.join("test_cases", str(test_num) + ".py")
undefs = candidate.find_undefined_variables(test_file)
sol = test_cases.solutions.solutions[test_num]

if undefs != sol:
    print("failed on test case number: " + str(test_num))
    print("expected: " + str(sol))
    print("got: " + str(undefs))
else:
    print("passed test: " + str(test_num))
    print("---")
