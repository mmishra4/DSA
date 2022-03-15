# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:20:33 2022

@author: MMEENAK4
"""

"""
Height of Binary tree
"""
def height(root):
    if root is None:
        return
    lHeight = height(root.left)
    rHeight = height(root.right)
    return max(lHeight, rHeight)+1


"""
Post Order traversal of Binary tree
"""
def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data)