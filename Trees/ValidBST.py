#Given a binary tree represented by root A.Assume a BST is defined as follows:
#1) The left subtree of a node contains only nodes with keys less than the node's key.
#2) The right subtree of a node contains only nodes with keys greater than the node's key.
#3) Both the left and right subtrees must also be binary search trees.

# Definition for a  binary tree node
INT_MAX = 4294967296
INT_MIN = -4294967296
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))
 
# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):
     
    # An empty tree is BST
    if node is None:
        return True
 
    # False if this node violates min/max constraint
    if node.val < mini or node.val > maxi:
        return False
 
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.val -1) and
          isBSTUtil(node.right, node.val+1, maxi))

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):
        if isBST(A):
            return 1
        else:
            return 0
