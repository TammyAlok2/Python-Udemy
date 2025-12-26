# You run an onle tea store.
# If the order amout is more than 300 , delivery is free ;
# otherwise , it costs 30.

# Task :
#     input : order_tea
#     use ternary operator

order_amount = int(input("Enter the order amount"))

print(f"Order amount is :{order_amount} and type is {type(order_amount)}")

deliver_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is {deliver_fees}")
