"""class A:
    def __init__(self,a):
        self.__a=a

    def show(self):
        print("private variable :",self.__a)

class B(A):
    def __init__(self,b):
        super().__init__(b)
    def showB(self):
        print(self.__a)

obj= B(20)
obj.showB()"""







class A():
    def __init__(self,a):
        self._a=a

    def show(self):
        print("protected varible: ", self._a)


class B(A):
    def __init__(self,b):
        super().__init__(b)
    def showB(self):
        print(self._a)
obj=B(250)
obj.showB()