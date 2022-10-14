"""class car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.cololr=color
    def getinfo(self):
        print('\tcarname:{}\n\tmodel:{}\n\tcolor:{}'.format(self.name,self.model,self.cololr))
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print('eating palav and drinking water')
class emp(person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car
    def work(self):
        print('coding pyt prgm')
    def empinfo(self):
        print('emp name:',self.name)
        print('emp age:',self.age)
        print('emp no:',self.eno)
        print('emp salary:',self.esal)
        print('emp car information')
        self.car.getinfo()
car=car('innova','2.5v','grey')
e=emp('ravi',35,255,10000,car)
e.eatndrink()
e.work()
e.empinfo()"""

