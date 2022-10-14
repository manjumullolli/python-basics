"""def my_function():
    print("hello")
my_function()

def my_function(fname):
    print(fname+ ' lion ')
my_function("raju")
my_function("taje")
my_function("doju")

def my_function(fname,lname):
    print(fname + " " +lname)
my_function("raju","doju")

def my_function(*kids):
    print("the youngest chid is" + kids[3])
my_function("raju","boju","hjk","ijhi","ghhi")

def my_function( child1,child2,child3):
    print('the yongest child is ' + child1)
my_function(child1=" raju", child2="baju", child3="njj")

def my_function(**kid):
    print('the yongest child is ' + kid["lname"])
my_function(fname=" raju", lname="mhatre")


def my_function(contry="canada"):
    print("i am from" + " " + contry)
my_function("sweden")
my_function("nepal")
my_function("india")
my_function()
my_function("brazil")

def my_function(drinks):
    for x in drinks:
        print(x)
fruits=["apple","banana","cherry"]
my_function(fruits)

def my_function():
    pass

def greet(name):
    print("hello, " + name + " .good")
greet("paul")

def my_function():
    x=10
    print("value inside function:", x)
x=20
my_function()
print("value outside function:", x)

def absolute_value(num):
    if num>=0:
        return num
    else:
        return -num
print(absolute_value(8))
print(absolute_value(4))
print('................................................')
def sum(a,b):
    total=a+b
    return total
n=sum(5,4)
print('total:',n)"""


def calculate_total(exp):
    total=0
    for item in exp:
        total = total + item
    return total
tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,300,800]
toms_total=calculate_total(tom_exp_list)
joes_total=calculate_total(joe_exp_list)
print("tom's total expenses:",toms_total)
print("joe's total expenses:", joes_total)



