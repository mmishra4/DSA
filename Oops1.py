# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:34:55 2022

@author: MMEENAK4
"""

class Demo: 

   def __init__(self, x): 

       self.x = x 

   def display(self, x): 

       print(x, self.x, end = " ") 

       x = x + self.x 

       self.x = x + self.x 

       print(x, self.x, x + self.x) 

obj = Demo(3) 

obj.display(10)