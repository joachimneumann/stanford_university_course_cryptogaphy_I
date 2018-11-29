#!/usr/bin/python

import sys
from crypto import *


print xor(stringToHex("932330e4"), stringToHex("b645c008"))
print xor(stringToHex("fdc48bfb"), stringToHex("c5e2364b"))
print xor(stringToHex("1351e2e1"), stringToHex("8dd39154"))
print xor(stringToHex("c0b1d266"), stringToHex("b2146dd0"))

print xor(stringToHex("9f970f4e"), stringToHex("6068f0b1"))
print xor(stringToHex("7c2822eb"), stringToHex("325032a9"))
print xor(stringToHex("4af53267"), stringToHex("87a40cfa"))
print xor(stringToHex("2d1cfa42"), stringToHex("eea6e3dd"))


print len("If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.")
print len("In this letter I make some remarks on a general principle relevant to enciphering in general and my machine.")
print len("significance of this general conjecture, assuming its truth, is easy to see. It means that it may be feasible to design ciphers that are effectively unbreakable.")
print len("most direct computation would be for the enemy to try all 2^r possible keys, one by one.")
