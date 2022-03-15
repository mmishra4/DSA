# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:02:28 2022
Leap Year
@author: MMEENAK4
"""

def checkLeap(A):
    n = len(str(A))
    
    if(n<4 or n>4):
        return 0
    
    if n==4 :
        if (A % 400 == 0) and (A % 100 == 0):
            return 1
        elif (A % 4 ==0) and (A % 100 != 0):
            return 1
        else:
            return 0
    
        
A=400
print(checkLeap(A))        

"""
Find minimum number
"""

def minNum(A, B, C):
    arr = [A, B, C]
    arr.sort()
    return(arr[0]*10000+arr[1]*100+arr[2])
 
A = 11; B= 44; C=22;
print(minNum(A,B,C)) 

"""
Rectangles ovelap
"""

def isRectangleOverlap(A, B, C, D, E, F, G, H):
    if(A>=G or C<=E or D<=F or B>= H):
        return 0
    else:
        return 1

A = 0;   B = 0;
C = 4;   D = 4;
E = 2;   F = 2;
G = 6;   H = 6;

print(isRectangleOverlap(A, B, C, D, E, F, G, H))

"""
Find LCM
"""
def compute_lcm(A, B):

   # choose the greater number
   if A > B:
       greater = A
   else:
       greater = B

   while(True):
       if((greater % A == 0) and (greater % B == 0)):
           lcm = greater
           break
       greater += 1
       print(greater)

   return lcm

A = 9
B = 6
print(compute_lcm(A,B))
"""
Python program to return title to result
# of excel sheet.
 
# Returns result when we pass title.
"""
def xltitleToNumber(A):
    # This process is similar to binary-to-
    # decimal conversion
    result = 0;
    for B in range(len(A)):
        result *= 26;
        result += ord(A[B]) - ord('A') + 1;
 
    return result;

A = "ABCD"
print(xltitleToNumber(A))

"""
Given two integers A and B, find the greatest possible positive M, 
such that A % M = B % M.
"""

def equalMod(A,B):
    if A>B:
        return (A-B)
    else:
        return (B-A)

A = 1
B = 2
print(equalMod(A,B))