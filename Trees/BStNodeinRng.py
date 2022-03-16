#Given a binary search tree of integers. You are given a range B and C.Return the count of the number of nodes that lie in the given range.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def getCount(root, low, high):
     
    # Base case
    if root == None:
        return 0
         
    # Special Optional case for improving
    # efficiency
    if root.val == high and root.val == low:
        return 1
 
    # If current node is in range, then
    # include it in count and recur for
    # left and right children of it
    if root.val <= high and root.val >= low:
        return (1 + getCount(root.left, low, high) +
                    getCount(root.right, low, high))
 
    # If current node is smaller than low,
    # then recur for right child
    elif root.val < low:
        return getCount(root.right, low, high)
 
    # Else recur for left child
    else:
        return getCount(root.left, low, high)
 

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return getCount(A, B, C)
