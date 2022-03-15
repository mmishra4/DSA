# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:04:11 2022
given an integer N you need to print all the Armstrong Numbers between 1 to N.
@author: MMEENAK4
"""
    
def Armstrong():
    N = int(input())
    if N > 0:
        Num = N
        order = len(str(Num))
        print(order)
        temp = Num
        print(temp)
        sum = 0
        while (temp > 0):
            digit = temp % 10
            print(digit)            
            sum += digit ** order
            temp //= 10
            
        print(sum)
        if (sum == Num):
            print("Armstrong Number")
            return True
        else:
            print("Not Armstrong Number")
            return False

    return 0

def main():
    #lower = int(input())
    x = int(input())
    if x>0:
        N = x
        lower = 1
        upper = N
        for num in range(lower, upper + 1):
            # order of number
            order = len(str(num))
        
            # initialize sum
            sum = 0    
            temp = num
            while temp > 0:
                digit = temp % 10
                if order == 1:
                    sum += digit ** 3
                    temp //= 10
                else:                
                    sum += digit ** order
                    temp //= 10
               
            if num == sum:
                print("Armstrong numbers are:")
                print(sum)
    
    return 0


if __name__ == '__main__':
    main()
