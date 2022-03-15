# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:36:27 2021

@author: MMEENAK4
"""

class Solution:
    def __init__(self):
        self.items = []
        
    def solve(self, A):
          Even= [];
          Odd= [];
          for i in A:
              if i%2 == 0:
                   Even.append(i)
              else:
                   Odd.append(i)    
          return (max(Even)-min(Odd))
      
    def getPairsCount(self, a, b):
        count = 0  # Initialize result
        n = len(a)
        # Consider all possible pairs and check their sums
        for i in range(0, n):
            for j in range(i + 1, n):
                if a[i] + a[j] == b:
                    count += 1 
        return count
    
#     def findCommonElements(self, a, b):
#         arr1 = []
#         if (len(a) > 0 && len(b) >0):
#             for i in range(0, len(a)):
#                 arr1.append(i)
#             for j in range(0, len(b)):
#                 if arr1.        
#        return count
#    
    def cmn(a, b):
        a.sort()
        b.sort()
        n = len(a)
        m = len(b)
        i = 0
        j = 0
        c = []
          
        while (i < n and j < m) : 
                      
            if (a[i] > b[j]) : 
                j += 1
                      
            else: 
                if (b[j] > a[i]) : 
                    i += 1
      
                else: 
                    # when both are equal 
                    #print(a[i], end = " ") 
                    c.append(a[i])
                    i += 1
                    j += 1      
        return c
    
    def subWhile(n):
        a = 0
        i = n
        while (i > 0):
            a+=i
            i /= 2
            print(i)
        return i
            
    
    def subAE(arr, n):
        
    # traverse through array
    # and store prefix sums
        n_sum = 0
        s = set()
     
        for i in range(n):
            n_sum += arr[i]
     
            # If prefix sum is 0 or
            # it is already present
            if n_sum == 0 or n_sum in s:
                return 1
            s.add(n_sum)
 
        return 0
       
       
if __name__ == "__main__":
    s = Solution()
    A = [0,2,9]
    s.solve(A)
    B = [5,2]
    s.solve(B)
    # Driver function
    a = [1, 5, 7, -1, 5]
    b = 6
    print("Count of pairs is", s.getPairsCount(a,b))
    a = [1,2,2,1] 
    b = [2,3,1,2] 
    cmn(a, b) 
    arr = [-3, 2, 3, 1, 6]
    n = len(arr)
    if subAE(arr, n) == 1:
        print("Found a sunbarray with 0 sum")
    else:
        print("No Such sub array exits!")
    N = subWhile(8)
    print(N)
     