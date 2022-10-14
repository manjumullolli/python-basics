# import gc
# import time
#
# print(gc.isenabled())
#
# gc.disable()
# print(gc.isenabled())
#
# gc.enable()
# print(gc.isenabled())
#
# class test:
#     def __init__(self):
#         print('object initialization')
#     def __del__(self):
#         print('fulfilling last wish and performing cleanup activities...')
# t1=test()
# del t1
# print(t1)
import sys

print('...................')
# import time
# import gc
# class test:
#     def __init__(self):
#         print('object initialization')
#     def __del__(self):
#         print('fulfilling last wish and performing cleanup activities...')
# gc.disable()
# # print(gc.isenabled())
# t1=test()
# t1=None
# time.sleep(5)
# print('end of app')
print('...................')
# import time
# class test:
#     def __init__(self):
#         print('object initialization')
#     def __del__(self):
#         print('cleanup')
# t1=test()
# t2=t1
# t3=t2
# t4=t3
# del t1
# time.sleep(5)
# print('end app')
# del t2
# del t3
# time.sleep(5)
# print('still obj not eligible for gc')
# time.sleep(5)
# del t4
# time.sleep(5)
# print('end of app')
print('.................')
# import time
# class test:
#     def __init__(self):
#         print('obj ini')
#     def __del__(self):
#         print('cleanup')
# list=[test(),test(),test()]
# time.sleep(5)
# list=None
# time.sleep(5)
# print('end app')
# print('.....................')
import time
import sys
class test:
    def __init__(self):
        print('obj ini')
t1=test()
t2=t1
t3=t2
t4=t3
print(sys.getrefcount(t3))
