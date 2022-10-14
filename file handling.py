#file creating
s="im from hubli"
file=open("demo1.text","w")
file.write(s)
print("file created")
file.close()

#file read
file=open("demo1.text","r")
filecontent=file.read()
print(filecontent)

#write a list into file
L1=["pyt","java","php","angu"]
file=open("demo2.text","w")
file.writelines(L1)
print("file created")
file.close()

#read a list from file
file=open("demo2.text","r")
filelist=file.readlines()
print(filelist)

#appending a value into file
s="python file handling"
file=open("demo1.text","a")
file.write(s)
print("file updated")
file.close()