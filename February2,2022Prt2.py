#Angelina Adamiec
#February 2, 2022
#CS 113-OOP
#A program that asks for a four digit number and then prints the sum of each digit in the four digit number

number = int(input("Input a four digit numbers: "))
sum = 0
for num in str(number):
    sum = sum + int(num)
print("The sum is", sum)
