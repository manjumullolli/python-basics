#accessing members of one class inside another class
"""class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print('emp no:',self.eno)
        print('emp name:',self.ename)
        print('emp sal:',self.esal)
class manager:
    def updateempsal(emp):
        emp.esal=emp.esal+1000
        emp.display()
emp=employee(11,'sunny',4000)
manager.updateempsal(emp)
"""
#########
"""class bird:
    wings=2
    @classmethod
    def fly(cls,name):
        print('{} flying with {} wings'.format(name,cls.wings))
bird.fly('parrot')
bird.fly('pigeon')"""
#prgm to track no of objects created for a class
class test():
    count=0
    def __init__(self):
        test.count=test.count+1
    @classmethod
    def getnoofobject(cls):
        print('the no of objects created:', cls.count)
test.getnoofobject() #0
t1=test()
t2=test()
t3=test()
t4=test()
test.getnoofobject()