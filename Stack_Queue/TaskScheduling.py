#A CPU has N tasks to be performed. It is to be noted that the tasks have to be completed in a specific order to avoid deadlock. 
#In every clock cycle, the CPU can either perform a task or move it to the back of the queue. 
#You are given the current state of the scheduler queue in array A and the required order of the tasks in array B.
#Determine the minimum number of clock cycles to complete all the tasks.

import collections
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        q = collections.deque(A)
        n = len(B)
        ans = 0
        for i in B:
            temp = q.popleft()
            while i != temp:
                ans += 1
                q.append(temp)
                temp = q.popleft()
            ans += 1
        return ans


