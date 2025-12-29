# Write a program to create a simple  calculator . perfomring only four basic operation 

val1 = float(input("Enter value 1"))
val2 = float(input("enter value 2"))
result = 0

op = input("Enter any one of the operator (+,-,*,/)")

if op =='+':
    result = val1 +val2

elif op =='-':
    result = val1-val2

elif op =='*':
    result = val1 * val2

elif op =='/':
    if val2 == 0:
        print("Error ! Division by zero is not allowed , program terminate")
    else:
        result = val1/val2     
else:
    print("Wrong input , program terminated")


print("the result is ",result)