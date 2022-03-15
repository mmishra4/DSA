# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:56:24 2022
Find the square root of a number
@author: MMEENAK4
"""

def floorSqrt(x) :
 
    # Base cases
    if (x == 0 or x == 1) :
        return x
  
    # Do Binary Search for floor(sqrt(x))
    start = 1
    end = x  
    while (start <= end) :
        mid = (start + end) // 2
        # If x is a perfect square
        if (mid*mid == x) :
            return(mid)
        # Since we need floor, we update
        # answer when mid*mid is smaller
        # than x, and move closer to sqrt(x)
        if (mid * mid < x) :
            start = mid + 1
            ans = mid             
        else :             
            # If mid*mid is greater than x
            end = mid-1
    
    return -1
 
# driver code   
x = 111
print(floorSqrt(x))