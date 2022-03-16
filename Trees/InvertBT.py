#Given a binary tree A, invert the binary tree and return it.Inverting refers to making the left child the right child and vice versa.

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def invert(root):
    if root == None:
        return None
    linv = invert(root.left)
    rinv = invert(root.right)
    root.right = linv
    root.left = rinv
    return root

class Solution:
	# @param A : root node of tree
	# @return the root node in the tree
	def invertTree(self, A):
        return invert(A)
