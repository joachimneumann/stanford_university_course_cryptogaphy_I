#!/usr/bin/env python3

# import cProfile
import sys

largestN = -1
largest=[]

def calcMax(allowed, stamp, debug):
    global largest, largestN
    if allowed >= 1:
        ns1=set()
        for s in stamp:
            ns1.add(s)
        ns2=ns1.copy()
        final = ns2.copy()
    if allowed >= 2:
        for n in ns1:
            for s in stamp:
                ns2.add(s+n)
        ns3 = ns2.copy()
        final = ns3.copy()
    if allowed >= 3:
        for n in ns2:
            for s in stamp:
                ns3.add(s+n)
        ns4 = ns3.copy()
        final = ns4.copy()
    if allowed >= 4:
        for n in ns3:
            for s in stamp:
                ns4.add(s+n)
        final = ns4.copy()

    n = 1
    while n in final:
        n = n + 1
    n = n - 1
    if n == largestN:
        largest.append(stamp)
    if n > largestN:
        largestN = n
        largest = [stamp]
    # if debug:
    #     print("    {} -> {}".format(stamp, n))
    return n


allowedStamps = 4
debug = True

s1 = 1
largestN = -1
n1 = calcMax(allowedStamps, [s1], False)
for s2 in list(range(s1+1, n1+2)):
    n2 = calcMax(allowedStamps, [s1,s2], debug)
for l in largest:
    print(" 2 ==> {} -> {}".format(l, largestN))
print()

largestN = -1
n1 = calcMax(allowedStamps, [s1], False)
for s2 in list(range(s1+1, n1+2)):
    n2 = calcMax(allowedStamps, [s1,s2], False)
    for s3 in list(range(s2+1, n2+2)):
        n3 = calcMax(allowedStamps, [s1,s2,s3], debug)
for l in largest:
    print(" 3 ==> {} -> {}".format(l, largestN))
print()

largestN = -1
n1 = calcMax(allowedStamps, [s1], False)
for s2 in list(range(s1+1, n1+2)):
    n2 = calcMax(allowedStamps, [s1,s2], False)
    for s3 in list(range(s2+1, n2+2)):
        n3 = calcMax(allowedStamps, [s1,s2,s3], False)
        for s4 in list(range(s3+1, n3+2)):
            n4 = calcMax(allowedStamps, [s1,s2,s3,s4], debug)
for l in largest:
    print(" 4 ==> {} -> {}".format(l, largestN))
print()

largestN = -1
n1 = calcMax(allowedStamps, [s1], False)
for s2 in list(range(s1+1, n1+2)):
    n2 = calcMax(allowedStamps, [s1,s2], False)
    for s3 in list(range(s2+1, n2+2)):
        n3 = calcMax(allowedStamps, [s1,s2,s3], False)
        for s4 in list(range(s3+1, n3+2)):
            n4 = calcMax(allowedStamps, [s1,s2,s3,s4], False)
            for s5 in list(range(s4+1, n4+2)):
                n5 = calcMax(allowedStamps, [s1,s2,s3,s4,s5], debug)
for l in largest:
    print(" 5 ==> {} -> {}".format(l, largestN))
print()

largestN = -1
n1 = calcMax(allowedStamps, [s1], False)
for s2 in list(range(s1+1, n1+2)):
    n2 = calcMax(allowedStamps, [s1,s2], False)
    for s3 in list(range(s2+1, n2+2)):
        n3 = calcMax(allowedStamps, [s1,s2,s3], False)
        for s4 in list(range(s3+1, n3+2)):
            n4 = calcMax(allowedStamps, [s1,s2,s3,s4], False)
            for s5 in list(range(s4+1, n4+2)):
                n5 = calcMax(allowedStamps, [s1,s2,s3,s4,s5], False)
                for s6 in list(range(s5+1, n5+2)):
                    n6 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6], debug)
for l in largest:
    print(" 6 ==> {} -> {}".format(l, largestN))
print()

largestN = -1
n1 = calcMax(allowedStamps, [s1], False)
for s2 in list(range(s1+1, n1+2)):
    n2 = calcMax(allowedStamps, [s1,s2], False)
    for s3 in list(range(s2+1, n2+2)):
        n3 = calcMax(allowedStamps, [s1,s2,s3], False)
        for s4 in list(range(s3+1, n3+2)):
            n4 = calcMax(allowedStamps, [s1,s2,s3,s4], False)
            for s5 in list(range(s4+1, n4+2)):
                n5 = calcMax(allowedStamps, [s1,s2,s3,s4,s5], False)
                for s6 in list(range(s5+1, n5+2)):
                    n6 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6], False)
                    for s7 in list(range(s6+1, n6+2)):
                        n7 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6,s7], debug)
for l in largest:
    print(" 7 ==> {} -> {}".format(l, largestN))
print()


largestN = -1
n1 = calcMax(allowedStamps, [s1], False)
for s2 in list(range(s1+1, n1+2)):
    n2 = calcMax(allowedStamps, [s1,s2], False)
    for s3 in list(range(s2+1, n2+2)):
        n3 = calcMax(allowedStamps, [s1,s2,s3], False)
        for s4 in list(range(s3+1, n3+2)):
            n4 = calcMax(allowedStamps, [s1,s2,s3,s4], False)
            for s5 in list(range(s4+1, n4+2)):
                n5 = calcMax(allowedStamps, [s1,s2,s3,s4,s5], False)
                for s6 in list(range(s5+1, n5+2)):
                    n6 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6], False)
                    for s7 in list(range(s6+1, n6+2)):
                        n7 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6,s7], False)
                        for s8 in list(range(s7+1, n7+2)):
                            n8 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6,s7,s8], debug)
for l in largest:
    print(" 8 ==> {} -> {}".format(l, largestN))
print()


largestN = -1
n1 = calcMax(allowedStamps, [s1], False)
for s2 in list(range(s1+1, n1+2)):
    n2 = calcMax(allowedStamps, [s1,s2], False)
    for s3 in list(range(s2+1, n2+2)):
        n3 = calcMax(allowedStamps, [s1,s2,s3], False)
        for s4 in list(range(s3+1, n3+2)):
            n4 = calcMax(allowedStamps, [s1,s2,s3,s4], False)
            for s5 in list(range(s4+1, n4+2)):
                n5 = calcMax(allowedStamps, [s1,s2,s3,s4,s5], False)
                for s6 in list(range(s5+1, n5+2)):
                    n6 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6], False)
                    for s7 in list(range(s6+1, n6+2)):
                        n7 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6,s7], False)
                        for s8 in list(range(s7+1, n7+2)):
                            n8 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6,s7,s8], False)
                            for s9 in list(range(s8+1, n8+2)):
                                n9 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6,s7,s8,s9], debug)
for l in largest:
    print(" 9 ==> {} -> {}".format(l, largestN))
print()

largestN = -1
n1 = calcMax(allowedStamps, [s1], False)
for s2 in list(range(s1+1, n1+2)):
    n2 = calcMax(allowedStamps, [s1,s2], False)
    for s3 in list(range(s2+1, n2+2)):
        n3 = calcMax(allowedStamps, [s1,s2,s3], False)
        for s4 in list(range(s3+1, n3+2)):
            n4 = calcMax(allowedStamps, [s1,s2,s3,s4], False)
            for s5 in list(range(s4+1, n4+2)):
                n5 = calcMax(allowedStamps, [s1,s2,s3,s4,s5], False)
                for s6 in list(range(s5+1, n5+2)):
                    n6 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6], False)
                    for s7 in list(range(s6+1, n6+2)):
                        n7 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6,s7], False)
                        for s8 in list(range(s7+1, n7+2)):
                            n8 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6,s7,s8], False)
                            for s9 in list(range(s8+1, n8+2)):
                                n9 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6,s7,s8,s9], False)
                                for s10 in list(range(s9+1, n9+2)):
                                    n10 = calcMax(allowedStamps, [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10], debug)
for l in largest:
    print("10 ==> {} -> {}".format(l, largestN))
print()
