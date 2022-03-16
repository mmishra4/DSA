#Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def isMirror(root1, root2):
    # If both trees are empty, then they are mirror images
    if root1 is None and root2 is None:
        return True
  
    """ For two trees to be mirror images, 
        the following three conditions must be true
        1 - Their root node's key must be same
        2 - left subtree of left tree and right subtree
          of the right tree have to be mirror images
        3 - right subtree of left tree and left subtree
           of right tree have to be mirror images
    """
    if (root1 is not None and root2 is not None):
        if root1.val == root2.val:
            return (isMirror(root1.left, root2.right)and
                    isMirror(root1.right, root2.left))
  
    # If none of the above conditions is true then root1
    # and root2 are not mirror images
    return False
class Solution:
	# @param A : root node of tree
	# @return an integer
	def isSymmetric(self, A):
        if isMirror(A, A):
            return 1
        else:
            return 0
