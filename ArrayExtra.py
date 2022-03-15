# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:45:47 2022
Return maximum size subarray of A having only non-negative elements. 
If there are more than one such subarrays, return the one having earliest starting index in A.
@author: MMEENAK4
"""

# Function that returns
# the longest subarray
# of non-negative integers
def longestSubarry(A):
    ret = [[]]
    for i in A:
        if i < 0:
            ret.append([])
        else:
            ret[-1].append(i)
    mxlen = max([len(i) for i in ret])
    for i in ret:
        if len(i) == mxlen:
            return i
 
def check(max_arr,curr):
    if sum(curr) > sum(max_arr):
                max_arr = curr
    elif sum(curr) == sum(max_arr):
        if len(curr) > len(max_arr):
            max_arr = curr
        elif len(curr) == len(max_arr):
            if max_arr and (curr[0] > max_arr[0]):
                max_arr = curr
    return max_arr

def maxset(A):
    curr = []
    max_arr = []
    for i in A:
        if i >= 0:
            curr.append(i)
        else:
            max_arr = check(max_arr,curr)
            curr = []
    max_arr = check(max_arr,curr)                    
    return max_arr
 
# Driver code
 
#A= [1, 0, 4, 0, 1, -1, -1, 0, 0, 1, 0]
A = [5, 6, -1, 7, 8]
print(longestSubarry(A))
#print(maxset(A))
 """
Created on Tue Jan 25 18:45:47 2022
.Print Hollow Inverted Right Triangle Star Pattern
@author: MMEENAK4
"""
# Python Program to 
 
rows = int(input())

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        if i == 1 or i == rows or j == 1 or j == i:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
    
 """
Created on Tue Jan 25 18:45:47 2022
.Print Hollow Diamond
@author: MMEENAK4
"""
# Python Program to 
 
row = int(input())

# Upper part of hollow diamond
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print("*", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part of hollow diamond
for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print("*", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#======================

n = int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*", end=" ")
    for j in range(2*(n-i)):
        print(" ", end=" ")
    for j in range(i,0,-1):
        print("*", end=" ")
    print()
    
for i in range(1,n):
    for j in range(i+1):
        print("*", end=" ")
    for j in range(2*(n-i-1)):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
    
 #======================

n = int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*", end="")
    for j in range(2*(n-i)):
        print(" ", end="")
    for j in range(i,0,-1):
        print("*", end="")
    print()
    
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    for j in range(2*(n-i-1)):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()
    
    
"""
Given integer print spiral matrix
"""

def generateMatrix(A):
    if A <= 0:
        return []
    result = [[None for i in range(A)] for j in range(A)]
    xBeg,xEnd = 0,A-1
    yBeg,yEnd = 0,A-1
    current = 1
    while (True):
        for i in range(yBeg,yEnd+1):
            result[xBeg][i] = current
            current += 1
        xBeg += 1
        if (xBeg > xEnd):
            break
        for i in range(xBeg,xEnd+1):
            result[i][yEnd] = current
            current += 1
        yEnd -= 1
        if (yEnd < yBeg):
            break
        for i in range(yEnd,yBeg-1,-1):
            result[xEnd][i] = current
            current += 1
        xEnd -= 1
        if (xEnd < xBeg):
            break
        for i in range(xEnd,xBeg-1,-1):
            result[i][yBeg] = current
            current += 1
        yBeg += 1
        if (yBeg > yEnd):
            break
    return result
            
A=6
print(generateMatrix(A))              

"""
Given integer print spiral matrix
"""

A = int(input())
for i in range(1, A + 1):
    lo = (i - 1) * A + 1
    hi = (i - 1) * A + A
    p = 1
    if i % 2 == 0:
        temp = lo
        lo = hi
        hi = temp
        p = -1
    
    j = lo
    while True:
        print (j, end = ' ')
        if j == hi:
            break
        j += p
    
    print()
    
"""
Given an integer array A of size N. Return 1 if the array can be rearranged 
to form an arithmetic progression, otherwise, return 0.

A sequence of numbers is called an arithmetic progression if the 
difference between any two consecutive elements is the same.
"""
def arthProg(A):
    n = len(A)
    A.sort()
    print(A)
    ans=[]
    c=1
    for i in range(1, n):
        diff = A[i]- A[i-1]
        ans.append(diff)
    for i in range(1,len(ans)):
        if(ans[i] != ans[i-1]):c=0
    return c

A = [2, 4, 1]
print(arthProg(A))
    
   
        
