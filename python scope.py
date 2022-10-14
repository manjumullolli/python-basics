def myfun():
    x=800
    print(x)
myfun()

def myfun():
    x=500
    def myinnerfun():
      print(x)
    myinnerfun()
myfun()


def myfun():
    global x
    x=200
myfun()
print(x)

x=300
def myfun():
    global x
    x=500
myfun()
print(x)