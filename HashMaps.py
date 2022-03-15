# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:21:58 2022
Given an integer array A of size N, find the first repeating element in it.
@author: MMEENAK4
"""

def printFirstRepeating(A): 
    n = len(A)
    # Initialize index of first repeating element
    Min = -1 
    # Creates an empty hashset
    myset = dict() 
    # Traverse the input array from right to left
    for i in range(n - 1, -1, -1):     
        # If element is already in hash set,update Min
        if A[i] in myset.keys():
            Min = A[i]
        else: # Else add element to hash set
            #myset.__setitem__(A[i],i)
            myset[A[i]] = 1
    #print(myset)
    return Min

A = [10, 5, 3, 4, 3, 5, 6]
#A = [6, 10, 5, 4, 9, 120]
print(printFirstRepeating(A))

"""
Given two integer array A and B of size N and M respectively. 
Your task is to find all the common elements in both the array.

NOTE:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""
def printIntersection(A, B):
    m = len(A); n = len(B);
    i, j = 0, 0
    ans = []
    A.sort(); B.sort()
    while i < m and j < n:
        if A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j+= 1
        else:
            #print(B[j],end=" ")
            ans.append(B[j])
            j += 1
            i += 1
    return ans
 
# Driver program to test above function
A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
 A = [2, 1, 4, 10]
 B = [3, 6, 2, 10, 10]
print(printIntersection(A,B))

"""
Given an array of integers A, find and return 
whether the given array contains a non-empty subarray with a sum equal to 0.
"""
def subArrayZeroSum(A):
    # traverse through array and store prefix sums
    n = len(A)
    n_sum = 0
    s = set()
 
    for i in range(n):
        n_sum += A[i]
 
        # If prefix sum is 0 or
        # it is already present
        if n_sum == 0 or n_sum in s:
            return 1
        s.add(n_sum)
 
    return 0

A = [1, 2, 3, 4, 5]
A = [-1, 1]
print(subArrayZeroSum(A))

"""
Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array as a special pair if elements at that index in the array are equal.

Shaggy wants you to find a special pair such that distance between that pair is minimum. 
Distance between two indices is defined as |i-j|.
 If there is no special pair in the array then return -1.
"""
def minimumDistance(A): 
    # Create a HashMap to store (key, values) pair.
    hmap = dict()
    minDistance = 10**9; previousIndex = 0
    currentIndex = 0
 
    # Traverse the array and  find the minimum distance
    # between the same elements with map
    for i in range(len(A)): 
        if A[i] in hmap:
            currentIndex = i
 
            # Fetch the previous index from map.
            previousIndex = hmap[A[i]] 
            # Find the minimum distance.
            minDistance = min((currentIndex -
                        previousIndex), minDistance) 
        # Update the map.
        hmap[A[i]] = i
 
    # return minimum distance, if no such elements found, return -1
    if minDistance == 10**9:
        return -1
    return minDistance

A = [7, 1, 3, 4, 1, 7]
print(minimumDistance(A))

"""
Find the largest continuous sequence in a array which sums to zero.
"""

def maxLen(A):
     
    # NOTE: Dictonary in python in implemented as Hash Maps
    # Create an empty hash map (dictionary)
    hash_map = {}; max_len = 0; curr_sum = 0 
    # Traverse through the given array
    for i in range(len(A)):         
        # Add the current element to the sum
        curr_sum += A[i] 
        if A[i] is 0 and max_len is 0:
            max_len = 1
 
        if curr_sum is 0:
            max_len = i + 1
 
        # NOTE: 'in' operation in dictionary to search
        # key takes O(1). Look if current sum is seen
        # before
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum] )
        else: 
            # else put this sum in dictionary
            hash_map[curr_sum] = i
    print(hash_map)
    return max_len

A = [1,2,-2,4,-4]
print(maxLen(A))

"""
Given an array A of N integers.

Find the largest continuous sequence in a array which sums to zero.
"""
def lszero(A):    
    start_index = -1
    first_with_sum = {}
    first_with_sum[0] = -1
    best_start = -1
    best_len = 0
    current_sum = 0
    for i in A:
        start_index += 1
        current_sum += i
        if current_sum in first_with_sum:
            if start_index - first_with_sum[current_sum] > best_len:
                best_start = first_with_sum[current_sum] + 1
                best_len = start_index - first_with_sum[current_sum]
        else:
            first_with_sum[current_sum] = start_index

    if best_len > 0:
        return A[best_start:best_start+best_len]
    else:
        return []


A = [ -19, 8, 2, -8, 19, 5, -2, -23 ]
#A = [1,2,-2,4,-4]
print(lszero(A))

"""
Check if characters of the given string can be rearranged to form a palindrome.
"""
def canFormPalindrome(A):
    ans = []
    # remove character if ans contains else add character to ans
    for i in range(len(A)):
        if (A[i] in ans):
            ans.remove(A[i])
        else:
            ans.append(A[i])
 
    # if character length is even list is expected to be empty
    # or if character length is odd listt size is expected to be 1
    if (len(A) % 2 == 0 and len(ans) == 0 or
            (len(A) % 2 == 1 and len(ans) == 1)):
        return 1
    else:
        return 0
    
A = "abbaee"
print(canFormPalindrome(A))

"""
Approach 2 bit
it is sufficient to keep track if the counts are odd or even.
"""

def isPalindrome(A):
    bitvector = 0
    for char in A:
        bitvector ^= 1 << ord(char)
    print(bitvector)
    return bitvector == 0 or bitvector & (bitvector - 1) == 0
 
A = "abbaee"
print(isPalindrome(A))


"""
Colorful number
"""
def isColorful(A):
    s = ""
    while (A):
        s += chr(A % 10 + ord('0'))
        A //= 10
 
    # Reverse the string to get the original number
    s = s[::-1] 
    # Store size of the string
    sz = len(s)
    se = []
 
    # Find product of every contiguous subsequence
    for i in range(sz):
        product = 1
        for j in range(i, sz, 1):
            product *= ord(s[j]) - ord('0')
            
            # If current product already
            # exists in the set
            for p in range(len(se)):
                if se[p] == product:
                    return 0
                else:
                    se.append(product) 
                    return 1
            
A = 236
print(isColorful(A))

"""
Approach 2
"""
def colorful(A):
    numbers = dict()
    strA = str(A)
    for a in strA:
        if a in numbers:
            return 0
        else:
            numbers[a] = 1
    n = len(strA)
    for i in range(2, n + 1):
        for j in range(n - i + 1):
            num = strA[j : j + i]
            ret = findProd(num)
            if ret in numbers:
                return 0
            else:
                numbers[ret] = 1
    return 1