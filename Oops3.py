# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:27:10 2022

@author: MMEENAK4
"""

class A:

    def one(self):

        return self.two()   

    def two(self):

        return 'A'   

class B(A):

    def two(self):

        return 'B'

obj2=B()

===================
"""
"""
print(obj2.two())

class A:
    def __init__(self, a=1):
        self.a = a

class B(A):
    def __init__(self, b=2):
        super().__init__()
        self.b = b

def main():
    obj = B()
    print(obj.a, obj.b)

main()
===================
"""
"""
class Props:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Ball(Props):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = "o"
        self.number = 1
        self.vely = 0
        self.velx = 0

    def get_x(self):
        return self.x
 
    def get_y(self):
       return self.y

    def get_velx(self):
       return self.velx
 
    def get_vely(self):
       return self.vely
    
    def inc_velx(self):
       self.velx = self.velx+2
    
    def inc_vely(self):
       self.vely = self.vely+1
       
obj_ball = Ball(27,3)

bx = obj_ball.get_x()
by = obj_ball.get_y()
b_velx = obj_ball.get_velx()
b_vely = obj_ball.get_vely()

print(bx, by, b_velx, b_vely)