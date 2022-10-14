#match function
import re
pattern = r"^abckk"
mystring ="abcll"
x= re.match(pattern,mystring)
print(x)
import re
pattern = r"^jksj"
mystring ="jksj"
x = re.match(pattern,mystring)
print(x)

#search function
txt= "we are learning python"
x= re.search("\s",txt)
print("the first whitespace : ", x) #or x.start()

import re
txt="rain in hubli"
x=re.search("goa",txt)
print(x)

#replace function
import re
str1="learnvern provide free online training"
print("before replace : ", str1)
result=re.sub(r"provide", "python" ,str1)
print(result)

import re
str1="Learnvern Provide Free Online Training"
result=re.sub(r"[a-z]", "0", str1)
print(result)
