class Animal:
    def __init__(self):
        print("Animal is Here")

    def sound(self):
        print("Animal Sounds")
        
# Define class Dog
class Dog(Animal):
           
    def __init__(self, name, breed):
    # standard we call the __init__ method of the base class
        #super().__init__() # self will be added by Python
        print("Animal is Here")
        self.name = name
        self.breed = breed
        
    def getname(self):
        return self.name 
    def getbreed(self):
        return self.breed
    
    def sound(self):
        #super().sound()
        print(f"Dog barks")

# Define class Dog
class Cat(Animal):           
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def getname(self):
        return self.name 
    def getbreed(self):
        return self.breed
    
    def sound(self):
        #super().sound()
        print(f"Cat meows")    
#def main():

# Create the instances for the classes here
a = Animal()
a.sound()
m = Dog('A', 'Chihuaa')
m.sound()
n = Cat('C', 'Disk')
n.sound()




