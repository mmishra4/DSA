# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:43:00 2022
Given an array of positive integers A and an integer B, 
find and return first continuous subarray which adds to B.
@author: MMEENAK4
"""
def subArraySum(A, B):
    n = len(A)
    curr_sum = A[0]
    start = 0
    ans = []
    i = 1
    while i <= n:         
        # If curr_sum exceeds the sum, then remove the starting elements
        while curr_sum > B and start < i-1:
         
            curr_sum = curr_sum - A[start]
            start += 1
            
        # If curr_sum becomes equal to sum, then return true
        if curr_sum == B:
            ans = A[start: i]
            return ans
 
        # Add this element to curr_sum
        if i < n:
            curr_sum = curr_sum + A[i]
        i += 1
 
    return -1
 
A = [ 5, 10, 20, 100, 105 ]
B = 120
print(subArraySum(A, B))

"""
Sum of all elements repeating ‘k’ times in an array
"""
import math as mt
 
# Returns Sum of k appearing elements.
def sumKRepeating(A, B, C):
    Sum = 0
    flag = False
    # Count frequencies of all items
    mp = dict()
    for i in range(A):
        if C[i] in mp.keys():
            mp[C[i]] += 1
        else:
            mp[C[i]] = 1                 
    # Sum items with frequencies equal to k.
    for x in mp:
        if (mp[x] == B):
            flag = True
            Sum += x
    if flag:
        return Sum
    return -1

A=5; B=2; C=[1, 2, 2, 3, 3];
A=3; B=2; C=[ 0, 0, 1 ]
print(sumKRepeating(A, B, C))

"""
You are given an array of N integers, A1, A2 ,…, AN and an integer B. 
Return the of count of distinct numbers in all windows of size B.
"""

from collections import defaultdict  
def countDistinct(A, B):
    n = len(A)
    mp = defaultdict(lambda:0)
    dist_count = 0
    ans = []
    # Traverse the first window and store count 
    # of every element in hash map 
    for i in range(B):
        if mp[A[i]] == 0:
            dist_count += 1
        mp[A[i]] += 1
    ans.append(len(mp))
        
    # Traverse through the remaining array 
    for i in range(B, n):  
        # Remove first element of previous window 
        # If there was only one occurrence, then reduce distinct count. 
        if mp[A[i - B]] == 1:
            dist_count -= 1
        mp[A[i - B]] -= 1
      
    # Add new element of current window If this element appears first time, 
    # increment distinct element count 
        if mp[A[i]] == 0:
            dist_count += 1
        mp[A[i]] += 1
        ans.append(len(mp))
     
    return ans
  
A = [1, 2, 1, 3, 4, 2, 3]
B = 4
print(countDistinct(A,B))

def distCnt(A,B):
    N = len(A)
    freq_dict = {}
    ans = []
    for i in range(B):
        if A[i] in freq_dict:
            freq_dict[A[i]] += 1
        else:
            freq_dict[A[i]] = 1
    ans.append(len(freq_dict))
    
    for i in range(B,N):
        if A[i] in freq_dict:
            freq_dict[A[i]] += 1
        else:
            freq_dict[A[i]] = 1
    
        freq_dict[A[i-B]] -= 1
        
        if freq_dict[A[i-B]] == 0:
            #del 
            

"""
Approach 3
"""

def findDistinctCount(A, k):
    ans = []
    # loop through the list
    for i in range(len(A) - (k - 1)):
        distinct = set(A[i:i+k])
        ans.append(len(distinct))
    return ans

A = [2, 1, 2, 3, 2, 1, 4, 5]
B = 5
print(countDistinct(A,B))

"""
Longest consecutive subsequence
"""
# Function to find the length of the largest subsequence formed by consecutive integers
def findMaxLenSubseq(A):
 
    # construct a set out of input elements
    S = set(A)
 
    # initialize result by 0
    maxlength = 0 
    # do for each element of the input sequence
    for e in A: 
        # check if the current element `e` is a candidate for starting a sequence;
        # i.e., the previous element `e-1` doesn't exist in the set
        if (e - 1) not in S: 
            # `len` stores the length of subsequence, starting with the current element
            len = 1 
            # check for presence of elements `e+1`, `e+2`, `e+3`, … ,`e+len` in the set
            while (e + len) in S:
                len += 1
 
            # update result with the length of current consecutive subsequence
            maxlength = max(maxlength, len)
 
    # return result
    return maxlength

A = [100, 4, 200, 1, 3, 2]
print(findMaxLenSubseq(A))

"""
Given an array A of integers and another non negative integer k, 
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
"""
def diffPossible(self, A, B):
        hashDict = dict()
        n = len(A)
        #print A, B
        for a in A:
            if a in hashDict:
                hashDict[a] += 1
            else:
                hashDict[a] = 1
        for i in range(n):
            x = A[i]
            if (x - B >= 0 and x - B in hashDict) or (x+B in hashDict):
                if B == 0:
                    if hashDict[x] >= 2:
                        return 1
                else:
                    return 1
            elif x+B in hashDict:
                return 1
            elif x in hashDict:
                del hashDict[x]
        #print hashDict
        return 0

"""
Longest consecutive subsequence
"""
 
def longestConsecutive(A):
    longest_streak = 0
    num_set = set(A)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

A = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(A))

"""
# Returns count of pairs in arr[0..n-1]
# with XOR value equals to x.
"""
def xorPairCount(A, B):
    n = len(A)
    result = 0 # Initialize result
 
    # create empty map that stores counts
    # of individual elements of array.
    m = dict()
 
    for i in range(n):
     
        curr_xor = B ^ A[i]
 
        # If there exist an element in map m
        # with XOR equals to x^arr[i], that
        # means there exist an element such that
        # the XOR of element with arr[i] is equal
        # to x, then increment count.
        if (curr_xor in m.keys()):
            result += m[curr_xor]
 
        # Increment count of current element
        if A[i] in m.keys():
            m[A[i]] += 1
        else:
            m[A[i]] = 1
     
    # return total count of pairs
    # with XOR equal to x
    return result
 
# Driver Code
A = [2, 5, 2]
B = 0
A = [3, 6, 8, 10, 15, 50]
B = 5
print("Count of pairs with given XOR = ",xorPairCount(A, B))

"""
# Function to check whether Words are sorted in given Order
"""
def isAlienSorted(A, B):
    Order_index = {c: i for i, c in enumerate(B)}
  
    for i in range(len(A) - 1):
        word1 = A[i]
        word2 = A[i + 1]
  
        # Find the first difference word1[k] != word2[k].
        for k in range(min(len(word1), len(word2))):
  
            # If they compare false then it's not sorted.
            if word1[k] != word2[k]:
                if Order_index[word1[k]] > Order_index[word2[k]]:
                    return False
                break
        else:
  
            # If we didn't find a first difference, the
            # Words are like ("add", "addition").
            if len(word1) > len(word2):
                return False
  
    return True
  
  
# Program Code
A = ["hello", "leetcode"]
B = "habcldefgijkmnopqrstuvwxyz"
  
# Function call to print required answer
print(isAlienSorted(A, B))

"""
check whether
# given sudoku board is valid or not
"""
# Checks whether there is any
# duplicate in current row or not
def notInRow(arr, row):
 
    # Set to store characters seen so far.
    st = set()
 
    for i in range(0, 9):
 
        # If already encountered before,
        # return false
        if arr[row][i] in st:
            return False
 
        # If it is not an empty cell, insert value
        # at the current cell in the set
        if arr[row][i] != '.':
            st.add(arr[row][i])
     
    return True
 
# Checks whether there is any
# duplicate in current column or not.
def notInCol(arr, col):
 
    st = set()
 
    for i in range(0, 9):
 
        # If already encountered before,
        # return false
        if arr[i][col] in st:
            return False
 
        # If it is not an empty cell, insert
        # value at the current cell in the set
        if arr[i][col] != '.':
            st.add(arr[i][col])
     
    return True
 
# Checks whether there is any duplicate
# in current 3x3 box or not.
def notInBox(arr, startRow, startCol):
 
    st = set()
 
    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]
 
            # If already encountered before,
            # return false
            if curr in st:
                return False
 
            # If it is not an empty cell,
            # insert value at current cell in set
            if curr != '.':
                st.add(curr)
         
    return True
 
# Checks whether current row and current
# column and current 3x3 box is valid or not
def isValid(arr, row, col):
 
    return (notInRow(arr, row) and notInCol(arr, col) and
            notInBox(arr, row - row % 3, col - col % 3))
 
def isValidConfig(A): 
    n = 9
    for i in range(0, n):
        for j in range(0, n): 
            # If current row or current column or
            # current 3x3 box is not valid, return false
            if not isValid(A, i, j):
                return 0                    
    return 1

board = [[ '5', '3', '.', '.', '7', '.', '.', '.', '.' ],
             [ '6', '.', '.', '1', '9', '5', '.', '.', '.' ],
             [ '.', '9', '8', '.', '.', '.', '.', '6', '.' ],
             [ '8', '.', '.', '.', '6', '.', '.', '.', '3' ],
             [ '4', '.', '.', '8', '.', '3', '.', '.', '1' ],
             [ '7', '.', '.', '.', '2', '.', '.', '.', '6' ],
             [ '.', '6', '.', '.', '.', '.', '2', '8', '.' ],
             [ '.', '.', '.', '4', '1', '9', '.', '.', '5' ],
             [ '.', '.', '.', '.', '8', '.', '.', '7', '9' ]]
print(isValidConfig(board))