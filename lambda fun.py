#syn: lambda arguments: expn
x=lambda a: a+10
print(x(6))

x=lambda a,b: a*b
print(x(4,5))

x=lambda a,b,c: a+b+c
print(x(5,7,6))

def myfun(n):
    return lambda a: a*n
mydoubler=myfun(2)
print(mydoubler(11))

def myfun(n):
    return lambda a: a*n
mytripler=myfun(3)
print(mytripler(11))

def myfun(n):
    return lambda a: a*n
mydoubler=myfun(2)
mytripler=myfun(3)
print(mydoubler(11))
print(mytripler(22))

double=lambda n:n*2
print(double(5))

larger=lambda a,b: a if(a>b) else b
print(larger(4,9))

names=["abb","dddd","mmm","yyy","ff","nnn","ssss"]
names.sort(key=lambda x: len(x))
print(names)


l=[1,2,3,4,5]
def squareit(n):
    return n*n
l1=list(map(squareit,l))
print(l1)

l=[1,2,3,4,5]
l1=list(map( lambda n:n*n,l))
print(l1)

l1=[1,2,3,4,5,6]
l2=[5,8,9,6,5,4]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)

#list_ = [34, 12, 64, 55, 75, 13, 63]

#odd_list = list(filter(lambda num: (num % 2 != 0), list_))

#print(odd_list)

list1 = [34,55,64,15,63,62]
odd_list = list(filter(lambda num: (num % 2 != 0),list1))
print(odd_list)