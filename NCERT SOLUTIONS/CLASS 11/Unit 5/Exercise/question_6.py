# 6. Write a program to find the sum of 1+ 1/8 + 1/27......1/n3, where n is the number input by the user

n = int(input("Enter the value of n "))

total_sum = 0.0
for k in range(1, n + 1):
    total_sum += 1 / (k ** 3)

print(f"The sum is {abs(total_sum)}")











