"""from sys import argv
print(argv[0])
print(argv[1])
print(argv[2])
print(argv)
print(type(argv))
"""
"""from sys import argv
print('the no of cmd line arguments:', len(argv))
print('the list of cmd line arguments:',argv)
print('the cmd line arguments one by one:')
for x in argv:
    print(x)"""
from sys import argv
args=argv[1:]
sum=0
for x in args:
    sum=sum+int(x)
print('the sum:',sum)
