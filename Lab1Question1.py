#Angelina Adamiec
#CS 113-OOP
#January 28,2022
#Question 1: A program that shows the subtotal, sales tax, and total of five items bought

price1 = int(input("Enter the price of item 1: "))
price2 = int(input("Enter price of item 2: "))
price3 = int(input("Enter price of item 3: "))
price4 = int(input("Enter price of item 4: "))
price5 = int(input("Enter price of item 5: "))
Subtotal = price1 + price2 + price3 + price4 + price5
currency = "${:,.2f}".format(Subtotal)
print("Subtotal:" ,currency)
SalesTax = Subtotal*.07
currency = "${:,.2f}".format(SalesTax)
print("Sales Tax:", currency)
Total = Subtotal + SalesTax
currency = "${:,.2f}".format(Total)
print("Total:", currency)
