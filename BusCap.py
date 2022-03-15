# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 18:09:19 2022

@author: MMEENAK4
"""

class Bus():
    def __init__(self, name, mileage, max_speed):
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed

    def seating_capacity(self):
        self.capacity = 50
        #print(f"The seating capacity of a {self. name} with maxspeed {self.max_speed} and mileage {self.mileage} is {self.capacity}")
        #print("The seating capacity of a" + {self.name} + " with maxspeed "+{self.max_speed}+ " and mileage "+{self.mileage}+ "is" + {self.capacity})
        print("The seating capacity of a {}".format(self.name) + " with maxspeed {}" .format(self.max_speed)+ " and mileage {} ".format(self.mileage) + " is {}".format(self.capacity) )
School_bus=Bus("Volvo", "50", "45")
School_bus.seating_capacity()


