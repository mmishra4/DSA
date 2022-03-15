# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 17:27:06 2022

@author: MMEENAK4
"""
def preCompute(arr, n, prefix):
  prefix[0] = arr[0]
  for i in range(1, n):
    prefix[i] = prefix[i - 1] + arr[i]
 
# Returns sum of elements in arr[i..j]
# It is assumed that i <= j
def rangeSum(l, r):
  if l == 0:
    return(prefix[r])   
  return(prefix[r] - prefix[l - 1])
  
# function to find the equilibrium index
def rangeS(A, B):
    n = len(A)
    prefix = [0 for i in range(n)]    
    preCompute(A,n,prefix)
    print(prefix)
    m = len(B)
    P = []
    for i in range(m):
        P.append(rangeSum(B[i][0]-1, B[i][1]-1))
    print(P)
     
# Driver code
A = [1, 2, 3, 4, 5]
B = [[1, 4], [2, 3]]
rangeS(A,B)