"""class movie:
    '''ths ks dllkd ldldlld lddls sffff'''
    def __init__(self, title, hero, heroine):
        self.title= title
        self.hero= hero
        self.heroine= heroine
    def info(self):
        print('movie name :', self.title)
        print('hero name :', self.hero)
        print('heroine name :', self.heroine)
list_of_movies = []
while True:
    title = input('enter movie name:')
    hero = input('enter hero name')
    heroine = input('enter heroine name')
    m=movie(title,hero,heroine)
    list_of_movies.append(m)
    print('movie added successfully')
    option = input('do you want to add one more movie [yes/No]:')
    if option.lower() =='no':
        break
print('all movies information...')
for movie in list_of_movies:
    movie.info()
    print()"""

# self variable
class test:
    def __init__(self):
        print('the address of object pointed by self:',id(self))
t=test()
print('the address of object pointed by t:', id(t))

#################
"""class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def talk(self):
        print('hello i am:' , self.name)
        print('my rollno is:', self.rollno)
        print('my marks are:', self.marks)
s1=student('sunny',101,56)
s1.talk()"""

