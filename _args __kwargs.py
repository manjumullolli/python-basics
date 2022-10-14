# def function_1(name,age,rollno):
#     print("the name of std is",name,"and age is",age,"and rollno is",rollno)
# function_1("raj",25,401)
# def fun(*args):
#     print(type(args))
#     print("the name of std is",args[0],"and age is",args[1],"and rollno is",args[2])
# fun('raj',25,405)
"""def fun(*args):
    if(len(args)==3):
        print("the name of std is",args[0],"and age is",args[1],"and rollno is",args[2])
    else:
        print("the name of std is",args[0],"and age is",args[1])
    lis=['harry']
# fun('harry',25,265)
lis=['raj',25,656]
fun(*lis)"""
"""def printmarks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key,value)
marklist={"rohan das":98,"harry das":96,"mohan raj":55}
printmarks(**marklist)"""
def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)
lis=["harry,22,256"]
marklist={"rohan das":98,"harry das":96,"mohan raj":55}
print(master('normal',*lis,**marklist))

