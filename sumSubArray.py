# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:16:24 2022

@author: MMEENAK4
"""

def sumSubArray(A):
    n = len(A)
    B = 0 
    C = []  
    for start in range (n):
        sum = 0
        for end in range (start , n):
            sum += A[end]
            #print(f" Sum of array A[[start][end]]", sum)
            B += sum
            C.append(sum)
            
    print(C)
    print(max(C))
    return B  

#optimized solution

def sumAllSubArrays(A):
    n=len(A)
    B = 0
    C = []
    for i in range(n):
        B += (A[i] * (i+1) * (n-i))
        C.append(B)
    #print(B)
    #print(C)
    return (int)(B % (1e9 + 7))
A = [1, 2, 3, 4, 5]
print(sumAllSubArrays(A))



 
def maxSubArraySum(A):
    from sys import maxsize
    size = len(A)
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(0,size):
        max_ending_here += A[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1     
    return max_so_far

def maxCSubArraySum(A,B,C):    
    max_so_far =C[0]
    curr_max = C[0]    
    for i in range(1,A):
        if curr_max <= B:
            curr_max = max(C[i], curr_max + C[i])
            max_so_far = max(max_so_far,curr_max)  
            print(curr_max, max_so_far)
    return max_so_far

def lstAvgSubArray(A,B):
    n = len(A)
    C = []  
    for i in range (n):
        sum = 0
        if i <= n-B:
            #print(i)
            for j in range (i , i+B):
                sum += A[j]
                #print(f" Sum of array A[[start][end]]", sum)        
            C.append(sum)         
    #print(C)
    return(C.index(min(C)))
    
def findMinAvgSubarray(A,B):
    n = len(A)
    # k must be smaller than or equal to n
    if (n < B): return 0
 
    # Initialize beginning index of result
    res_index = 0
 
    # Compute sum of first subarray of size k
    curr_sum = 0
    for i in range(B):
        curr_sum += A[i]
 
    # Initialize minimum sum as current sum
    min_sum = curr_sum
 
    # Traverse from (k + 1)'th
    # element to n'th element
    for i in range(B, n):
     
        # Add current item and remove first
        # item of previous subarray
        curr_sum += A[i] - A[i-B]
 
        # Update result if needed
        if (curr_sum < min_sum):
         
            min_sum = curr_sum
            res_index = (i - B + 1)
    return res_index    
    #print("Subarray between [", res_index, ", ", (res_index + B - 1), "] has minimum average")
#A = [1, 2, 3]
#A = [2, 1, 3]
#A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
#A = [1, 2, 3, 4, -10]
#sumSubArray(A)
#sumAllSubArrays(A)
#print(maxSubArraySum(A)) 
#A=[3, 7, 90, 20, 10, 50, 40]
#k=3
#A=[3, 7, 5, 20, -10, 0, 12]
#k=2
A = [ 18, 11, 16, 19, 11, 9, 8, 15, 3, 10, 9, 20, 1, 19 ]
B = 1
A = [ 15, 7, 11, 7, 9, 8, 18, 1, 16, 18, 6, 1, 1, 4, 18 ]
B = 6
findMinAvgSubarray(A,B)

A = 5
B = 12
C = [2, 1, 3, 4, 5]

maxCSubArraySum(A, B, C)


    