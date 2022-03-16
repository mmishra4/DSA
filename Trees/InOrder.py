#Given a binary tree, return the inorder traversal of its nodes' values.

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
def in_order(root, ans):
    if root:        
        in_order(root.left, ans)
        ans.append(root.val)
        in_order(root.right, ans)         
        return ans
        
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
        ans = []
        return in_order(A, ans)
