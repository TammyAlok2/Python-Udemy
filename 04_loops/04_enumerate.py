menu = ["Green","Lemon","Spiced","Mint"]
# for m in menu :
#     print(f"Menu item is {m}")
    
#  You are creating a tea menu board .
#  Each item must be numbered . 
# Task : 
# . Use enumerate() to print menu items with numbers 

for index,item in enumerate(menu,start=1): # Enumerate return tuple
    print(f'{index} is {item}')

 