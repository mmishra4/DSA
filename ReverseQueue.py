# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 18:34:09 2022
Given an array of integers A and an integer B. We need to reverse the order 
of the first B elements of the array, leaving the other elements in the same relative order.
@author: MMEENAK4
"""

from queue import Queue
 
# Function to reverse the first K
# elements of the Queue
def reverseQueueFirstKElements(k, Queue):
    if (Queue.empty() == True or
             k > Queue.qsize()):
        return
    if (k <= 0):
        return
 
    Stack = []
 
    # put the first K elements
    # into a Stack
    for i in range(k):
        Stack.append(Queue.queue[0])
        Queue.get()
 
    # Enqueue the contents of stack
    # at the back of the queue
    while (len(Stack) != 0 ):
        Queue.put(Stack[-1])
        Stack.pop()
 
    # Remove the remaining elements and
    # enqueue them at the end of the Queue
    for i in range(Queue.qsize() - k):
        Queue.put(Queue.queue[0])
        Queue.get()
        
    # Utility Function to print the Queue
    def Print(Queue):
        while (not Queue.empty()):
            print(Queue.queue[0], end =" ")
            Queue.get()
 
def solve(A,B):
    q = Queue()
    for i in A:
        q.put(i)
    reverseQueueFirstKElements(B, q)
    #Print(q) 
    return list(q.queue)
 
A = [1, 2, 3, 4, 5]
B = 3
print(solve(A, B))

"""
Approach 2
"""
from collections import deque
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        if n < 2:
            return A
        q = deque()
        for i in range(B):
            q.append(A[i])
        i = B - 1
        while len(q) != 0:
            A[i] = q.popleft()
            i -= 1
        return A

A = [1, 2, 3, 4, 5]
B = 3
s = Solution()
s.solve(A, B)

#===================================
"""
Given an integer A. Find and Return first positive 
A integers in ascending order containing only digits 1, 2 and 3.
"""
from collections import deque

def solve(A):
    ans = []
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    cnt = 3
    while len(ans) < A:
        x = q.popleft()
        ans.append(x)
        if cnt>=A: continue
        x1 = x * 10 + 1
        x2 = x * 10 + 2
        x3 = x * 10 + 3
        q.append(x1)
        q.append(x2)
        q.append(x3)
        cnt += 3

    return ans

A=7
print(solve(7))
#===========
def isBalanced(exp):
  
    # Initialising Variables
    flag = 1
    count = 0
  
    # Traversing the Expression
    for i in range(len(exp)):
        if (exp[i] == '('):
            count += 1
        else:
              
            # It is a closing parenthesis
            count -= 1
  
        if (count < 0):
  
            # This means there are 
            # more closing parenthesis 
            # than opening
            flag = 0
            break
  
    # If count is not zero , 
    # it means there are more 
    # opening parenthesis
    if (count != 0):
        flag = 0
  
    return flag

A = '(())'
print(isBalanced(A))

"""
Return an integer denoting the minimum number of clock cycles 
required to complete all the tasks.
"""
