# 5. Write a program to generate the sequence: –5, 10, –15, 20, –25….. upto n, where n is an integer input 
# by the user


n = int (input("Enter value of n"))

for index in range(1,n+1):
    if index % 2 != 0:
        print(-index * 5)
    else:
        print(index * 5)   