# with open('student.txt', 'w') as f:
#     f.write('hello')
print('....................')
# class ContextManager():
#     def __init__(self):
#         print('init method called')
#
#     def __enter__(self):
#         print('enter method called')
#         return self
#
#     def __exit__(self, exc_type, exc_value, exc_traceback): #manage exception
#         print('exit method called')
#
#
# with ContextManager() as manager:
#     print('with statement block')
print('...............')


class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# loading a file
with FileManager('student.txt', 'w') as f:
    f.write('Test')

print(f.closed)