#namedtuple returns a tuple with a named value for each elements in the tuple.
# from collections import namedtuple
# a=namedtuple('course', 'name, technology')
# s=a('ai', 'python')
# print(s)
# s=a._make(['ai', 'java'])
# print(s)
# print()
# from collections import namedtuple
# point=namedtuple('point', 'x,y')
# pt=point(1,5)
# print(pt)
# print(pt.x, pt.y)

print('..................')
#Deque is an optimised list to perform insertion and deletion easily
# from collections import deque
# a=['a', 'b', 'd', 'h', 'r', 't', 'p']
# d=deque(a)
# print(d)
# d.append('java')
# print(d)
# d.popleft()
# print(d)
# print()
# from collections import deque
# d=deque()
# print(d)
# d.append(1)
# d.append(2)
# print(d)
# d.appendleft(3)
# print(d)
# d.rotate(2)
# print(d)
# d.pop()
# print(d)
# d.extendleft([4,5,6])
# print(d)
print('......................')
#chainmap is adictionary like class for creating a single view of multiple mappings
# from collections import ChainMap
# a={1:'java', 2:'php'}
# b={3:'css', 4:'html'}
# c=ChainMap(a,b)
# print(c)
print()

#counter is a dict subclass for counting hashable objects
# from collections import Counter
# a=[1,1,2,3,2,2,4,5,4,3,6,2,2]
# c=Counter(a)
# print(c)
# print(list(c.elements()))
# print(c.most_common())
# sub={2:1, 6:1}
# print(c.subtract(sub))
# print(c.most_common())
#
# print()
# from collections import  Counter
# a="aaaaabbbbccc"
# my_counter=Counter(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common(3))
# print(my_counter.most_common(1)[0][0])
# print(list(my_counter.elements()))
print('................')

#orderedDict is dict subclass which remember the order in which the entries were done.
from collections import OrderedDict
d=OrderedDict()
d[1]='e'
d[2]='m'
d[3]='g'
d[4]='t'
d[5]='h'
print(d)
print(d.keys())
print(d.values())
#to change value
d[1]='p'
print(d)

from collections import OrderedDict
o=OrderedDict()
# o={}
o['a']=1
o['b']=2
o['c']=3
o['d']=4
print(o)