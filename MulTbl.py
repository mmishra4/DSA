# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 12:34:11 2022

@author: MMEENAK4
"""
def main():
    Num = int(input())
    if Num > 0 :
        N = Num
        Opr = '*'
        Eq = '='
        for i in range (1, 11):
            print("{} {} {} {}".format(N, Opr, i, Eq), N*i)
    
    return 0

if __name__ == '__main__':
    main()

