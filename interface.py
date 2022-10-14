from  abc import  ABC, abstractmethod

class father(ABC):
    @abstractmethod
    def disp(self):
        pass
    #def show(self):
        print('concrete method')


class child(father):
    def disp(self):
        print('child class')
        print('defining abstract method')

c=child()
c.disp()
print('...............................')

from abc import ABC, abstractmethod
class father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass
class child(father):
    def disp1(self):
        print('child class')
        print('disp1 abstract method')
class Grandchild(child):
    def disp2(self):
        print('grand child class')
        print('disp2 abstract method')
gc=Grandchild()
gc.disp1()
gc.disp2()



