"""mylist=[4,5,6,7]
myiter=iter(mylist)
print(next(myiter))
print(next(myiter))
print(myiter.__next__())
print(myiter.__next__())

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)"""
print('..........................................')
class remotecontrol:
  def __init__(self):
    self.channels=["hbo","abc","cnn","espn"]
    self.index=-1
  def __iter__(self):
    return self
  def __next__(self):
    self.index +=1
    if self.index==len(self.channels):
        raise StopIteration
    return self.channels[self.index]
r=remotecontrol()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))







