#Angelina Adamiec
#CS 113-OOP
#January 28,2022
#Question 2: A program that asks for number of cookies and then displays the amount of ingredients needed

cookies = float(input('Enter number of cookies: '))
Sugar = 1.5
Butter = 1.0
Flour = 2.75
Cookies_made_by_recipe = 48
required_sugar = (cookies * Sugar) / Cookies_made_by_recipe
required_butter = (cookies * Butter) / Cookies_made_by_recipe
required_flour = (cookies * Flour) / Cookies_made_by_recipe
print('\n'"To make " + str(round(cookies,2)) + " cookies, you will need: \n")
print(str(round(required_sugar,2)) + " cups of sugar \n")
print(str(round(required_butter,2)) + " cups of butter \n")
print(str(round(required_flour,2)) + " cups of flour \n")
