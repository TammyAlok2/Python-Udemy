# 8. Write a function that checks whether an input number is a palindrome or not.

def reverse_number(number):
    reverse = 0 
    while number >0:
        last_digit = number % 10 
        reverse = reverse * 10 + last_digit
        number = number //10 
    return reverse    
    

def check_palindrome(number):
    reversed_number = reverse_number(number)
    
    if number == reversed_number:
        print(f"The given number {number} is palindrome")
    else :
        print(f"The given number {number} is not palindrome")    


number = int(input("Enter the number "))

check_palindrome(number)