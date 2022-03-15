# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:05:31 2022
Count of nodes that are greater than Ancestors
@author: MMEENAK4
"""

from collections import deque
 
# A Tree node
class Tree:
   
    def __init__(self, x):
       
        self.val = x
        self.left = None
        self.right = None
 
count = 0
 
# Dfs Function
def dfs(node, maxx):
   
    global count
     
    # Base case
    if (node == None):
        return
    else:
 
        # Increment the count if
        # the current node's value
        # is greater than the maximum
        # value in it's ancestors
        if (node.val > maxx):
            count += 1
 
        # Left traversal
        dfs(node.left, max(maxx,node.val))
 
        # Right traversal
        dfs(node.right,max(maxx,node.val))
           
# Driver code
if __name__ == '__main__':
 
    root = Tree(4)
    root.left = Tree(5)
    root.right = Tree(2)
    root.right.left = Tree(3)
    root.right.right = Tree(6)
 
    # To store the required
    # count
    count = 0
 
    dfs(root,-10 ** 9)
    print(count)
 