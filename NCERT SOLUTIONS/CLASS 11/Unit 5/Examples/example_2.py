# Program to print the positive difference of two numbers 

num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))

if(num1>num2):
    diff = num1-num2
else:
    diff = num2-num1

print(f"The difference btw {num1} and {num2} is {diff}")    
        