#Given two binary trees, check if they are equal or not.
#Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def identicalTrees(a, b):     
    # 1. Both empty
    if a is None and b is None:
        return True
 
    # 2. Both non-empty -> Compare them
    if a is not None and b is not None:
        return ((a.val == b.val) and
                identicalTrees(a.left, b.left)and
                identicalTrees(a.right, b.right))
     
    # 3. one empty, one not -- false
    return False

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):
        if identicalTrees(A, B):
            return 1
        else:
            return 0
