"""class outer():
    def __init__(self):
        print('outer object creator')
    class inner:
        def __init__(self):
            print('inner class object creator...')
        def m1(self):
            print('inner class method')
o=outer()
i=o.inner()
i.m1()
#or
i=outer().inner().m1()"""

class outer:
    def __init__(self):
        print('outer class obj creation..')
    class inner:
        def __init__(self):
            print('inner class obj...')
        class innerinner:
            def __init__(self):
                print('inner inner class')
            @staticmethod
            def m1():
                print('nested inner class')
"""o=outer()
i=o.inner()
ii=i.innerinner()
ii.m1()"""
outer().inner().innerinner.m1()
