#Angelina Adamiec
#February 2, 2022
#CS 113-OOP
#A program that calculates the compound interest of a loan

P = float(input('Enter the initial principal balance (loan amount): $'))
r = float(input('Enter the interest rate:  '))
n = float(input('Enter the number of times interest applied per time period:'))
t = float(input('Enter the number of time periods elapsed: '))


A = P * ((1 + (r / n))**(n * t))
currency = "${:,.2f}".format(A)
print('After ', t, ' years, you have paid', currency )
