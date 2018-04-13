# -*- coding: utf-8 -*-
# Time    : 19/03/2018 10:01 PM
__author__ = 'wjy'


def by_name(t):
    return t[0]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)