import argparse 

def local_value_numbering(f):
    f = open(f)
    s = f.read()
    f.close()

    pre = s.split("// Start optimization range")[0]
    post = s.split("// Start optimization range")[1].split("// End optimization range")[1]
    to_optimize = s.split("// Start optimization range")[1].split("// End optimization range")[0]

    # hint: perform the local value numbering optimization here on to_optimize
    
    print(pre)

    # hint: print out any new variable declarations you need here

    # hint: print out the optimized local block here

    # hint: store any new numbered variables back to their unumbered counterparts here
    
    print(post)

    # You should keep track of how many instructions you replaced
    #print("// replaced: " + str(replaced))    
    

# if you run this file, you can give it one of the python test cases
# in the test_cases/ directory.
# see solutions.py for what to expect for each test case.
if __name__ == '__main__': 
    parser = argparse.ArgumentParser()   
    parser.add_argument('cppfile', help ='The cpp file to be analyzed') 
    args = parser.parse_args()
    local_value_numbering(args.cppfile)
