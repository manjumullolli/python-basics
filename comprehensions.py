list_1=[1,2,32,4,5,45,3,3,3,5,6,7,343,353,5,4,9,6]
divide_by_3 = []
for item in list_1:
    if item%3==0:
        divide_by_3.append(item)
print('without using list comprehension', divide_by_3)
print('using list comprehension',[item for item in list_1 if item%3==0])
print('..........................................')
dict1={'a':45,'b':20,'A':5}
print({k.lower():dict1.get(k.lower(),0)+dict1.get(k.upper(),0) for k in dict1.keys()})
print({k.upper():dict1.get(k.upper(),0)+dict1.get(k.lower(),0) for k in dict1.keys()})
print('..............................................')
squared={x**2 for x in [1,2,3,4,5,2,2,3,3,4,5,6]}
print(squared)
print('..........................................')
"""gen = (i for i in range(56) if i%3==0)
for item in gen:
    print(item)
"""
