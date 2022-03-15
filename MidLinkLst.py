# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 12:19:57 2022
Given a linked list of integers. Find and return the middle element of the linked list.

NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.
@author: MMEENAK4
"""

class Node:
   
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
   
   
# Linked List class contains a Node object
class LinkedList:
   
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
 
    # Print the linked list
    def printList(self):
        node = self.head
        while node:
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")
 
    # Function that returns middle.
    def printMiddle(self):
        # Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
        slow = self.head
        fast = self.head
 
        # Iterate till fast's next is null (fast reaches end)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        # return the slow's data, which would be the middle element.
        #print("The middle element is ", slow.data)
        return slow.data
 
# Code execution starts here
if __name__=='__main__':
   
    # Start with the empty list
    llist = LinkedList()
   
    for i in range(5, 0, -1):
        llist.push(i)
        #llist.printList()
        a = llist.printMiddle()
    print(a)
 
    
"""

# Linked list implementation in Python


class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    # Print the linked list item
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next
"""