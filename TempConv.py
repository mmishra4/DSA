# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 12:10:06 2022

@author: MMEENAK4

def tempconversion(self, s):
    if s == 'Cel':
        return ((t - 32) * 5/9)
    else:
        return ((t * 9/5) + 32)
        
def tempconversion(self, s):
        if s == 'Cel':
            return ((self.temp - 32) * 5/9)
        else:
            return ((self.temp * 9/5) + 32)
    

"""   
class Temperature:
    # YOUR CODE GOES HERE
    def __init__(self, temp):
        self.temp = temp
     
    
    def convertcelsius(self):
        cel = round((self.temp - 32) * 5/9, 2)
        print("{} degree celsius" . format(cel))
        
    def convertfahrenheit(self):
        far = round((self.temp * 9/5) + 32,2)
        print("{} degree fahrenheit" . format(far))
        
    
temp=Temperature(37)
temp.convertcelsius()
temp.convertfahrenheit()