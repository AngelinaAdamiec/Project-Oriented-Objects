#Angelina Adamiec
#CS 113-OOP
#January 28,2022
#A program that displays the information of stock info Joe has
# Not sure how to get the $535 for the end amount to determine if he made a profit or not. 

Commission_of_stockbroker = .03

amount_of_shares_sold = amount_of_shares_purchased = 2000
each_shares_price = 40.00

amount_paid = amount_of_shares_purchased * each_shares_price
currency = "${:,.2f}".format(amount_paid)
print('\nAmount of money paid for the stock = $', currency)

amount_of_commission_when_purchased = amount_paid * Commission_of_stockbroker
currency = "${:,.2f}".format(amount_of_commission_when_purchased)
print('Amount of commission paid to broker when Joe bought the stock = $', currency)

price_each_share = 42.75

amount_stock_sold_for = amount_of_shares_sold * price_each_share
currency = "${:,.2f}".format(amount_stock_sold_for)
print('Amount for which Joe sold the stock = $', currency)

commission_amount_paid_when_sold = amount_stock_sold_for * Commission_of_stockbroker
currency = "${:,.2f}".format(commission_amount_paid_when_sold)
print('Amount of commission paid to broker when Joe sold the stock = $', currency)

total_amount_left1 = amount_stock_sold_for - \
                   (amount_of_commission_when_purchased + \
                    commission_amount_paid_when_sold)
currency = "${:,.2f}".format(total_amount_left1)
print('\nTotal leftover =', currency)
