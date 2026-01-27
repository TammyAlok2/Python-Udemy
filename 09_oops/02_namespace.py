class Chai :
    origin = "India" # It is called properties 
    

print(Chai.origin)  

# We can add property in the class directly   
Chai.is_hot = True
print(Chai.is_hot)


# Creating object from class Chai 

masala = Chai()   

print(f"{masala.origin}")
print(f"{masala.is_hot}")


masala.is_hot = False
print(f"Changed Value in Object  {masala.is_hot}")

print(f"Chai is_hot property in Class =  {Chai.is_hot}")

# If we change or add property in object it does not appear on class because both has their own namespace 