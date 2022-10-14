# number data type
a=5
print(type(a))
b=40.5
print(type(b))
c=1+5j
print(type(c))
print("c is complex number", isinstance(1+5j,complex))

x=1
y=2.55
z=1j
# convert from int to float
a= float(x)
# convert from float to int
b=int(y)
# convert from int to complex
c=complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1,10))



# sequence data type
a="hello"
print(a)
str="india is my country"
print(str)
a="""mkjkk kkdkd kjjj
jdjk jkkkkk dkkkd
djkkd kkkkd,dd
d"""
print(a)
a="hello ckm"
print(a[3])
str1="hello javatpoint"
str2="hello python"
print(str1[0:2])
print(str1[4:])
print(str1*2)
print(str1+str2)

for x in "banana":
    print(x)

a="hello, world!"
print(len(a))
print(a[-5:-2])


a="hello, world!"
print(a.upper())

b="HI HOW R U"
print(b.lower())

#strip() method removes any whitespace from the beginning or the end:
a="  hello, world!  "
print(a.strip())

#replace string
a='hello, world'
print(a.replace('h', 'd'))

#split string
a="hello, world"
print(a.split())


#lists
disk=[1,"hi","pyt",5]
print(type(disk))
print(disk)
print(disk[1:3])
print(disk+disk)
print(disk*3)

#list length
thislist=["apple",2,4,"banana","cherry"]
print(len(thislist))

#list constructor
disk=list(("apple",'banana',"cherry"))
print(disk)

#access items
list=["apple","banana","cherry","mango","grapes"]
print(list[2])
print(list[-2])
print(list[2:5])
print(list[:4])
print(list[2:])
print(list[-4:-1])
if "apple in list":
    print("yes, 'apple' is in the list")

    # change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#tuple
tup=("apple",2,3,4,"banana","cherry")
print(type(tup))
print(tup)
print(tup[1:4])
print(tup*3)

#dictonary
d={1:"jimmy", 2:'alex', 3:"raju", 4:"gff", 5:"hg"}
print(d)
print("the first name is: " + d[1])
print(d.keys())
print(d.values())

#boolean
d=True
print(type(d))
e=False
print(type(e))


#set

thislist={"apple",2,"banana","cherry","grape","orange",}
print(thislist)
print(len(thislist))
for x in thislist:
    print(x)
print("banana" in thislist)
thislist.add("mango")
print(thislist)



