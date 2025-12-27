#Dictionary is the datatype in python used to store the data in key-value form and it mutable 
# Creating a dictionary
person ={
    "name": "John",
    "age": 30,
    "city": "New York"
    
}

chai_order = dict(type= "Masala Chai",size= "Large",sugar_level= 3  )
print("person dictionary:", person)
print("chai_order dictionary:", chai_order)

# Accessing values in dictionary 
print("Name:", person["name"])
print("Age:", person.get("age"))
print("City:", person["city"])

# Adding key value pair in the dictirary 

person["gender"] = "male"
person["number"] = 9890
print(person,'Whole set of person ')


# deleting data from the dictionary 
del person["age"]


print(person , 'Deleted age from the dictionary ')

# checking the membership testing in dicrionary 
print("Is age of 20 present ", 'age' in person)

print(f"Order details (Keys) : {chai_order.keys()} ")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items):{chai_order.items()}")

# removing last item from the dictionary 
last_item = chai_order.popitem()
print('Removed last item ,',last_item)

# Adding more elements to the dictionary
extra_spices = {"cardoman":"crushed","ginger":"sliced"}
chai_order.update(extra_spices)

print(f"Updated Chai Recepie :{chai_order}") 

chai_size = chai_order["size"]
customer_node = chai_order.get("note ","No note")
print(f"Chai size is : {chai_size}")
print(f"Customer node is {customer_node}")