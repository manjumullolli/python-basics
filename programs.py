"""#addition
num1=12
num2=15
sum= num1+num2
print("sum of {0} and {1} is {2}".format(num1,num2, sum))

#user input
# num1 = input(" first num is : ")
# num2 = input(" second num is : ")
# sum = int(num1) + int(num2)
# print("the sum of {0} and {1} is {2}".format(num1, num2, sum))

#driver code

num1 = 20
num2 = 25

    # Adding two numbers
sum = lambda num1, num2 : num1 + num2

    # printing values
print("Sum of {0} and {1} is {2};".format(num1, num2, sum(num1, num2)))"""
print('................................................................................')
#factorial of given number
"""def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);


# Driver Code
n = 5;
print("Factorial of", n, "is",
      factorial(n))"""
print('.................................................')

def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while(n>1):
            fact=fact*n
            n-=1
        return fact
num=5
print('factorial of',num,'is',factorial(num))