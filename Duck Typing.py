class duck:
    def walk(self):
        print('tapak tapak')
class horse:
    def talk(self):
        print('tabdak tabdak')
class cat:
    def walk(self):
        print('mew mew')
def myfun(obj):
    obj.walk()
d=duck()
h=horse()
c=cat()
myfun(c)
