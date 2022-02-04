#Angelina Adamiec
#CS 113-OOP
#January 28,2022
#Question 2: A program that asks for purchase price and calculates taxes. And prints out the total of everything.

Purchase_amount = int(input("Enter the price of purchased items: "))
currency = "${:,.2f}".format(Purchase_amount)
print("Purchase amount:" ,currency)
State_Tax = 0.05
currency = '${:,.2f}'.format(5.00)
print("State Tax:" ,currency)
County_Tax = 0.025
currency = '${:,.2f}'.format(2.50)
print("County Tax:" ,currency)
Total_Tax = State_Tax + County_Tax
currency = "${:,.2f}".format(5.00 + 2.50)
print("Total Tax:", currency)
Sale_Total = Purchase_amount + Total_Tax
currency = "${:,.2f}".format(Purchase_amount + 7.50)
print("Sale Total:", currency)
