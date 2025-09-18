masala_spices = ("cardoman", "cloves","cinnamon")

print (masala_spices[0])
# unpacking the tuple in python 
(spice1, spice2, spice3) = masala_spices


print(f"Masala spices are {spice1}, {spice2}, {spice3}")

# swapping in python 
cardomon_ratio ,ginger_ratio = 2,4
print(f"Before swapping : cardomon ratio is {cardomon_ratio} and ginger ratio is {ginger_ratio}")
cardomon_ratio,ginger_ratio = ginger_ratio,cardomon_ratio
print(f"After swapping : cardomon ratio is {cardomon_ratio} and ginger ratio is {ginger_ratio}")

# membership testing in tuple 
print("cinnamon" in masala_spices)
print("nutmeg" in masala_spices)