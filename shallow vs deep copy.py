# lst1=[1,2,3,4]
# lst2=lst1
# print(lst2)
#
# lst2[1]=1000
# print(lst2)
# print(lst1)  #both variable in same mem location

#copy
#shallow copy
# lst1=[1,2,3,4]
# lst2=lst1.copy() #whenever use .copy it create diff mem loctn
# print(lst2)
#
# lst2[1]=1000
# print(lst2)
# print(lst1) #both having dii mem loctn

#shallow copy nested list
lst1=[[1,2,3,4], [5,6,7,8]]
lst2=lst1.copy()
print(lst1)
print(lst2)

lst1[1][0]=100
print(lst1)