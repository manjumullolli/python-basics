import pickle,stu
with open('student.dat', mode='wb') as f:
    stu1=stu.student('Rahul',101,'Hubli')
    stu2=stu.student('rohit', 102, 'mysore')
    pickle.dump(stu1, f)
    pickle.dump(stu2, f)
    print('pickling done!!!')

with open('student.dat', mode='rb') as f:
    obj1=pickle.load(f)
    obj2=pickle.load(f)
    print('unpickling done')
    obj1.disp()
    obj2.disp()