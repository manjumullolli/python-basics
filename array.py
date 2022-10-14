#accessing elements of array
cars=["ford","volvo","bmw"]
print(cars)

import array as arr
a=arr.array('i',[2,4,6,8])
print("first element:", a[0])
print("second element:", a[1])
print("second last :", a[-1])

#modifying value
cars=["ford","volvo","bmw","maruti","tesla"]
cars[0]="toyota"
print(cars)

import array as arr
nos=arr.array('i',[1,2,3,4,5,6])
nos[0]=8
print(nos)
nos[3:5]=arr.array('i',[7,8,9])
print(nos)
nos.extend([9,9,9])
print(nos)


cars=["ford","volvo","bmw","maruti","tesla"]
x=len(cars)
print(x)
for x in cars:
    print(x)


cars=["ford","volvo","bmw","maruti","tesla"]
cars.append("honda")
print(cars)
cars.remove("volvo")
print(cars)


num_list=[2,5,65,25,41,78,55,56]
num=arr.array('i',num_list)
print(num[2:5])
print(num[:-5])
print(num[5:])
print(num[:])

import array as arr
num=arr.array('i',[1,2,3,4])
del num[3]
print(num)


import array as arr
odd=arr.array("i",[1,7,5])
even=arr.array("i",[4,5,6])
num=arr.array('i')
num=odd+even
print(num)












