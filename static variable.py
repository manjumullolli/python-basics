#various place to declare to static variables
#within the class directly, but outside of any method or constructor
class test:
    a=10
print(test.__dict__)

#

"""class test:
    a=20
    def __init__(self):
        test.b=20
    def m1(self):
        test.c=30
    @classmethod
    def m2(cls):
        cls.d=40
        test.e=50
    @staticmethod
    def m3():
        test.f=60

t=test()
t.m1()
t.m2()
t.m3() #satic method directly called by class name i.e test.m3
test.g=70
print(test.__dict__)

class test():
    a=20
    def __init__(self):
        self.b=20
t1=test()
t2=test()
test.a=888
t1.b=999
print('t1:', t1.a, t1.b)
print('t2:', t2.a, t2.b)

#####
class test:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        self.a=888
        self.b=999
t1=test()
t2=test()
t1.m1()
print('t1:', t1.a, t2.b)
print('t2:', t2.a, t2.b)
#####
class test():
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        self.a=888
        self.b=999
t1=test()
t2=test()
t1.m1()
t2.m1()
print('t1:', t1.a, t1.b)
print('t2', t2.a, t2.b)
#########
class test():
    a=10
    def __init__(self):
        self.b=20
    @classmethod
    def m1(cls):
        cls.a=888
        cls.b=999
t1=test()
t2=test()
t1.m1()
print('t1:', t1.a, t1.b)
print('t2', t2.a, t2.b)
print('test:', test.a, test.b)

###setter and getter
class student:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks
n = int(input('enter number of students:'))
students=[]
for i in range(n):
    s=student()
    name=input('enter student name:')
    marks=int(input('Enter student marks:'))
    s.setname(name)
    s.setmarks(marks)
    students.append(s)
for s in students:
    print('hi', s.getname())
    print('your marks is', s.getmarks())
    print()"""


######################################
"""class student:
    def __init__(delf,name,rollno,marks):
        delf.name=name
        delf.rollno=rollno
        delf.marks=marks
    def talk(kelf):
        print('hello i am:' , kelf.name)
        print('my rollno is:', kelf.rollno)
        print('my marks are:', kelf.marks)
s1=student('sunny',101,56)
s1.talk()"""

