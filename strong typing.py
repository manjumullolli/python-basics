class duck:
    def walk(self):
        print('tapak tapak')
class horse:
    def walk(self):
        print('tabdak tabdak')
class cat:
    def talk(self):
        print('mew mew')
def myfun(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()
d=duck()
myfun(d)
h=horse()
myfun(h)
c=cat()
myfun(c)
