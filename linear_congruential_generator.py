#!/usr/bin/python
seed = 100
modulus = 2**32-1
a = 1664525
c = 1013904223
def next():
    global seed, a, c, modulus
    seed = (a * seed + c) % modulus

# def lcg(modulus, a, c, seed):
#     while True:
#         seed = (a * seed + c) % modulus
#         yield seed
# print lcg(10, 3, 2, 33)

for i in range(1, 100):
    print seed
    next()
