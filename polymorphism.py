
#method overloading
class mo():
    def myfunct(self):
        print(" function with no argument")
    def myfunct(self,a):
        print(" function with 1 argument")
    def myfunct(self,a,b):
        print("function with 2 argument")
m=mo()
m.myfunct(10,2)

#method overriding
class mo1:
    def myfunct(self,a):
        print("class mo1 funct called")
class mo2(mo1):
    def myfunct(self,a):
        print("class mo2 funct called")
        # super method calling the method of class mo1
        super().myfunct(10)
class mo3(mo2):
    def myfunct(self,a):
        print("class mo3 funct called")
        #super method calling the method of class mo2
        super().myfunct(10)
m=mo3()
m.myfunct(10)


############
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


    #########

from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
