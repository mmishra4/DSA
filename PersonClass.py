# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 14:34:47 2022

@author: MMEENAK4
"""

class Person:
    def __init__(self, first_name, last_name):
        print("Person init is run")
        self.first_name = first_name
        self.last_name = last_name
        
    def say_hello(self):
        print("Person hello is rum")
        print(f"Hi my name is {self.name}")

#Inheritance
class Employee(Person):
    #method overriding
    def __init__(self, first_name, last_name, salary):
        print("Employee init is run")
        #super will call base calss init method
        super().__init__(first_name, last_name)
        self.salary = salary
        
    #Polymorphism - overridden the existing behavior
    def say_hello(self):
        print("Employee ssy hello is run")
    def print_salary(self):
        print("10,000")
        
e = Employee("Mee","M", 10000)
e.say_hello()
e.print_salary()