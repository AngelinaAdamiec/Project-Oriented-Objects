#Angelina Adamiec
#CS 113-OOP
#January 28,2022
#A program that calculates the balance of the account after specific amount of years

P = float(input('Enter principal amount: $'))
r = float(input('Enter annual interest rate: '))
n = float(input('Enter number of times per year interest has compounded: '))
t = float(input('Enter number of years account will be left to earn interest: '))

r /= 100 # 50% = .50
A = P * ((1 + (r / n))**(n * t))
currency = "${:,.2f}".format(A)
print('After ', t, ' years, there will be', currency , 'in the account')
