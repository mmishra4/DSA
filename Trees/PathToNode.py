#Given a Binary Tree A containing N nodes, you need to find the path from Root to a given node B.
#NOTE:No two nodes in the tree have the same data values.You can assume that B is present in tree A and a path always exists.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def hasPath(root, arr, x): 
      
    # if root is None there is no path  
    if (not root): 
        return False
      
    # push the node's value in 'arr'  
    arr.append(root.val)      
      
    # if it is the required node  
    # return true  
    if (root.val == x):      
        return True
      
    # else check whether the required node  
    # lies in the left subtree or right  
    # subtree of the current node  
    if (hasPath(root.left, arr, x) or 
        hasPath(root.right, arr, x)):  
        return True
      
    # required node does not lie either in  
    # the left or right subtree of the current  
    # node. Thus, remove current node's value   
    # from 'arr'and then return false      
    arr.pop(-1)  
    return False
  
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        ans=[]
        hasPath(A,ans,B)
        return ans

