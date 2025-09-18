# List in python 
indgridients = ["water", "milk", "tea leaves", "sugar"] 

# adding item in list 
indgridients.append("ginger")

# removing item from list 
indgridients.remove("sugar")

print(indgridients)

spice_options = ["cinnamon", "cardamom", "cloves", "nutmeg", "black pepper"]

chai_indgridients = ["Water","milk"]

# Adding one list in other list
chai_indgridients.extend(spice_options)

# to adding something at particular value 
spice_options.insert(2,"saffron")

# removing last element from the list 
last_added = spice_options.pop()
print(f"last added spice was : {last_added}")

# ro reverse the list 
spice_options.reverse()
print("f Reversed spice options are : ", spice_options)

# to sort the list permanently
spice_options.sort()
print("Sorted spice options are : ", spice_options)

# to sort the list temporarily
print("Temporarily sorted spice options are : ", sorted(spice_options))
print("Original spice options are : ", spice_options)

sugar_levels = [1,2,3,4,5]
print("Max sugar level is : ", max(sugar_levels))

print("Min sugar level is : ", min(sugar_levels))
print("Sum of sugar levels is : ", sum(sugar_levels))
print("Length of sugar levels is : ", len(sugar_levels))
print("Length of spice options is : ", len(spice_options))

# to find index of an item in list
print("Index of nutmeg is : ", spice_options.index("nutmeg"))

# to count how many times an item is present in list
print("Count of water in chai ingredients is : ", chai_indgridients.count("Water"))
print("Count of sugar in chai ingredients is : ", chai_indgridients.count("sugar"))

# to copy a list
new_spice_options = spice_options.copy()
print("New spice options are : ", new_spice_options)

# to clear a list
new_spice_options.clear()
print("New spice options after clear are : ", new_spice_options)

# to create a list of numbers
numbers = list(range(1,11))
print("List of numbers from 1 to 10 are : ", numbers)
numbers.sort(reverse=True)

print("List of numbers from 10 to 1 are : ", numbers)

# to create a list of even numbers
even_numbers = list(range(2,21,2))


# operator overloading 
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print("List after adding two lists : ", list3)

list4 = list1 * 3
print("List after multiplying list1 by 3 : ", list4)


# Bytearray in python
byte_array = bytearray("Hello World", "utf-8")
print("Byte array : ", byte_array)
print("Type of byte array : ", type(byte_array))


  
   