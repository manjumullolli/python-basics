# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name
# student=student(12,'raju')
# print(str(student))
print('.....................')
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name
#     def __str__(self):
#         return 'class str is called'
# student=student(12,'raju')
# print(str(student))
print('..........................')
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name
#     def __str__(self):
#         return 'class str is called'
#     def __len__(self):
#         return(len(self.name))
#     def __del__(self):
#         print('student destroyed')
# student=student(12,'raju')
# print(len(student))
# del student
print('........................')
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3


    def __gt__(self, other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2
        if s1 > s2:
            return True
        else:
            return False


s1=student(20,50)
s2=student(50,60)

s3=s1+s2


if s1>s2:
    print('s1 wins')
else:
    print('s2 wins')