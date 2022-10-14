"""x=10




assert x>10 #AE


print(x)"""

"""x=10

assert x>10, 'x value >10 but it is not'

print(x)"""
def squareit(x):
    return x**x #x*x
assert squareit(2)==4,'the square of 2 should be 4'
assert squareit(3)==9,'the square of 3 should be 9'
assert squareit(4)==16,'the square of 4 should be 16'

print(squareit(2))
print(squareit(3))
print(squareit(4))

