#Given the root of a tree A with each node having a certain value, find the count of nodes with more value than all its ancestor.

import sys
sys.setrecursionlimit(100006)
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def dfs(root, maxsofar):
    if root == None:
        return 0
    ans = 0
    if root.val > maxsofar:
        ans = 1
        maxsofar = root.val
    ans = ans + dfs(root.left, maxsofar)
    ans = ans + dfs(root.right, maxsofar)
    return ans


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        return dfs(A, 0)
