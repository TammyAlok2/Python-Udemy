# Question : Customer Profile Management
# You are building a customer profile manager for a CRM (Customer Relationship Management) system. You need to store and manipulate customer data using Python dictionaries.

# Tasks:

# Create a dictionary named customer with the following fields:

# "name": "John Doe"

# "age": 32

# "city": "New York"

# Print the dictionary.

# Add "email" and "phone" to the dictionary.

# Print the updated dictionary.

# Print the customer’s "name" and "city" values.

# Check whether the key "email" exists in the dictionary and print the result.

# Delete the "age" field from the dictionary.

# Print the updated dictionary.

# Print all dictionary keys, values, and items.

# Remove and print the last inserted key-value pair.

# Use .get() to access the key "membership" (which doesn’t exist).

# Print the result.

# Update the dictionary with a new field "address" set to "221B Baker Street".

# Print the final dictionary.





# Step 1: Create a customer dictionary with name, age, and city
customer = {
    "name": "John Doe",
    "age": 32,
    "city": "New York"
}
print(customer)

# Step 2: Add email and phone
customer["email"] = "john.doe@example.com"
customer["phone"] = '123-456-7890'
print(customer)


# Step 3: Print customer's name and city
print(customer["name"])
print(customer['city'])

# Step 4: Check if "email" exists
print('email' in customer)

# Step 5: Delete the "age" field
del customer['age']
print(customer)

# Step 6: Print all keys, values, and items
print(customer.keys())
print(customer.values())
print(customer.items())
# Step 7: Remove and print the last inserted item
del_item = customer.popitem()
print(del_item)

# Step 8: Use .get() to access "membership"
member = customer.get("membership")
print(member)

# Step 9: Update dictionary with "address"
customer["address"] = "221B Baker Street"

# Step 10: Print final dictionary
print(customer)
