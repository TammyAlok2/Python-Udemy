# List are the mutable datatype in python 
ingredients = ["water","milk","black tea"]

print(ingredients)

# Adding new element in the last of the list 
ingredients.append("sugar")
print(f"Ingredients are : {ingredients}")


# Deleting the particular element 
ingredients.remove("water")
print(f" Updated Ingredients are : {ingredients}")

# Adding a list into another list 
spice_options = ["ginger","Cardomon"]
ingredients.extend(spice_options)
print(f" Ingredients after adding spice options : {ingredients}")

# Adding element at particular index
ingredients.insert(1,"honey")
print(f" Ingredients after adding honey at index 1 : {ingredients}")

# Removing last element froom the list 
popped_ingredient = ingredients.pop()
print(f"Popped ingredient is : {popped_ingredient}")

# Reversing whole list 
print(f"Reversed list is : {ingredients.reverse()}") # output is None because reverse() modifies the list in place
ingredients.reverse()  # reversing again to show the reversed list
print(f" Reversed Ingredients are : {ingredients}")

# Deleting the particular index element
del ingredients[2]
print(f" Ingredients after deleting index 2 element : {ingredients}")

# Sorting the list permanently 
ingredients.sort()
print(f"Sorted Ingredients are : {ingredients}")

# making a swallow copy of the list
new_ingredients = ingredients.copy()
print(f"New Ingredients are : {new_ingredients}")

# making a deep copy of the list using list() function
deep_copied_ingredients = list(ingredients)
print(f"Deep Copied Ingredients are : {deep_copied_ingredients}")
# Clearing the whole list
new_ingredients.clear()
print(f"New Ingredients after clear are : {new_ingredients}")
# Finding length of the list
print(f"Length of ingredients list is : {len(ingredients)}")


sugar_levels = [1,2,3,4,5]
print(f"Max sugar level is : {max(sugar_levels)}")
print(f"Min sugar level is : {min(sugar_levels)}")
print(f"Sum of sugar levels is : {sum(sugar_levels)}")
print(f"Length of sugar levels is : {len(sugar_levels)}")
# Finding index of an item in the list
print(f"Index of honey in ingredients is : {ingredients.index('honey')}")