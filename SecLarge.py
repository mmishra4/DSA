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

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    while T > 0:
        A = input().split()
        N = int(A[0])
        s = []
        max2 = -1
        if N == 1:
            print(max2)
        else:
            for i in range(1, N+1):
                s.append(A[i])
            print(s)
            s.sort()
            print(s)
            max2 = s[N-2]
            print(max2)    
                
    return 0

if __name__ == '__main__':
    main()