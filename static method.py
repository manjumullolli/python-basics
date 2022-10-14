#how to delete static method
"""class test:
    a=10
    @classmethod
    def m1(cls):
        del cls.a
        #del test.a
#test.m1()
del test.a
print(test.__dict__)"""


"""class test:
    a=10
    def __init__(self):
        test.b=20
        del test.a
    def m1(self):
        test.c=30
        del test.b
    @classmethod
    def m2(cls):
        cls.d=40
        del test.c
    @staticmethod
    def m3():
        test.e=50
        del test.d
t=test()
t.m1()
t.m2()
t.m3()
del test.e
print(test.__dict__)"""
########################################3
class durgamath:
    @staticmethod
    def add (a,b):
        print('the sum:',(a+b))
    @staticmethod
    def product(a,b):
        print('the product is:', (a*b))
    @staticmethod
    def average(a,b):
        print('the average is:', (a+b)/2)
durgamath.add(10,20)
durgamath.product(20,5)
durgamath.average(50,30)