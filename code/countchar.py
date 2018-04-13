# -*- coding: utf-8 -*-
# Time    : 2018年04月12日20:55:58
__author__ = 'wjy'


def countchar(str):
    res = [0] * 26
    for i in list(str):
        if i.isalpha():
            res[ord(i.lower())-ord('a')] += 1
    return res

if __name__ == "__main__":
    str = input()
    print(countchar(str))