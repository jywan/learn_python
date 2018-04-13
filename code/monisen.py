# -*- coding: utf-8 -*-
# Time    : 31/03/2018 2:13 PM
__author__ = 'wjy'

'''
P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
'''

# import math

def prime(num):
    if num == 1 or num == 2:
        return True
    if num % 2 == 0:
        return False
    else:
        for i in range(2, num//2):
            if num % i == 0:
                return False
    return True


def monisen(no):
    p = 2
    while True:
        if prime(p):
            m = 2**p - 1
            if prime(m):
                no -= 1
            if no == 0:
                return m
        p += 1


print(monisen(int(input())))
'''
print(monisen(1))
print(monisen(2))
print(monisen(3))
print(monisen(4))
print(monisen(5))
print(monisen(6))
print(monisen(7))
'''
