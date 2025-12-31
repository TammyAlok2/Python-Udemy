# 7. Write a program to find the sum of digits of an 
# integer number, input by the user.

def sum_of_digits(number):
    sum =0 
    while(number >0):
        last_digit = number % 10 
        sum = sum + last_digit
        number = number //10  # V IMP  here to get integer section only
    return sum     

number = int(input("Enter your number "))

sum_digits = sum_of_digits(number)

print(f"Sum of digits of number {number} is {sum_digits}")