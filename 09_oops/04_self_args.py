class Chaicup :
    size = 140 # ml
    
    def describe(self):
        return f"A {self.size} ml chai cup "
    
    
cup = Chaicup()

print(cup.describe())        

print(Chaicup.describe()) # It gives error 

print(Chaicup.describe(cup)) # this will work fine because it has context of self (positional argurment)