
try:
    print(45/0)
except:
    print("enter num should > 0")
finally:
    print("thank you")

try:
    print(x)
except:
    print("an exception occurred")


try:
    print(x)
except NameError:
    print("x is not defined")
except:
    print("something went wrong")


try:
    print("hello")
except:
    print("jfk kkf ")
else:
    print("gjojo jjo")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")



x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")



x = "hello"

 if not type(x) is int:
  raise TypeError("Only integers are allowed")
