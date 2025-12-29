# Write a program that prints minimum and maximum 
# of five numbers entered by the user.

numbers = [1,2,3,4,5]

def find_maximum(numbers):
    maximum = -1
    for number in numbers:
        if number > maximum :
            maximum = number 
    return maximum 

def find_minimum (numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum :
            minimum = number         
    return minimum        



minimum_number = find_minimum(numbers)
maximum_number = find_maximum(numbers)
print(f"Maximum number is {maximum_number} and minimum number is {minimum_number}")
 