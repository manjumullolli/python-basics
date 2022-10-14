class rbi():
    def interest(self):
        pass
class sbi(rbi):
    def interest(self):
        print("sbi interest is 5%")
class hdfc(rbi):
    def interest(self):
        print("hdfc interest is 6%")
S=sbi()
H=hdfc()

S.interest()
H.interest()

class animal():
    def move(self):
        pass
class dog(animal):
    def move(self):
        print("i can bark")
class cat(animal):
    def move(self):
        print("i can mewmew")
D=dog()
C=cat()
D.move()
C.move()

from abc import ABC
class Car(ABC):
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()