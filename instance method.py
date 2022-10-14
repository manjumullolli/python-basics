"""class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('hi',self.name)
        print('your marks are:',self.marks)
    def grade(self):
        if self.marks>=60:
            print('you got first grade')
        elif self.marks>=50:
            print('you got second grade')
        elif self.marks>=35:
            print('you got third grade')
        else:
            print('you are fail')
n=int(input('enter number of students:'))
for i in range(n):
    name=input('enter student name:')
    marks=int(input('enter marks:'))
    A=student(name,marks)
    A.display()
    A.grade()
    print()"""

#how to access instance variable
"""class test():
    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        print(self.a)
        print(self.b)
t=test()
t.display()
print(t.a)
print(t.b)"""

#how to delete instance variable
"""class test():
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def m1(self):
        del self.c
t1=test()
t1.m1()
print('t1:', t1.__dict__)
t2=test()
del t2.b, t2.d
print('t2:', t2.__dict__)"""
###constructor
"""class student:
    def __init__(self,name,rollno,marks):
        print('creating instance variable and performing initialization..')
        self.name=name
        self.rollno=rollno
        self.marks=marks
s1=student('sunny',101,98)
print(s1.name,s1.rollno,s1.marks)
s2=student('bunny',102,55)
print(s2.name,s2.rollno,s2.marks)
#########instance variable
class test():
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t=test()
t.m1()
t.d=40
print(t.__dict__)

class test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t1=test()
t1.m1()
t1.d=40
t2=test()
print(t1.__dict__)
print(t2.__dict__)"""
#########################
class student():
    schoolname='durgasoft'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def getstdinfo(self):
        print('student name:',self.name)
        print('student rollno:',self.rollno)
    @classmethod
    def getschoolinfo(cls):
        print('schoolname:',cls.schoolname)
    @staticmethod
    def getsum(a,b):
        sum=a+b
        return sum


c=student('sunny',10)
c.getstdinfo()
student.getschoolinfo()
student.getsum(5,45)
