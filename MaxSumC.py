# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 18:38:17 2022

@author: MMEENAK4
"""

def findMinAvgSubarray(A, B, C):
    ans=0
    for i in range(A):
        sum=0
        for j in range(i, A):
            sum+=C[j]
            if (sum<=B):
                ans = max(sum, ans)
            else:
                break
    return ans
                
                

A = 5
B = 12
C = [2, 1, 3, 4, 5]
print(findMinAvgSubarray(A, B, C))