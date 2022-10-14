l1=[1,2,3,4,5]
print(l1)
print(type(l1))

r2=(1,2,3,4,5,6)
print(r2)
print(type(r2))

a = 50
b = a
print(id(a))
print(id(b))
# Reassigned variable a
a = 500
print(id(a))



# x=6
# print(x)
# del x
# print(x)

#type conversion
# a=str(input("enter the value of A : "))
# print("A :",a)
# print(type(a))

x, y, z =50, 55, 88
print(x,y,z)

x="python "
y="is "
z="awesome"
print(x+y+z)

x=55
def mainfunc():
    global x
print(x)
#modifying gobal x
x="welcome to python"
print(x)
mainfunc()
print(x)





