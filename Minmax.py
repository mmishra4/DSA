# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 14:36:36 2022

@author: MMEENAK4
"""

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
    return list1
 
    
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    while T > 0:
        A = input().split()
        N = int(A[0])
        B = int(input())
        found = 0
        for i in range(1, N + 1):
            A[i] = int(A[i])
            if A[i] ==  B:
                found = 1
            
        print(found)
        T -= 1
        
    return 0

if __name__ == '__main__':
    main()