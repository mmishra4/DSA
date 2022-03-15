# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:29:02 2022

@author: MMEENAK4
"""

def LeadersArray(A):
    N = len(A)
    cnt = 1
    maxi = A[N-1]
    l_a = []
    l_a.append(A[N-1])
    for i in range(N-2, -1, -1):
        if A[i] > maxi:
            maxi = A[i]
            cnt += 1
            l_a.append(A[i])
    return l_a


def CountPairs(A):
    N = len(A)
    cnt = 0
    ans = 0
    for i in range(N-1, -1, -1):
        if A[i] == 'G':
            cnt += 1
        elif A[i] == 'A':
            ans += cnt
    return ans
# Python program to find number switch presses to
# turn all bulbs on.

def AmazingSubStr(A):
    N = len(A)
    s = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cnt = 0
    ans = 0
    for i in range(N-1, -1, -1):
        if A[i] not in s:
            cnt += 1
        elif A[i] in s:
            cnt+=1
            ans += cnt
    ans = ans%10003          
    return ans

#A = "XYZEROS"
A="ABEC"

print(AmazingSubStr(A))

def SubArray(A):
    N=len(A)
    if(A[0]%2 == 0 and A[N-1]%2 == 0 and N%2 == 0):
        return "YES"
    else:
        return "NO"
    
def bulbs(a, n):
    # To keep track of switch presses so far
    count = 0
    res = 0
    for i in range(n):
        # if the bulb's original state is on and count is even,
        # it is currently on...no need to press this switch
        if (a[i] == 1 and count % 2 == 0):
            continue
        # If the bulb's original state is off and count is odd
        # it is currently on...no need to press this switch
        elif(a[i] == 0 and count % 2 != 0):
            continue
        # if the bulb's original state is on and count is odd
        # it is currently off...Press this switch to on the bulb and increase
        # the count
        elif (a[i] == 1 and count % 2 != 0):
            res += 1
            count += 1
        # if the bulb's original state is off and count is even, it is  off...
        # press this switch to on the bulb and increase the count
        elif (a[i] == 0 and count % 2 == 0):
            res += 1
            count += 1
    return res
        
#A = [16, 17, 4, 3, 5, 2]
#A = [1, 2]
#A = [ 93, 57, 83, 41, 100, 10, 79, 27, 94, 22, 4, 96, 48, 18, 89, 37, 21, 5, 46, 81, 15, 30, 47, 23, 34, 65, 55, 9, 36, 20, 54, 17, 7, 56, 78, 84, 87, 97, 16, 69, 28, 11, 44, 49, 8, 25, 98, 75, 53, 62, 19, 24, 80, 68, 50, 91, 1, 86, 77, 14, 72, 66, 42, 63, 73, 45, 31, 61, 85, 64, 35, 32, 92, 71, 74, 3, 99, 52, 90, 43, 6, 40, 38, 2, 12, 59, 29, 82, 76, 60, 67, 13, 70, 58, 39, 33, 95, 88, 51, 26 ]
#print(LeadersArray(A))
    
#A = "ABCGAG"
#A = "GAB"
#print(CountPairs(A))
    
# =============================================================================
# states = [0, 1, 0, 1]
# n = len(states)
# print("The minimum number of switches needed are", bulbs(states, n))
# =============================================================================

#A = "ABEC"
# =============================================================================
# A = "XYZEROS"
# print(AmazingSubStr(A))
# =============================================================================

 #A = [2, 4, 8, 6]
A = [2, 4, 8, 7, 6]
print(SubArray(A))