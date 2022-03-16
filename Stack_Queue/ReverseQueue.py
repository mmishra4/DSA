#Given an array of integers A and an integer B, we need to reverse the order of the first B elements of the array, 
#leaving the other elements in the same relative order.
#NOTE: You are required to the first insert elements into an auxiliary queue then perform Reversal of first B elements.

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
