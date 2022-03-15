# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:37:31 2022
Whether a given number is prime or not
@author: MMEENAK4
"""
import math
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    if A > 0:
        N = A
        s = math.sqrt(N)
        j = int(s)        
        cnt = 0
        if N==1:
            print('No')
            return False
        for i in range (2,j+1):
             if N%i==0:
                 cnt+=1
                 print('No')
                 break
        if cnt==0:
            print('Yes')
            return True
        else:
            print('No')
            return False
    return 0
            
if __name__ == '__main__':
    main()