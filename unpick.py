#unpick
#reading object from the file
import pickle, stu
with open('student.dat', mode='rb') as f:
    while True:
        try:
            obj=pickle.load(f)
            obj.disp()
        except EOFError:
            print('done')
            break