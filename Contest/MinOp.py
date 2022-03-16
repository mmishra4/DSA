# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:00:08 2022
Little Pony is given an array A of N integers. In a particular operation, he can set any element of the array equal to -1
He want your help in finding out the minimum number of operations such that the maximum element of the resulting array is B. If not possible than return -1

A = Integer array | B = integer

i/p: A=[2,4,3,1,5]
B=3

A=[1,4,2]
B=3
o/p: -1
@author: MMEENAK4
"""

def minOpCnt(A, B):
    A.sort()
    cnt = 0 
    if B in A:        
        for i in A:
            if i> B:
                cnt += 1
    if cnt>0:
        return cnt
    else:
        return -1
    
A=[2,4,3,1,5]
B=3
A=[1,4,2]
B=3
print(minOpCnt(A,B))
    
            
