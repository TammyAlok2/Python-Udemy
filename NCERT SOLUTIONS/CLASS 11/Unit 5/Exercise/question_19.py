# Write a program that asks the user to enter their name and age. Print a message addressed to the user tell the user the year inw which they will turn 100 year old 

# name = input("Enter your name")
# age = int(input("Enter your age"))



from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = datetime.now().year
year_100 = current_year + (100 - age)

print(f"Hello {name}, you will turn 100 years old in {year_100}.")
