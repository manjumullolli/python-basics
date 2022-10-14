import bisect
number=5
a=[1,2,4,6,7,8,9,34]
print(bisect.bisect(a, number))
bisect.insort(a, number)
print(a)