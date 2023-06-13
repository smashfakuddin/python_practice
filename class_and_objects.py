# basic class

class MyClass:
    x = "Something for test"

    def function(self):
        print("This is a message inside the class") 

my_objectx = MyClass()
my_objecty = MyClass()

# assign new value 
my_objecty.x = "another Test"

# print(my_objectx.x)
# print(my_objecty.x)

my_objectx.function()

# init() function

class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

x = NumberHolder(7)
print(x.returnNumber()) #Prints '7'



# class Exercise

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "Red"
car1.value = 60000

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "Van"
car2.color = "Blue"
car2.value = 10000
# test code
print(car1.description())
print(car2.description())