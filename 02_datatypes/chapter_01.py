sugar_amount = 10 
print(f"Intial sugar amount: {sugar_amount} grams")
sugar_amount = 12
print(f"Updated sugar amount: {sugar_amount} grams")

# numbers are immutable, so we cannot change the value of a number directly
print(f"Id of 10: {id(10)}")
print(f"Id of 12: {id(12)}")

# Both id are different, so we can say that numbers are immutable 
sugar  =1 
print ("sugar intialize with ",sugar)
print(f"id of 1 : {id(1)}")
sugar = 2 
print(f"id of 2 : {id(2)}")
print ("sugar finalize  with ",sugar)