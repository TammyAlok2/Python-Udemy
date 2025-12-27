# Zip iterate over several iterables in parallel ,producing tuples iwth an item from every one.

# You are preparing an order summary with customer names and thier total bill .
# Task : 
# . Use two lists : one for names and one for bills 
# . Print "[Name] paid [amount]"


names = ["hitesh","meera","sam","ali"]

bills = [50,70,100,55]

for name,amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")


