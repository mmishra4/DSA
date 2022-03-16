# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:18:22 2022
Minimum Picks
Prob: Given array of integers A of Size N
Return the difference between the maximum among all even numbers of A and the minimum among all odd number in A

Return maximum amoong all even numbers of A - minimum among all odd numbers in A

A=[0,2,9]
o/p:-7
A=[5,17,100,1]
o/p:99
@author: MMEENAK4
"""

def diffMinMax(A):
    maxE = 0
    minO = 0
    eve = []
    odd = []
    for i in A:
        if i%2==0:
            eve.append(i)
        else:
            odd.append(i)
    maxE = max(eve)
    minO = min(odd)
    return maxE-minO

A=[0,2,9]
print(diffMinMax(A))
            
        

