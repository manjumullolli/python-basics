set1=set() #creatng empty set
set2={'james',2,3,'python'}
print(set2) #printing set2
set2.add(10)#adding elements to set
print(set2)
set1.add(6)#adding elements to set
print(set1)
set2.remove(2)#Removing element from the set
print(set2)
set1.remove(6)
print(set1)

set={'apple','banana','cherry'}#create set
print(set)

set={'apple','banana','cherry','apple','grape'}#Duplicate values will be ignored:
print(set)
print(len(set))# to find length

set1 = {"abc", 34, True, 40, "male"} #A set with strings, integers and boolean values:
print(set1)

myset={"apple", "banana", "cherry"} # data type of a set
print(type(myset))


thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(thisset)

thisset = {"apple", "banana", "cherry"} #Check if "banana" is present in the set
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")#add orange
print(thisset)