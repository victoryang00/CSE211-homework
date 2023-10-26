# Follow the template in provided_tests.py to add your own tests here

Tests = [   
    {
	"Name"    : "Yiwei 1",
	"Outcome" : [1.0],
	"Program" : """
                x = 1 * 1 ^ 1 * (1 + 1) - 1;
                print(x);
               """
    },
    {
        "Name"    : "Yiwei 2",
        "Outcome" : [140.0],
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
        "Outcome" : [-0.625, 7.625],
        "Program" : """
                    x = 2;
                    y = 3;
                    z = (x + y) * (x - y) / x ^ y;
                    print(z);
                    z = x + y * x - y / x ^ y;
                    print(z);
                   """
    },
    {
	"Name"    : "Jack 1",
	"Outcome" : [2.001],
	"Program" : """
                x = 1 + 1.001;
                print(x);
               """
    },
    {
	"Name"    : "Jack 2",
	"Outcome" : [1.0, 2.0, 3.0, 9.0, 9.0, 12.12],
	"Program" : """
                x = 1 + 0;
                print(x);
                y = 1 + 1;
                print(y);
                x = 1 + 2;
                print(x);
                z = x + y * x;
                print(z);
                print(z);
                x = 1.01;
                z = x * y + x * z + x;
                print(z);
               """
    },
    {
	"Name"    : "Jack 3",
	"Outcome" : [],
	"Program" : """
                {}
               """
    },
    {
	"Name"    : "Jack 4",
	"Outcome" : [1024.0, 1048576.0, 1.0],
	"Program" : """
                {
                    x = 2 ^ 10;
                    y = x ^ 2;
                    print(x);
                    print(y);
                }
                x = 1;
                print(x);
               """
    },
    {
	"Name"    : "Jack 5",
	"Outcome" : [10.001, 100.1231, 100.0, 10.001, 100.0, 100.0, 100.0],
	"Program" : """
                z = 100;
                {
                    {
                        x = 10.001;
                        {
                            print(x);
                            x = 100.1231;
                            print(x);
                            print(z);
                        }
                        print(x);
                        print(z);
                    }
                    print(z);
                }
                print(z);
               """
    },
    {
	"Name"    : "Jack 6",
	"Outcome" : [100.0],
	"Program" : """
                x = 100;
                {
                    y = 10;
                    x = y;
                    y = x;
                }
                x = x;
                print(x);
               """
    },
    {
	"Name"    : "Jack 7",
	"Outcome" : "SymbolTableException",
	"Program" : """
                x = 100;
                {
                    y = 10;
                    x = y;
                    y = x;
                }
                x = y;
               """
    },
    {
	"Name"    : "Jack 8",
	"Outcome" : "SymbolTableException",
	"Program" : """
                {
                    {
                        {
                            x = 10;
                        }
                        x = 10;
                    }
                    x = 10;
                }
                y = x;
               """
    }
    ]
