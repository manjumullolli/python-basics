import random
num=random.random()
print(num)

num=random.randint(10,20)
print(num)

num=random.randrange(100,200,2)
print(num)

num=random.uniform(50,70)
print(num)

numlist=random.sample(range(150,200),15)
print(numlist)

numlist=[1,2,3,4,5]
random.shuffle(numlist)
print(numlist)
print(random.choice(numlist))