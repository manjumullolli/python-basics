class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages + other.pages
    def __sub__(self, other):
        return self.pages-other.pages
b1=book(800)
b2=book(500)
b3=book(300)
print(b2-b3)
print(b1-b2)
print(b1-b3)
print('......................................')

class book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return 'the number of pages:'+str(self.pages)
    def __add__(self, other):
        return self.pages+other.pages
b1=book(100)
b2=book(200)
b3=book(300)
print(b1+b2)
print('..........................')

class book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return 'the number of pages:'+str(self.pages)
    def __add__(self, other):
        total=self.pages+other.pages
        b=book(total)
        return b
b1=book(100)
b2=book(200)
b3=book(300)
b4=book(400)
print(b1+b2+b3+b4)
print('....................................')

class book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return 'the number of pages:'+str(self.pages)
    def __add__(self, other):
        total=self.pages+other.pages
        b=book(total)
        return b
    def __mul__(self, other):
        total=self.pages*other.pages
        b=book(total)
        return b
b1=book(100)
b2=book(200)
b3=book(300)
b4=book(400)
print(b1+b2+b3+b4)
print(b1*b2+b3*b4)
print('.............................')
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __lt__(self, other):
        return self.marks<other.marks
s1=student('durga',100)
s2=student('raj',200)
print(s1<s2)
print(s2<s1)
print('......................................')
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self, other):
        return self.salary*other.days
class timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days

    # def __mul__(self, other):
    #     return self.days * other.salary
e=employee('durga',500)
t=timesheet('durga',25)
print('this month salary:',e*t)
# print('this month salary:',t*e)




