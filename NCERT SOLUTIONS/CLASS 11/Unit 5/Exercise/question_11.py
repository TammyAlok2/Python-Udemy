# . Write a Python program to calculate the amount 
# payable if money has been lent on simple interest. 

# Principal or money lent = P, Rate of interest = R% 
# per annum and Time = T years. Then Simple Interest 
# (SI) = (P x R x T)/ 100. 
# Amount payable = Principal + SI. 
# P, R and T are given as input to the program

principal = 1000
rate = 4 
time = 2 
simple_interest = (principal * rate*time)/100
amount = principal + simple_interest

print("Simple Interest is ",simple_interest)
print("Amount is ",amount)