class customer():
    '''customer class devloped by durga for bank operations'''
    bankname='durgabank'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('balance after deposit:',self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print('insufficient balance')
        else:
            self.balance=self.balance-amount
            print('balance after withdraw:',self.balance)

print('welcome to',customer.bankname)
name=input('enter your name:')
c=customer(name)
while True:
    print('d-deposit \nw-withdraw\n e-exit')
    option=input('choose your option:')
    if option.lower()=='d':
        amount=float(input('enter amount to deposit:'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input('enter amount to withdraw:'))
        c.withdraw(amount)
    elif option.lower()=='e':
        print('thanks for banking')
        break
    else:
        print('please choose valid option')
