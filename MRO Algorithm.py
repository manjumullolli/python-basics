class A:
    def m1(self):
        print('A class method')
class B:
    def m1(self):
        print('B class method')
class C:
    def m1(self):
        print('c class method')
class D(A,B):
    def m1(self):
        print('d class')
class E(B,C):
    def m1(self):
        print('D class method')
class F(D,E,C):
   pass
f=F()
f.m2()

# print(F.mro()) #FDAEBCO
