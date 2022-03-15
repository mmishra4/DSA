# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:08:11 2022
A recursive Python program
# to check whether a given
# number is palindrome or not
@author: MMEENAK4
""" 
# A recursive function that
# check a str[s..e] is
# palindrome or not.
def isPalRec(st, s, e) :
     
    # If there is only one character
    if (s == e):
        return True
 
    # If first and last
    # characters do not match
    if (st[s] != st[e]) :
        return False
 
    # If there are more than
    # two characters, check if
    # middle substring is also
    # palindrome or not.
    if (s < e + 1) :
        return isPalRec(st, s + 1, e - 1);
 
    return True
 
def isPalindrome(A) :
    n = len(A)     
    # An empty string is
    # considered as palindrome
    if (n == 0) :
        return 1
     
    if isPalRec(A, 0, n - 1):
        return 1
    else:
        return 0
 
A = "NAMAN"
print(isPalindrome(A))

"""
Write a program to find the factorial of the given number A.
"""
def factorial(N):
    if N==0:
        return 1
    return N*factorial(N-1)

N=4
print(factorial(N))

"""
Reverse a string recursively
"""

def reverse(A):
    if len(A) == 0:
        return A
    else:
        return reverse(A[1:]) + A[0]

A = "mad"
print(reverse(A))

s = input()

print(reverse(s))

"""
Test function 1
Find power
"""
def bar(x,y):
    if y ==0:
        return 0
    return (x + bar(x, y-1))

def foo(x,y):
    if y==0 :
        return 1
    return bar(x, foo(x,y-1))

print(foo(2,10))

"""
Test function 2
Pwer function
"""
def fun(x,n):
    if(n==0):
        return 1
    elif(n%2 == 0):
        return fun(x*x, n//2)
    else:
        return x*fun(x*x,(n-1)//2)

ans = fun(2,10)
print(ans)
 
"""    
sum of first N natural numbers
"""
def recursiveSum(n):
    if n <= 1:
        return n
    return n + recursiveSum(n - 1)

A = 5
print(recursiveSum(A))

"""
Given a number A, we need to find sum of its digits using recursion.
"""

def sum_of_digit( n ):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))

A=1234
print(sum_of_digit(A))

"""
Magic NUmber
"""

def isMagic(n):
    sum = 0;
    while (n > 0 or sum > 9):
        if (n == 0):
            n = sum;
            sum = 0;
        sum = sum + n % 10;
        n = int(n / 10);
    return 1 if (sum == 1) else 0;

A=83557
print(isMagic(A))  
        

"""
find((x pow n)%d)
"""
def fun(x,n):
    if(n==0):
        return 1
    elif(n%2 == 0):
        return fun(x*x, n//2)
    else:
        return x*fun(x*x,(n-1)//2)
def pow(A, B,C):
    return fun(A,B)%C

A = 2; B = 3; C = 3;
print(pow(A,B,C))

