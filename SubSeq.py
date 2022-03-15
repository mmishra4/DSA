# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:09:22 2022
find that there is any subsequence exists or not whose sum is equal to B.
@author: MMEENAK4
"""
def checkbit(num, i):
    if num & (1<<i):
        return True
    return False


def sumSubSeq(A, B):
    N = len(A)
    A.sort()
    for num in range(1, 2**N):
        cursubset = []
        sum_subseq = 0
        for idx in range(0,N):
            #if checkbit(num, idx):
            #if(num & (1<<idx)):
            if num & (1 << (idx)):
                cursubset.append(A[idx]) 
                sum_subseq += A[idx]
    if sum_subseq == B:
        return True
    return False
                
    
A=[1,20,13,4,5]
B=18
print(sumSubSeq(A, B))

"""
Approach 2
"""

def CheckForSequence(A, B) :
    n = len(A)
    #A.sort()
    # Traverse the array from end
    # to start
    for i in range(n - 1, -1, -1) :
        # if k is greater than
        # arr[i] then subtract
        # it from k
        if (B >= A[i]) :
            B -= A[i];
 
    # If there is any subsequence
    # whose sum is equal to k
    if (B != 0) :
        return False;
    else :
        return True;
    


A = [ 10, 8, 19, 7, 16 ]
B = 23
A=[1,20,13,4,5]
B=18
print(CheckForSequence(A, B))

"""
Odd Even Subsequence
"""
def oddEveSub(A):
    if not A:
        return []
    sln = [A[0]]
    for x in A[1:]:
        if x % 2 != sln[-1] % 2:
            sln.append(x)
    return len(sln)

A = [1,2,2,5,6]
A = [2, 2, 2, 2, 2, 2]
print(oddEveSub(A))

"""
Given a set of distinct integers, A, return all possible subsets.
"""
def printAllSubSet(A):
    n = len(A)
    # Function to find all subsets of given set.
    # Any repeated subset is considered only
    # once in the output
    _list = []
    _list.append([])
    # Run counter i from 000..0 to 111..1
    for i in range(2**n):
        subset = []
        # consider each element in the set
        for j in range(n): 
            # Check if jth bit in the i is set.
            # If the bit is set, we consider
            # jth element from set
            if (i & (1 << j)):
                subset.append(A[j])
 
        # if subset is encountered for the first time
        if subset not in _list and len(subset) > 0:
            _list.append(subset)
    return _list
A = [1, 2, 3]
print(printAllSubSet(A))

"""
Approach 2
"""
def subsets(A):    
    A.sort()
    r = [[]]
    for e in A:
        r += [x + [e] for x in r]
    return sorted(r)
A = [1, 2, 3]
print(subsets(A))

"""
Lexicographically smallest subsequence
"""
def smallestSubsequence(S, K):
   
    # Length of string
    N = len(S)
 
    # Stores the minimum subsequence
    answer = []
 
    # Traverse the string S
    for i in range(N):
       
        # If the stack is empty
        if (len(answer) == 0):
            answer.append(S[i])
        else:
           
            # Iterate till the current
            # character is less than the
            # the character at the top of stack
            while (len(answer) > 0 and (S[i] < answer[len(answer) - 1]) and (len(answer) - 1 + N - i >= K)):
                answer = answer[:-1]
 
            # If stack size is < K
            if (len(answer) == 0 or len(answer) < K):
               
                # Push the current
                # character into it
                answer.append(S[i])
 
    # Stores the resultant string
    ret = []
 
    # Iterate until stack is empty
    while (len(answer) > 0):
        ret.append(answer[len(answer) - 1])
        answer = answer[:-1]
 
    # Reverse the string
    ret = ret[::-1]
    ret = ''.join(ret)
     
    return(ret)
 

S = "aabdaabc"
K = 3
S = "ksdjgha"
K = 2
smallestSubsequence(S, K)


"""
Max Sum - Min SUM
"""

  
# function for sum of max min difference 
def maxMin (A):
    MOD = 1000000007;
    n = len(A)
    # sort all numbers
    A.sort()
      
    # iterate over array and with help of 
    # horner's rule calc max_sum and min_sum
    min_sum = 0
    max_sum = 0
    for i in range(0,n):
          
        max_sum = 2 * max_sum + A[n-1-i];
        max_sum %= MOD;
        min_sum = 2 * min_sum + A[i];
        min_sum %= MOD;
      
    return (max_sum - min_sum + MOD) % MOD;

A = [1,2]    
print(maxMin(A))


"""
Value of a subarray is defined as BITWISE OR of all elements in it.

Return the sum of Value of all subarrays of A % 109 + 7.
"""

def totalSum(a, n):
    sum = 0;
    for i in range(n):
        sum1 = 0;
         
        # perform Bitwise OR operation
        # on all the subarray present
        # in array
        for j in range(i, n):
             
            # OR operation
            sum1 = (sum1 | a[j]);
             
            # now add the sum after
            # performing the
            # Bitwise OR operation
            sum = sum + sum1;
    return sum;
 
# Driver code
a = [1, 2, 3, 4, 5];
n = len(a);
print(totalSum(a, n));

"""
Approach 2
"""
def cnt(n):
    return (n * (n + 1)) // 2


def solve(A):
    MOD = int(1e9 + 7)
    ans = 0
    n = len(A)
    for b in range(27):
        c = 0
        C = cnt(n)
        for i in range(n):
            if A[i] & 1:
                C -= cnt(c)
                c = 0
            else:
                c += 1
            A[i] >>= 1
        C -= cnt(c)
        ans = (ans + (1 << b) * C) % MOD
    return ans

a = [1, 2, 3, 4, 5];
print(solve(a));

def OR(a, n):     
    ans = a[0]
    sum = []
    for i in range(1,n):
        ans |= a[i]
        sum.append(ans)     
    return sum
a = [1, 2, 3, 4, 5];
n = len(a);
print(OR(a, n));


from math import log2
 
# Function to find sum of bitwise OR
# of all subarrays
def givesum(A, n) :
 
    # Find max element of the array
    max_element = max(A)
 
    # Find the max bit position set in
    # the array
    maxBit = int(log2(max_element)) + 1
 
    totalSubarrays = n * (n + 1) // 2
 
    s = 0
 
    # Traverse from 1st bit to last bit which
    # can be set in any element of the array
    for i in range(maxBit) :
        c1 = 0
 
        # List to store indexes of the array
        # with i-th bit not set
        vec = []
 
        sum = 0
 
        # Traverse the array
        for j in range(n) :
 
            # Check if ith bit is not set in A[j]
            a = A[j] >> i
             
            if (not(a & 1)) :
                vec.append(j)
 
        # Variable to store count of subarrays
        # whose bitwise OR will have i-th bit
        # not set
        cntSubarrNotSet = 0
 
        cnt = 1
 
        for j in range(1, len(vec)) :
             
            if (vec[j] - vec[j - 1] == 1) :
                cnt += 1
             
            else :
                 
                cntSubarrNotSet += cnt * (cnt + 1) // 2
 
                cnt = 1
             
        # For last element of vec
        cntSubarrNotSet += cnt * (cnt + 1) // 2
 
        # If vec is empty then cntSubarrNotSet
        # should be 0 and not 1
        if len(vec) == 0:
            cntSubarrNotSet = 0   
 
        # Variable to store count of subarrays
        # whose bitwise OR will have i-th bit set
        cntSubarrIthSet = totalSubarrays - cntSubarrNotSet
 
        s += cntSubarrIthSet * pow(2, i)
     
    return s
a = [1, 2, 3, 4, 5];
n = len(a);
print(givesum(a, n)); 