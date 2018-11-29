#!/usr/bin/python

import sys

file = open('code.txt')
codes = []
for line in file:
    numbers = line.split(',')
    for n in numbers:
        i = int(n)
        codes.append(i)
print len(codes)
print max(codes)
print min(codes)
