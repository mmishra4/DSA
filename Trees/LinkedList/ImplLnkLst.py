#Design and implement a Linked List data structure.
#A node in a linked list should have the following attributes - an integer value and a pointer to the next node. It should support the following operations:

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = None
size_of_ll = 0


def insert_node(position, value):
    global head
    global size_of_ll
    if position >= 1 and position <= size_of_ll + 1:
        temp = ListNode(value)
        if position == 1:
            temp.next = head
            head = temp
        else:
            count = 1
            prev = head
            while count < position - 1:
                prev = prev.next
                count += 1
            temp.next = prev.next
            prev.next = temp
        size_of_ll += 1


def delete_node(position):
    global head
    global size_of_ll
    if position >= 1 and position <= size_of_ll:
        temp = None
        if position == 1:
            temp = head
            head = head.next
        else:
            count = 1
            prev = head
            while count < position - 1:
                prev = prev.next
                count += 1
            temp = prev.next
            prev.next = prev.next.next
        size_of_ll -= 1


def print_ll():
    global head
    tmp = head
    ans = []
    while tmp is not None:
        ans.append(str(tmp.val))
        tmp = tmp.next
    print(" ".join(ans))
