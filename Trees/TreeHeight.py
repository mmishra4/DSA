#You are given the root node of a binary tree A. You have to find the height of the given tree.
#A binary tree's height is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def height(root):
    if root is None:
        return 0
    
    lHeight = height(root.left)
    rHeight = height(root.right)
    
    return max(lHeight, rHeight)+1

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        import sys
        sys.setrecursionlimit(500000)
        return height(A)
