
print('...........single inheritance...........')
class p():
    def m1(self):
        print('parent method')
class C(p):
    def m2(self):
        print('child method')
a=C()
a.m1()
a.m2()

print('.....................multilevel inherit..........')
class p:
    def m1(self):
        print('parent class')
class c(p):
    def m2(self):
        print('sub parent')
class cc(c):
    def m3(self):
        print('child class')
x=cc()
x.m1()
x.m2()
x.m3()

print('..................hierarchical inherit..........')
class p():
    def m1(self):
        print('parent class')
class c1(p):
    def m2(self):
        print('child one class')
class c2(p):
    def m3(self):
        print('child 2')
c=c1()#obj of child one
a=c2()#obj of child two
c.m1()
c.m2()
a.m1()
a.m3()

print('.................multiple inherit.............')
class p1():
    def m1(self):
        print('parent1 method')
class p2():
    def m2(self):
        print('parent2 ')
class c(p1,p2):
    def m3(self):
        print('child class')
C=c()
C.m1()
C.m2()
C.m3()

print('............hierarchical iherit...................')
class  p:
    def m1(self):
        print('parent class')
class c1(p):
    def m2(self):
        print('child 1')
class c2(p):
    def m3(self):
        print('child 2')
c=c1()
a=c2()
c.m1()
c.m2()
a.m1()
a.m3()

print('..............hybrid inherit..........')
class b1():
    def myfun1(self):
        print('parent class')
class b2(b1):
    def myfun2(self):
        print('child 1')
class b3(b1):
    def myfun3(self):
        print('child 2')
class b4(b2,b3):
    def myfun4(self):
        print('child 3')
b=b4()
b.myfun1()
b.myfun2()
b.myfun3()
b.myfun4()