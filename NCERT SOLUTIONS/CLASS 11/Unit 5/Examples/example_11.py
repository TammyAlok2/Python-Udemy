# Program to find the factors of a whole number using while loop 

num = int(input("enter the number"))

count = 2
print(1,'is a factor') 

while count <= num/2:
    if num % count == 0 :
        print(count,'is a factor')
    count+=1

print(num,'is a factor')            