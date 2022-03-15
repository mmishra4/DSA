# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 04:49:30 2022
Modulo of string
@author: MMEENAK4
"""

def mod(A,B):
    ans=0
    coefficient = 1
    for i in reversed(range(len(A))):
        d = int(A[i])
        ans = (ans + ((d % B) * coefficient ) % B ) % B
        coefficient = (coefficient*10) % B
    return ans

A = "143"
B = 2
A = "43535321"
B = 47
print(mod(A,B))

"""
Whether number is divible by 8
"""

def divby8(A):
    n = len(A)
    # Empty string
    if (n == 0) :
        return 0
 
    # If there is single digit
    if (n == 1) :
        if ((int)(A[0]) % 8 == 0):
            return 1
        else:
            return 0
 
    # If there is double digit
    if (n == 2) :
        if ((int)(A[n - 2]) * 10 + ((int)(A[n - 1]) % 8 == 0)):
            return 1
        else:
            return 0
 
    # If number formed by last
    # three digits is divisible
    # by 8.
    last = (int)(A[n - 1])
    second_last = (int)(A[n - 2])
    third_last = (int)(A[n - 3])
 
    if ((third_last*100 + second_last*10 +
                               last) % 8 == 0):
        return 1
    else:
        return 0

A = "17"
print(diveby81(A))

A="17"
n=len(A)
one = int(A[n-1])
ten = int(A[n-2])
ans = (ten*10 + one)%8
print(ans)

def diveby81(A):

    n = len(A)
    ans = 1 
    # Empty string
    if (n == 0) :
        ans = 1
 
    # If there is single digit
    if (n == 1) :
        ans = (int(A[0])) % 8 
 
    # If there is double digit
    if (n == 2) :
        one = int(A[n-1])
        ten = int(A[n-2])
        ans = (ten*10 + one)%8
        
       
 
    # If number formed by last
    # three digits is divisible
    # by 8.
    if(n>2):
        last = (int)(A[n - 1])
        second_last = (int)(A[n - 2])
        third_last = (int)(A[n - 3])
     
        ans =  ((third_last*100 + second_last*10 +
                                   last) % 8 )
    if(ans == 0):
        return 1
    else:
        return 0
        