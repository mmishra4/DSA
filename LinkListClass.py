# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 10:15:26 2022

@author: MMEENAK4
"""

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        
head = Node(1)
print(head)

temp = head
temp = temp.next
print(temp)

print(head)
    