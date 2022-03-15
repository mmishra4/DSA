# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 18:15:59 2022
Return the minimum number of times help taken from Sam.
@author: MMEENAK4
"""

A=5
A = A<<1
n = len(bin(A))
x = []
x = bin(A)
count = 0
for i in x:
    if i == 1:
        print('hi')


def minHelp(A):
    count =0
    A = A<<1
    while A > 0:
        A = A//2
        if A%2 != 0:
            count+= 1
    return count

A= 7
print(minHelp(A))

def check(x, A):
    ct = 0
    for a in A:
        if (a & x) == x:
            ct += 1
        if ct > 3:
            return 1
    return 0

def andOp(A):
    ans = 0
    for i in range(32, -1, -1):
        temp = ans | (1 << i)
        if check(temp, A) == 1:
            ans = temp
    return ans


A = [10, 20, 15, 4, 14]
print(andOp(A))


