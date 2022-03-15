# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 09:43:03 2022
On the first row, we write a 0. Now in every subsequent row, we look at the 
previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row A and index B, return the Bth indexed symbol in row A. 
(The values of B are 1-indexed.) (1 indexed).
@author: MMEENAK4
"""

import sys
sys.setrecursionlimit(1000000)

def Grammar(N,K):
    if N==1:
        return 0
    if K%2==0:
        if Grammar(N-1,K/2) == 0:
            return 1
        else:
            return 0
    else:
        if Grammar(N-1,(K+1)/2) == 0:
            return 0
        else:
            return 1
        
    return Grammar(N,K)

A = 2
B = 1
print(Grammar(A,B))

"""
The gray code is a binary numeral system where two successive values differ 
in only one bit.
Given a non-negative integer A representing the total number of bits in the 
code, print the sequence of gray code.
A gray code sequence must begin with 0.
"""

def grayCode(A):    
    ans = []
    for i in range(2 ** A):
        ans.append((i>>1) ^ i)
    return ans

A = 2
print(grayCode(A))
