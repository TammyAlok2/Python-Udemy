flavors = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavor in flavors:
    if flavor == "Out of Stock":
        continue
    if flavor == "Discontinued":
        print(f"{flavor} item found ")
        break
    print(f"{flavor} item found ")
    
print(f"Out side of loop")   


 
