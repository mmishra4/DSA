class Batman:
  fn = "Ben"
  ln = "Affleck"

  def instance_method(self):
    self.fn = "Christian"
    self.ln = "Bale"
    print(self.fn, self.ln, end = " | ")

  @classmethod
  def class_method(cls):
    print(cls.fn, cls.ln, end = " | ")
    cls.fn = "Robert"
    cls.ln = "Pattinson"

  @staticmethod
  def static_method():
    print(Batman.fn, Batman.ln)

batman = Batman()
batman.instance_method()
Batman.class_method()
Batman.static_method()


"""
"""
class test:
    def __init__(self,a):
        self.a=a
    def display(self):
        print(self.a)
obj=test()
obj.display()

"""
"""
class People():


  def __init__(self, name):

    self.name = name


  def namePrint(self):

    print(self.name)


person1 = People("Sally")

person2 = People("Louise")

person2.namePrint()

"""
"""
class People():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

person1 = People("John")
person2 = People("Mary")
person1.get_name()

"""
"""
class Football:
  final_res = "lose"
  def __init__(self, name, score):
    self.name = name
    self.score = score
    self.final_res = "lose"
  def calc(self, winning_score):
    if self.score > winning_score:
       self.final_res = "win"

match = Football("Juventus", 3)
match.calc(2)
print(Football.final_res, match.final_res)

"""
Temperature Conversion
"""

def tempconversion(self, s):
    if s == 'Cel':
        return ((t - 32) * 5/9)
    else:
        return ((t * 9/5) + 32)
    
class Temperature:
    # YOUR CODE GOES HERE
    def __init__(self, temp):
        self.temp = temp
     
    def tempconversion(self, s):
        if s == 'Cel':
            return ((self.temp - 32) * 5/9)
        else:
            return ((self.temp * 9/5) + 32)
    

    def convertcelsius(self):
        cel = tempconversion(self,'Cel')
        print(cel, "degree celsius")
        
    def convertfahrenheit(self):
        cel = tempconversion(self,'Far')
        print(cel, "degree celsius")
        
    
temp=Temperature(23)
temp.convertcelsius()
temp.convertfahrenheit()