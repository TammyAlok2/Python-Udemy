def calculate_bills(cups,price_per_cup):
    return  cups * price_per_cup


bills = calculate_bills(3,15)
print(bills)

print("Order for table 2: ",calculate_bills(2,50))
print("Order for table 3:", calculate_bills(3,50))