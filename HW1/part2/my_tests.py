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
         ("7.0.0.(p.7.s.s.e.d|6.7.i.0.e.d)?", "70067i0ed", True),
         ("J.a.c.k", "Jack", True),
         ("J.a.c.k | B.o.b", "Jack", True),
         ("J.a.c.k | B.o.b", "Bob", True),
         ("J.a.c.k | B.o.b", "JackBob", False),
         ("J*", "J", True),
         ("J*", "JJJJJJJ", True),
         ("J*", "", True),
         ("J*", "JJJJack", False),
         ("(J*.A*.C*.K*)*", "J", True),
         ("(J*.A*.C*.K*)*", "JACKJAKCKACKACJKACJKA", True),
         ("(J*.A*.C*.K*)*", "ACKAJACK", True),
         ("(J*.A*.C*.K*)*", "jack", False),
         ("J?|A?|C*|(B.O.B)", "", True),
         ("J?|A?|C*|(B.O.B)", "J", True),
         ("J?|A?|C*|(B.O.B)", "A", True),
         ("J?|A?|C*|(B.O.B)", "C", True),
         ("J?|A?|C*|(B.O.B)", "JA", False),
         ("J?|A?|C*|(B.O.B)", "CCCCCCC", True),
         ("J?|A?|C*|(B.O.B)", "CBOB", False),
         ("(1.0.0)?|(1.0.0)*", "100", True),
         ("(1.0.0)?|(1.0.0)*", "100100100", True),
         ("J?|A?|C*|(B.O.B)", "10010010", False),
         ("(J.A.C.K)?|J*.A", "JACK", True),
         ("(J.A.C.K)?|J*.A", "", True),
         ("(J.A.C.K)?|J*.A", "JA", True),
         ("(J.A.C.K)?|J*.A", "JJJA", True),
         ("(J.A.C.K)?|J*.A", "JAC", False),
         ("(J.A.C.K)?|J*.A", "JJJJAAA", False),
         ("(J.A.C.K)?|J*.A", "WHY_DID_THE_CHICKEN_CROSS_THE_ROAD?", False),
    ]
