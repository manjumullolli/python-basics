odd=[1,3,5,7,9]
even=[2,4,6,8,10]
# check=all([num%2 !=0 for num in odd])
check=any([num%2==0 for num in odd])
print(check)
