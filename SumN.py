# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 18:57:39 2022
1. Find the sum of first n numbers 
2. Wheter a number is a perfect 

@author: MMEENAK4
"""

# =============================================================================
# def main():
#     val1 = input("Enter the number: ")
#     N = int(val1)
#     Sum = N*(N+1) // 2
#     print(Sum)
#     return Sum
# =============================================================================


def main():
    N = int(input())
    while N > 0:
        A = int(input())
        sum = 0
        for i in range(1,A):
            if A%i == 0:
                sum += i

        if sum == A:
            print('YES')
        else:
            print('NO')
        N-= 1

    return 0


if __name__ == '__main__':
    main()