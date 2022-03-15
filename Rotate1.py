# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:02:49 2022

@author: MMEENAK4
"""



def solve(self, A, B):
        n = len(A)
        for r in range(n):
            for c in range(r+1, n):
                if (A[r] + A[c] == B):
                    return 1
        return 0
    
def rotate(Arr, k):
    N = Arr
    c= len(N)-k
    c = len(N)-k
    list1 = N[0:c]
    list1.reverse()
    list2 = N[c:len(N)]
    list2.reverse()
    list1 = list1+list2
    list1.reverse()
    print(*list1, sep=' ')
 
def RightRotate(a, n, k):
 
    # If rotation is greater
    # than size of array
    k = k % n;
     
    for i in range(0, n):
     
        if(i < k):
     
            # Printing rightmost
            # kth elements
            print(a[n + i - k], end = " ");
     
        else:
     
            # Prints array after
            # 'k' elements
            print(a[i - k], end = " ");     
    print("\n");
    
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    Num = []
    input_string = input() 
    NM = input_string.split()
    for i in range(1,len(NM)):
    # convert each item to int type
        item = int(NM[i])
        Num.append(item)
    B = int(input())
    if (len(Num)>0 and B > 0) :
        RightRotate(Num, len(Num), B)
    return 0
# Function to exchange data of two given indices in a list
def swap(A, i, j):
 
    data = A[i]
    A[i] = A[j]
    A[j] = data
 
 
# Function to reverse a given sublist
def reverse(A, low, high):
 
    i = low
    j = high
    while i < j:
        swap(A, i, j)
        i = i + 1
        j = j - 1
 
 
# Function to right-rotate a list by `k` positions
def rightRotate(A, k, n):
 
    # base case: invalid input
    if k < 0 or k >= n:
        return
 
    # Reverse the last `k` elements
    reverse(A, n - k, n - 1)
 
    # Reverse the first `n-k` elements
    reverse(A, 0, n - k - 1)
 
    # Reverse the whole list
    reverse(A, 0, n - 1)
 
 
if __name__ == '__main__':
 
    A = [1, 2, 3, 4, 5, 6, 7]
    k = 3
 
    rightRotate(A, k, len(A))
    print(A)
