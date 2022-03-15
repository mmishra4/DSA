# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:07:52 2022
XOR
@author: MMEENAK4
"""
def exorOp(A):
    ans = 0
    for i in A:
        ans = ans ^ i
    return ans

A=[1, 3, 5]
A = [1, 1, 1]
A = [1, 2, 3, 1, 2, 4]
print(exorOp(A))
        
"""
Created on Thu Jan 27 11:07:52 2022
AND
@author: MMEENAK4
"""
def andOp(A):
    n = len(A)
    k = 0
    ans = 0
    for i in range(n):
        while k <= 4 :
            for j in range(i+1,n):
                ans = max(ans, A[i] & A[j])
                print(ans)
                k += 1
    return ans

A = [10, 20, 15, 4, 14]
print(andOp(A))

20 & 15 & 14 & 10
"""
Given an array of integers A, every element appears twice except for one.
Find that single one.
"""
def singleNumber(A):
    n = len(A)
    a = A[0]
    for i in range(1,n):
        a = a ^ A[i]
    return a

A = [1, 2, 2, 3, 1]
print(singleNumber(A))

"""
Given two binary strings, return their sum (also a binary string).
"""
def addBinary(self, A, B):
        x = A; y = B;
        max_len = max(len(x), len(y))
 
        x = x.zfill(max_len)
        y = y.zfill(max_len)
         
        # initialize the result
        result = ''
         
        # initialize the carry
        carry = 0
 
        # Traverse the string
        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1     # Compute the carry.
         
        if carry !=0 : result = '1' + result
 
        return result.zfill(max_len)
"""
find the element
that occur only once
"""

INT_SIZE = 32
 
def getSingle(A) :
    n = len(A)
    # Initialize result
    result = 0
    ans=[]
    # Iterate through every bit
    for i in range(0, INT_SIZE) :
         
        # Find sum of set bits
        # at ith position in all
        # array elements
        sm = 0
        x = (1 << i)
        print(x)
        for j in range(0, n) :
            if (A[j] & x) :
                sm = sm + 1
        print(x) 
        print(sm)
        # The bits with sum not
        # multiple of 3, are the
        # bits of element with
        # single occurrence.
        if ((sm % 3)!= 0) :
            result = result | x
            ans.append(result)
     
    return ans

A = [1, 2, 3, 1, 2, 4]
print(getSingle(A))  

"""
Given an array of numbers A , in which exactly two elements appear only once
and all the other elements appear exactly twice.
Find the two elements that appear only once.
"""
def UniqueNumbers2(A):
    n = len(A)
    sums = 0
    ans = []
    for i in range(0, n):
 
        # Xor  all the elements of the array
        # all the elements occurring twice will
        # cancel out each other remaining
        # two unique numbers will be xored
        sums = (sums ^ A[i])
 
    # Bitwise & the sum with it's 2's Complement
    # Bitwise & will give us the sum containing
    # only the rightmost set bit
    sums = (sums & -sums)
 
    # sum1 and sum2 will contains 2 unique
    # elements elements initialized with 0 box
    # number xored with 0 is number itself
    sum1 = 0
    sum2 = 0
 
    # Traversing the array again
    for i in range(0, n):
 
        # Bitwise & the arr[i] with the sum
        # Two possibilities either result == 0
        # or result > 0
        if (A[i] & sums) > 0:
 
            # If result > 0 then arr[i] xored
            # with the sum1
            sum1 = (sum1 ^ A[i])
        else:
 
            # If result == 0 then arr[i]
            # xored with sum2
            sum2 = (sum2 ^ A[i])
    
    ans.append(sum1)
    ans.append(sum2)
    ans.sort()
    # Print the the two unique numbers
    #print("The non-repeating elements are ",sum1, " and ", sum2)
    return ans
 
A = [1, 2, 3, 1, 2, 4]
A = [ 186, 256, 102, 377, 186, 377 ]
print(UniqueNumbers2(A))