#to implement countdown
"""import time
def countdown(num):
    print('countdown starting....')
    while num>0:
        yield num
        num=num-1
values=countdown(5)
for x in values:
    print(x)
    time.sleep(3)"""
#to generate first n numbers
"""def firstn(num):
    n=1
    while n<=num:
        yield n
        n=n+1
for x in firstn(10):
    print(x)"""
#to generate fibonacci number
"""def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for n in fib():
    if n>100:
        break
    print(n)"""
print('.......................................')
import random
import time

names=['raj','vk','dk','mk']
subjects=['java','php','django']

def people_list(num):
    results=[]
    for i in range(num):
        person={
            'id':i,
            'name':random.choice(names),
            'subject':random.choice(subjects)
            }
        results.append(person)
    return results
t1=time.clock()
people=people_list(100000)
t2=time.clock()
print('time taken:',t2-t1)