# Follow the template in provided_tests.py to add your own tests here

Tests = [   
    {
	"Name"    : "Yiwei 1",
	"Outcome" : [1],
	"Program" : """
                x = 1 * 1 ^ 1 * (1 + 1) - 1;
                print(x);
               """
    },
    {
        "Name"    : "Yiwei 2",
        "Outcome" : [140],
        "Program" : """
                    x = 62 + 78;
                    {
                        x = 1;
                    }
                    y = x;
                    {
                        x = 3;
                    }
                    print(y);
                   """
    },
    {
        "Name"    : "Yiwei 3",
        "Outcome" : "SymbolTableException",
        "Program" : """
                    x = y;
                    y = 12;
                   """
    },
    {
        "Name"    : "Yiwei 4",
        "Outcome" : [0],
        "Program" : """
                    x = 2;
                    y = 3;
                    z = (x + y) * (x - y) / x ^ y;
                    print(z);
                    z = x + y * x - y / x ^ y;
                    print(z);
                   """
    }
    ]
