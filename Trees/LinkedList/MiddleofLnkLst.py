#Given a linked list of integers, find and return the middle element of the linked list.
#NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.
#eg: i/p:  1 -> 2 -> 3 -> 4 -> 5  o/p: 3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Linked List class contains a Node object
class LinkedList:
   
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = ListNode(new_data) 
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

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A): 
        n = int(A)       
        llist = LinkedList()   
        for i in range(n, 0, -1):
            llist.push(i)
            #llist.printList()
            a = llist.printMiddle()
        return a
