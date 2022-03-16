#You are given the root node of a binary tree A. You have to find the number of nodes in this tree.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def size(root):
    if root is None:
        return 0

    lst = size(root.left)
    rst = size(root.right)
    return lst+rst+1

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        import sys
        sys.setrecursionlimit(500000)
        return size(A)
