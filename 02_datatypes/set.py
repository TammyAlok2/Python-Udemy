# set 
# defining a set 


essential_spices = {"cardamom","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

# Union of two sets
all_spices = essential_spices | optional_spices # Union of two sets It takes interesction element only one time 

print("All spices needed are : ", all_spices)

# Intersection of two sets 
common_spices = essential_spices & optional_spices # Intersection of two sets
print("Common spices are : ", common_spices)


# only in essential but not in optional
only_essential = essential_spices - optional_spices
print("Only essential spices are : ", only_essential)

# only in optional but not in essential
only_optional = optional_spices - essential_spices
print("Only optional spices are : ", only_optional)

# symmetric difference
symmetric_diff = essential_spices ^ optional_spices
print("Symmetric difference spices are : ", symmetric_diff)

# membership testing in set
print(f"Is 'cloves in essential spices ? : {'cloves' in essential_spices}   ")

# defining frozen set 
frozen_spices = frozenset(["turmeric","saffron","paprika"])
print("Frozen spices are : ", frozen_spices)

print (True and False)
print("Python"[0])