Tests = [
    {
	"Name"    : "Test 1",
	"Outcome" : [16],
	"Program" : """
                 x = 1 + 1;
                 y = x + x;
                 z = y ^ 2;
                 print(z);
               """
    },
    {
	"Name"    : "Test 2",
        "Outcome" : [21,30],
	"Program" : """
                    x = 1 + 2 * 10;
                    y = (1+2) * 10;
                    print(x);
                    print(y);
               """
    },
    {
	"Name"    : "Test 3",
	"Outcome" : [-5,3],
	"Program" : """
                    x = 2 - 3 - 4;
                    y = 2 - (3 - 4);
                    print(x);
                    print(y);
                """
    },
    {
	"Name"    : "Test 4",
	"Outcome" : "ParsingException",
	"Program" : """
                    x = 1 ++ 1;
                 """
    },
    {
	"Name"    : "Test 5",
	"Outcome" : "ParsingException",
	"Program" : """
                    x5 = 1 + 2 * 10;
                 """
    },
    {
	"Name"    : "Test 6",
	"Outcome" : "ParsingException",
	"Program" : """
                    x = 2 - 3 - 4;
                    y = 2 - (3 - 4)
                 """
    },
    {
	"Name"    : "Test 6",
	"Outcome" : "SymbolTableException",
	"Program" : """
                    x = 1 + z;
                 """
    },
    {
	"Name"    : "Test 7",
	"Outcome" : "SymbolTableException",
	"Program" : """
                    {
                      x = 12 + 6;
                    }
                    z = x + x;
                 """
    },
    {
	"Name"    : "Test 8",
	"Outcome" : "SymbolTableException",
	"Program" : """
                    x = 62 + 78;
                    {
                      z = x + 1;
                      {
                        y = z + x;
                      }
                    w = y;
                    }
                 """
    }
]
