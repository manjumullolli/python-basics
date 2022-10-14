from threading import *
mt=current_thread()
print(mt.daemon)

# print(mt.isDaemon())
# print('...............................')
# from threading import *
# def job():
#     print('executed by child thread')
# t=Thread(target=job)
# print(t.isDaemon())
# t.setDaemon(True)
# print(t.isDaemon())
# print('.................................')
# from threading import *
# def job1():
#     print('executed by t1')
#     t2=Thread(target=job2)
#     print('t2 is daemon:', t2.isDaemon())
#     t2.start()
# def job2():
#     print('executed by t2')
# t1=Thread(target=job1)
# t1.setDaemon(True)
# print('t1 is daemon:', t1.isDaemon())
# t1.start()
print('........................................')
# from threading import *
# import time
# def job1():
#     print('executed by t1')
#     t2=Thread(target=job2)
#     print('t2 is daemon:',t2.isDaemon())
#     t2.start()
# def job2():
#     print('executed by t2')
# t1=Thread(target=job1)
# t1.setDaemon(True)
# print('t1 is daemon:',t1.isDaemon())
# t1.start()
# time.sleep(10)
from threading import *
import time
def job():
    for i in range(10):
        print('lazy thread')
        time.sleep(6)
t=Thread(target=job)
t.start()
time.sleep(5)
print('end of main thread')
