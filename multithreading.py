"""from Threading import *
def display():
    for i in range(10):
        print('child thread')
t=Thread(target=display)
t.start()
for i in range(10):
    print('main thread')"""

"""from threading import *
class myThread():
    def run(self):
        for i in range(10):
            print('child thread')
t=myThread()
t.start()
for i in range(10):
    print('main thread')"""
"""from threading import *
def display():
    for i in range(10):
        print('child thread')
t=Thread(target=display)
t.start()
for i in range(10):
    print('main thread')"""
"""from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print('child thread')
t=MyThread()
t.start()
for i in range(10):
    print('main thread')"""
"""from threading import *
class test:
    def m1(self):
        for i in range(10):
            print('child thread-1')
obj=test()
t=Thread(target=obj.m1)
t.start()
for i in range(10):
    print('main thread-1')"""
"""import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('double value',2*n)
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('square vale',n*n)
numbers=[1,2,3,4,5,6]
begintime=time.time()
doubles(numbers)
squares(numbers)
endtime=time.time()
print('total time taken:',endtime-begintime)
"""
"""import time
from threading import *
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('double value:',2*n)
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('square value:',n*n)
numbers=[1,2,3,4,5,6]
begintime=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print('total time taken:',endtime-begintime)"""
#setting and getting name of thread:
"""from threading import *
print(current_thread().name)
current_thread().name='durga'
print(current_thread().name)
#thread identification number:
from threading import *
def test():
    print('child thread')
t=Thread(target=test)
t.start()
print('main thread identification number:',current_thread().ident)
print('child thread identification number:',t.ident)
"""
#active_count:
"""from threading import *
import time
def display():
    print(current_thread(),'...started')
    time.sleep(3)
    print(current_thread(),'....ended')
print('the number of active threads:',active_count())
t1=Thread(target=display,name='childthread-1')
t2=Thread(target=display,name='childthread-2')
t3=Thread(target=display,name='childthread-3')
t1.start()
t2.start()
t3.start()
print('the number of active threads:',active_count())
time.sleep(10)
print('the number of active threads:',active_count())"""
#enumerate:
"""from threading import *
import time
def display():
    print(current_thread(),'...started')
    time.sleep(3)
    print(current_thread(),'....ended')
print('the number of active threads:',active_count())
t1=Thread(target=display,name='childthread-1')
t2=Thread(target=display,name='childthread-2')
t3=Thread(target=display,name='childthread-3')
t1.start()
t2.start()
t3.start()
l=enumerate()
for t in l:
    print('Thread name:',t.name)
    print('Thread identification number:',t.ident)
    print()
time.sleep(10)
l=enumerate()
for t in l:
    print('Thread name:',t.name)
    print('Thread identification number:',t.ident)
    print()"""
#isAlive:
"""from threading import *
import time
def display():
    print(current_thread().name,'...started')
    time.sleep(3)
    print(current_thread().name,'....ended')

t1=Thread(target=display,name='childthread-1')
t2=Thread(target=display,name='childthread-2')
t1.start()
t2.start()
print(t1.name,'is Alive:',t1.is_alive())
print(t2.name,'is Alive:',t2.is_alive())
time.sleep(10)
print(t1.name,'is Alive:',t1.is_alive())
print(t2.name,'is Alive:',t2.is_alive())"""
#join method:
from threading import *
import time
def display():
    for i in range(10):
        print('seetha thread')
        time.sleep(3)
t=Thread(target=display)
t.start()
t.join(10)
for i in range(10):
    print('rama thread')

