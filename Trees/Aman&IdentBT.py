#Aman likes Identical Binary Trees. He bought two Binary Trees denoted by root node A and B.
#He wants to make both the Trees Identical but he is only allowed to do operation on Binary Tree A.
#In each operation, you can swap the left pointer and right pointer of any node.
#Return the minimum number of operations required to make both trees identical. If, impossible return -1.
#NOTE: Two binary trees are considered Identical if they are structurally identical and the nodes have the same value.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def check(a, b):
    if a == None and b == None:
        return 1

    if a == None or b == None:
        return 0

    if a.val == b.val:
        return 1

    return 0


def recur(A, B):
    ans = 0
    if check(A.left, B.left) and check(A.right, B.right):
        temp = 0
        if A.left != None:
            temp = recur(A.left, B.left)
        if temp == -1:
            return -1

        ans += temp
        temp = 0
        if A.right != None:
            temp = recur(A.right, B.right)
        if temp == -1:
            return -1

        ans += temp

    elif check(A.left, B.right) and check(A.right, B.left):
        temp = 0
        ans += 1
        if A.left != None:
            temp = recur(A.left, B.right)

        if temp == -1:
            return -1

        ans += temp
        temp = 0
        if A.right != None:
            temp = recur(A.right, B.left)

        if temp == -1:
            return -1

        ans += temp

    else:
        return -1

    return ans


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def solve(self, A, B):
        if A.val == B.val:
            return recur(A, B)
        else:
            return -1

