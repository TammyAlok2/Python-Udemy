# List operator overloading in python
base_liquid = ["water", "milk"]
extra_flavors = ["sugar", "honey"]

full_liquid = base_liquid + extra_flavors

print("Full liquid ingredients:", full_liquid)

strong_brew = ["black tea"] * 3
print("Strong brew ingredients:", strong_brew)


strong_full_brew = ["black tea","green tea"] * 2
print("Strong full brew ingredients:", strong_full_brew)

# from operator import itm 
# combined_ingredients = itm.add(base_liquid, extra_flavors)
# print("Combined ingredients using operator module:", combined_ingredients)


# converting string to list 
tea_string = "water, milk, tea leaves, sugar"
tea_list = tea_string.split(", ")
print("Tea ingredients list from string:", tea_list)

# converting list to string
joined_tea_string = ", ".join(tea_list)
print("Joined tea ingredients string:", joined_tea_string)

# concept of bytearray 
raw_spice_data = bytearray(b"cinnamon, cardamom, cloves")
print("Raw spice data bytearray:", raw_spice_data)