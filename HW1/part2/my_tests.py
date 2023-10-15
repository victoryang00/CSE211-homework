# Follow the template in provided_tests.py to add your own tests here

Tests = [("7.b.0", "7b0", True),
         ("6?", "6", True),
         ("6?", "", True),
         ("6?", "2", False),
         ("6|2.2?", "", False),
         ("6|2.2?", "2", True),
         ("6|2.2?", "22", True),
         ("6|2.2?", "6", True),
         ("e.2.0.i.t.e.(2.e.u.t)?", "e20ite2eut", True),
         ("e.2.0.i.t.e.(2.e.u.t)?", "e20ite", True),
         ("e.2.0.i.t.e.(2.e.u.t)? | 0.7.r.s?", "e20ite", True),
         ("e.2.0.i.t.e.(2.e.u.t)? | 0.7.r.s?", "e20ite2eut", True),
         ("e.2.0.i.t.e.(2.e.u.t)? | 0.7.r.s?", "07r", True),
         ("e.2.0.i.t.e.(2.e.u.t)? | 0.7.r.s?", "07rs", True),
         # 22 07ses:
         ("7.0.0.(p.7.s.s.e.d|6.7.i.0.e.d)?", "700", True),
         ("7.0.0.(p.7.s.s.e.d|6.7.i.0.e.d)?", "700p7ssed", True),
         ("7.0.0.(p.7.s.s.e.d|6.7.i.0.e.d)?", "70067i0ed", True)
    ]
