#!/usr/bin/env python3

n1 = [0, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = n1
for x1 in n1:
    n2 = n1.copy()
    n2.remove(x1)
    for x2 in n2:
        n3 = n2.copy()
        n3.remove(x2)
        for x3 in n3:
            n4 = n3.copy()
            n4.remove(x3)
            for x4 in n4:
                n5 = n4.copy()
                n5.remove(x4)
                for x5 in n5:
                    n6 = n5.copy()
                    n6.remove(x5)
                    for x6 in n6:
                        n7 = n6.copy()
                        n7.remove(x6)
                        for x7 in n7:
                            # print("{} {} {} {} {} {} {}".format(x1,x2,x3,x4,x5,x6,x7))
                            # sys.exit(0)
                            s1 = 1000*x1+100*x2+10*x3+x4
                            s2 = 1000   +100*x5+10*x6+x2
                            s3 = 10000+1000*x5+100*x3+10*x2+x7
                            if s1+s2==s3:
                                print("{} {} {} {} {} {} {}".format(x1,x2,x3,x4,x5,x6,x7))
