"""class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self, other):
        return self.marks>other.marks
s1=student('sun',75)
s2=student('ravi',64)
print(s1>s2)
s3=student('shivu',98)
print(s1>s3)"""

print('...............................................')
"""class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self, other):
        return self.marks>other.marks
    def __le__(self, other):
        return self.marks<=other.marks
s1=student('duga',100)
s2=student('doga',200)
print(s1<=s2)"""
##overriding
class p:
    def property(self):
        print('cash+gold+land')
    def marry(self):
        print('laxmi')
class c(p):

     def marry(self):
         print('katrina')
c=c()
c.property()
c.marry()