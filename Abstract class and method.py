from abc import ABC, abstractmethod
class father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print('concrete method')
class child(father):
    def disp(self):
        print('child class')
        print('defining abstract method')
c=child()
c.disp()
c.show()
print('...................................')
from abc import ABC, abstractmethod
class defenceforce(ABC):
    @abstractmethod
    def area(self):
        pass
    def gun(self):
        print('gun=ak47')
class army(defenceforce):
    def area(self):
        print('land')
class airforce(defenceforce):
    def area(self):
        print('sky')
class navy(defenceforce):
    def area(self):
        print('sea')
a=army()
af=airforce()
n=navy()
a.gun()
a.area()
af.gun()
af.area()
n.gun()
n.area()