'''

'''





users=['rohan das', 'subham', 'chotu', 'motu']
computer=['rasberry pi', 'android','iphone','100rs']
# for i in range(0, len(users)):
#     print("computer used by",users[i],"is",computer[i])
for i in range(0, len(users)):
    template = 'computer used by {0} is {1}'
    print(template.format(users[i], computer[i]))