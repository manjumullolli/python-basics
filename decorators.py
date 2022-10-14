"""def dec1(fun1):
    def nowexe():
        print('executing now')
        fun1()
        print('executed')
    return nowexe

@dec1
def who_is_harry():
    print('boy')
who_is_harry()"""
def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div=smart_div(div)
div(2,4)