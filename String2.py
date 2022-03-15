# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:32:36 2022
Find number of occurrences of bob in the string A 
consisting of lowercase english alphabets.
@author: MMEENAK4
"""

def findBob(A):
    cnt = 0
    n = len(A)
    for i in range(n-2):
         if(A[i] == 'b' and A[i+1] == 'o' and A[i+2] == 'b'):
             cnt += 1
    return cnt

A = "abobc"
print(findBob(A))

"""
First concatenate the string with itself so string A becomes "AbcaZeoBAbcaZeoB".
Delete all the uppercase letters so string A becomes "bcaeobcaeo".
Now replace vowel with '#'.
A becomes "bc###bc###".
"""

def concatString(A):
    n = len(A)
    s = ""
    for i in range(n):
         if(ord(A[i]) >= 65 and ord(A[i]) <= 90):
             x = ""
         elif(A[i] in ('a','e','i', 'o','u')):
             s += '#'
         else:
             s += A[i]
    return s+s
 
A = "AbcaZeoB"
print(concatString(A))