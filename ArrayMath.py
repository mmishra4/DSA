# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 15:57:31 2022
Given an array of size n, find the majority element. 
The majority element is the element that appears more than floor(n/2) times.
@author: MMEENAK4
"""
def majorityElement(A):
    n = len(A)
    maj = A[0]; cnt = 1;
    for i in range(1,n):
        if(A[i] == maj):
            cnt += 1
        elif (cnt == 0):
            maj = A[i]; cnt =1
        else:
            cnt -= 1
            
    for i in range(n):
        if A[i] == maj:
            cnt += 1
    
    if cnt > n/2 :         
        return maj
    else:
        return 0

"""

"""

 
def appearsNBy3(A):
    import sys
    n=len(A)
    count1 = 0
    count2 = 0
    first = sys.maxsize
    second = sys.maxsize
 
    for i in range(0, n): 
        # if this element is previously seen, increment count1.
        if (first == A[i]):
            count1 += 1 
        # if this element is previously seen, increment count2.
        elif (second == A[i]):
            count2 += 1     
        elif (count1 == 0):
            count1 += 1
            first = A[i] 
        elif (count2 == 0):
            count2 += 1
            second = A[i]
        # if current element is different from both
        # the previously seen variables, decrement both the counts.
        else:
            count1 -= 1
            count2 -= 1
    count1 = 0
    count2 = 0
    # Again traverse the array
    # and find the actual counts.
    for i in range(0, n):
        if (A[i] == first):
            count1 += 1 
        elif (A[i] == second):
            count2 += 1
     
 
    if (count1 > n / 3):
        return first 
    if (count2 > n / 3):
        return second
 
    return -1

A=[1,1,1,4,2,5]
print(appearsNBy3(A))

"""
Given an integer A, find and return the Ath magic number.

A magic number is defined as a number which can be expressed as a 
power of 5 or sum of unique powers of 5.

First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….
"""

def nthMagicNo(A): 
    pow = 1
    answer = 0 
    # Go through every bit of n
    while (A): 
        pow = pow*5 
        # If last bit of n is set
        if (A & 1):
            answer += pow 
        # proceed to next bit
        A >>= 1 # or n = n/2     
    return answer
A = 13
print(nthMagicNo(A))


"""
Given an integer array A, find if an integer p exists in the array 
such that the number of integers greater than p in the array equals to p.
"""

def nobleInt(A):
    A.sort(reverse=True)
    c=0; res=0; 
    if (A[0]==0): 
        res = 1;
    for i in range(1,len(A)):
        if(A[i] != A[i-1]):c=i
        if c == A[i]:res+=1
    if res==0: 
        res=-1
    else: 
        res=1
    return res

A = [3,1,2,3]
print(nobleInt(A))

"""
Min cost to remove element from Array
"""
"""
Given an integer array A, find if an integer p exists in the array 
such that the number of integers greater than p in the array equals to p.
"""

def minCost(A):
    A.sort(reverse=True)  
    cost = 0
    while(len(A) > 0): 
        for i in range(len(A)):
            cost += A[i]
        A.remove(A[0])     
    return cost

A = [4,6,1]
print(minCost(A))

"""
sort array 
"""

def sortColor(A):
    n = len(A)
    lo = 0
    hi = n - 1
    mid = 0
    while mid <= hi:
        if A[mid] == 0:
            A[lo], A[mid] = A[mid], A[lo]
            lo = lo + 1
            mid = mid + 1
        elif A[mid] == 1:
            mid = mid + 1
        else:
            A[mid], A[hi] = A[hi], A[mid]
            hi = hi - 1
    return A

A = [0,1,2,0,1,2]            
print(sortColor(A))

"""
Largest number from array of integers
"""

from functools import cmp_to_key
from functools import cmp

def factors(num):
  cnt = 0
  for i in range(1, num + 1):
    if num % i == 0:
      cnt += 1
  return cnt

# x is the first num
def my_cmp(x, y):
  c1 = factors(x)
  c2 = factors(y)
  if c1 < c2:
    return -1 # comment x should be y
  if c2 < c1:
    return 1 # comment: y should come before x
  # c1 = c2
  # smaller element should come before
  if x < y:
    return -1
  if y < x:
    return 1
  return 0 # both are equal

l = [3, 30, 34, 5, 9]


# l.sort()
# l.sort(key=factors)

l.sort(key=cmp_to_key(my_cmp))
print(l)
s = [str(i) for i in l]
  
# Join list items using join()
res = int("".join(s))
print(res)  
return(res)

print(l)


from itertools import permutations
def largest(l):
    lst = []
    for i in permutations(l, len(l)):
        # provides all permutations of the list values,
        # store them in list to find max
        lst.append("".join(map(str,i)))
    return max(lst)
 
A=[54, 546, 548, 60]
print(largest(A)) #Output 6054854654
 
def my_cmp(x,y):
    sx = str(x)
    sy = str(y)
    sx = sx + sy
    sy = sy + sx
    if sx > sy:
        return -1
    if sx == sy:
        return 0
    if sx < sy:
        return 1
    
def largestNumber(A):
    #A = sorted(A, cmp=my_cmp)
    A.sort(key=cmp_to_key(my_cmp))
    
    if A[0] == 0:
        return "0"
    else:
        return "".join([str(n) for n in A])
                       
A=[54, 546, 548, 60]
print(largestNumber(A))               

        
    
    
    
            
            
        
        
    








