# Write a program to swap two number without using third variable 
a =9
b = 50

print(f"Value before swapping a = {a} , b ={b}")

a = a + b 
b = a - b 
a = a - b 

print (f"Value after swapping a = {a} , b= {b}")

