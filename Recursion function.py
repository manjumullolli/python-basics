# def greet():
#     print("hello")
#     greet()
# greet()


# import sys
# print(sys.getrecursionlimit())
# def greet():
#     print("hello")  #1000
#     greet()



# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# i=0
# def greet():
#     global i
#     i += 1
#     print("hello", i)
#     greet()
# greet()

#factorial usin recursion

def fact(n):
    if n == 0:# fact of 0 is 1
        return 1
    return n*fact(n-1)
result=fact(6)
print(result)