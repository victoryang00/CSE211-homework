from skeleton import analyze_file

# fill these in with the expected result for each test
tests = {"0.py" : (True, True),
         "1.py" : (False, False),
         "2.py" : (True, True),
         "3.py" : (False, False),
         "4.py" : (True, True),
         "5.py" : (True, False),
         "6.py" : (True, True),
         "7.py" : (True, True)
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
    
