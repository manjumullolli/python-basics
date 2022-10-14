#pick.py
#storing oject in the file

import pickle,stu
n=int(input('enter number of students: '))
with open('student.dat', mode='wb') as f:
    for i in range(n):
        name=input('enter student name: ')
        roll=int(input('enter roll'))
        address=input('enter address')
        stu1=stu.student(name,roll,address)
        pickle.dump(stu1, f)

print('pickling done!!!')