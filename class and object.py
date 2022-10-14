#create class
class myclass:
    x=5
#creat object
m1=myclass()
print(m1.x)

#calling a function by object
class myclass:
    def myfunc(self):
        print("hello")
m1=myclass()
m1.myfunc()

#create constructor
class myclass:
    def __init__(self):
        print("this is my constructor")
m1=myclass()

#change the value by object

class myclass():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("my name is : " + self.name)
m1=myclass("rahul",25)
m1.myfunc()
m1.age=88
print("age:",m1.age)


class student():
    def check_pass_fail(self):
        if self.marks >= 40:
            return true
        else:
            return false
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    student1 = student("harry", 85)
    student2 = student('raji', 30)
    did_pass = student1. check_pass_fail()
    print(did_pass)
    did_pass = student2. check_pass_fail()
print(did_pass)

