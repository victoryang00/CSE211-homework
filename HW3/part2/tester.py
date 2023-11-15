from skeleton import analyze_file

# fill these in with the expected result for each test
tests = {"0.py" : (False, False),
         "1.py" : (False, False),
         "2.py" : (False, False),
         "3.py" : (False, False),
         "4.py" : (False, False),
         "5.py" : (False, False),
         "6.py" : (False, False),
         "7.py" : (False, False)
}

passed = 0
failed = 0
for t in tests:
    result = tests[t]
    test_file = "test_cases/" + t
    print("running: " + test_file)
    print("")
    res = analyze_file(test_file)
    if res != result:
        print("failed test: " + t)
        failed += 1
    else:
        passed += 1

print("passed: " + str(passed))
print("failed: " + str(failed))
    
