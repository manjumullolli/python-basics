import os
w=os.walk('yourdir', topdown=True)
for i in w:
    print(i)