# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:02:04 2022
Given a string A of size N.

Return the string A after reversing the string word by word.
@author: MMEENAK4
"""
def reverse(s):
    s = s[::-1]
    return s

s="god"
print(reverse(s))

def reverseSubstring(s, start, end):
    s = list(s)
    while(start < end):
        s[start], s[end] = s[end], s[start]
        start+=1; end-=1
    return "".join(s)
    
s="mean"
print(reverseSubstring(s,0,3))


def reverseString1(str):
    str = str.strip()
    words = str.split(' ')
    string =[]
    for word in words:
        string.insert(0, word)
    return " ".join(string)
            
s="god is "
print(reverseString1(s))   

def solve(str):
    str = str.strip()
    str = str.split()
    str = str[::-1]
    return ' '.join(str)    
  
s="god is "
print(solve(s))    

"""
tolower case
"""

def toLowerCase(A):
    ans = ""
    for i in A:
        #ans += 32 ^ i
        if(ord(i) >= 65 and ord(i) <= 90):
            new_ascii = ord(i)+32
            ans += chr(new_ascii)
        else:
            ans += i
        
    return ' '.join(ans)

A = ['S', 'c', 'A']
print(toLowerCase(A))

"""
to upper case
"""

def toUpperCase(A):    
    ans = [x.upper() for x in A]
    return ans

A = ['s', 'c', 'A']
print(toUpperCase(A))

def isalpha(A):
    ans = 1
    for i in A:
        if((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)
        or (ord(i) >= 48 and ord(i) <= 57)):
            s = False
        else:
            ans = 0
    return ans

A = ['S', 'c', 'a', 'l', 'e', 'r', '2', '0', '2', '0']
print(isalpha(A))
 
"""
toggle case
"""
"""
tolower case
"""

def toggleCase(A):
    ans = ""
    for i in A:
        #ans += 32 ^ i
        if(ord(i) >= 65 and ord(i) <= 90):
            new_ascii = ord(i)+32
            ans += chr(new_ascii)
        elif(ord(i) >= 97 and ord(i) <= 122):
            new_ascii = ord(i)-32
            ans += chr(new_ascii)
        
    return ' '.join(ans)

A = ['S', 'c', 'A']
print(toggleCase(A))

"""
check Palindrome
"""
def isPalindrome(A):
    n = len(A)
    for i in range(n//2):
        if A[i] != A[n-i-1]:
            return 0
    return 1

A = "abba"
print(isPalindrome(A))

"""
Given a string A of size N,
find and return the longest palindromic size in A.
"""
def expand1(s, start, end):
    n = len(s)
    while(start>=0 and end<n and s[start] == s[end]):
        start -= 1; end += 1;
    return end-start-1
    #return s[start+1:end]

def longestPalin(A):
    maxi = 1
    for i in range(1,len(A)):
        maxi = max(maxi, expand1(A, i, i)) #odd length
        maxi = max(maxi, expand1(A, i, i+1)) #even length
    return maxi


A = "aaaabaaa"
print(longestPalin(A))  

"""
Approach 2
"""

def printSubStr(str, low, high):  
    s = ""     
    for i in range(low, high+1):
        s += str[i]
    return s
        
def longestPalSubstr(str):
    n = len(str)
    maxLength = 1
    start = 0
    for i in range(n):
        for j in range(i, n):
            flag = 1
             
            # Check palindrome
            for k in range(0, ((j - i) // 2) + 1):
                if (str[i + k] != str[j - k]):
                    flag = 0
 
            # Palindrome
            if (flag != 0 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1
                 
    
    return printSubStr(str.strip(), start, start + maxLength - 1)

A = "abbcccbbbcaaccbababcbcabca"
print(longestPalSubstr(A))  

"""
Approach3
"""

class Solution(object):
   def longestPalindrome(self, A):
      n = len(A)
      dp = [[False for i in range(n)] for i in range(n)]
      for i in range(n):
         dp[i][i] = True
      max_length = 1
      start = 0
      for l in range(2,n+1):
         for i in range(n-l+1):
            end = i+l
            if l==2:
               if A[i] == A[end-1]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
            else:
               if A[i] == A[end-1] and dp[i+1][end-2]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
      return A[start:start+max_length]
ob1 = Solution()
A = "abbcccbbbcaaccbababcbcabca"
print(ob1.longestPalindrome(A))

"""
Approach 4
"""
#Expand in both directions of `low` and `high` to find maximum length palindrome
def expand(s, low, high):
    length = len(s)
 
    # expand in both directions
    while low >= 0 and high < length and s[low] == s[high]:
        low = low - 1
        high = high + 1
 
    # return palindromic substring
    return s[low + 1:high]
 
 
# Function to find the longest palindromic substring in `O(n²)` time and `O(1)` space
def findLongestPalindromicSubstring(A):
    n = len(A)
    if not A or not n:
        return '' 
    max_str = ''; max_length = 0 
    # consider every character of the given string as a midpoint and expand
    # in both directions to find maximum length palindrome 
    for i in range(n): 
        # find the longest odd length palindrome with `s[i]` as a midpoint
        curr_str = expand(A, i, i)
        curr_length = len(curr_str)
 
        # update maximum length palindromic substring if the odd length
        # palindrome has a greater length
 
        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str
 
        # Find the longest even length palindrome with `s[i]` and `s[i+1]` as
        # midpoints. Note that an even length palindrome has two midpoints.
 
        curr_str = expand(A, i, i + 1)
        curr_length = len(curr_str)
 
        # update maximum length palindromic substring if even length
        # palindrome has a greater length
 
        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str
 
    return max_str

A = "abbcccbbbcaaccbababcbcabca"
print(findLongestPalindromicSubstring(A))

"""
Given a string A of size N consisting of lowercase alphabets.

You can change at most B characters in the given string to any other 
lowercase alphabet such that the number of distinct characters in the string is minimized.

Find the minimum number of distinct characters in the resulting string.


"""

from collections import Counter
class Solution:
   def solve(self, s, k):
      count = Counter(s)
      sv = sorted(count.values())
      ans = 0
      for i in range(len(count) - k):
         ans += sv[i]
      return ans

ob = Solution()
s = "wxxyyzzxx"
k = 3
print(ob.solve(s, k))


"""
Approach1
"""
def minimizeChar(A, B):
    char_count = {}
    
    for char in A:
        if char not in char_count:
            char_count[char] = 0
    
        char_count[char] += 1
    
    counts = sorted(char_count.values())
    
    # Current number of distinct characters
    answer = len(counts)
    
    # Excluding the last element because there has to be atleast 1 character
    for i in range(len(counts) - 1):
        # We can substitute all the characters
        # Assume you are substituting for the max occurred character
        if counts[i] <= B:
            B -= counts[i]
            answer -= 1
    
        # If we can't substitute all counts[i]
        # We definitely can't substitute for any upcoming values
        else:
            break
    
    return(answer)
    
A = "abcabbccd"
B = 3
print(minimizeChar(A, B))
