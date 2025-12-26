# A local cafe wants a program that suggst a snack. if acustomer asks for cookies or samosa ,it confims the order , other wise , it says it's not available 
# Task : 
# take snack input 
# if it's "cookies" or samosa  confirm the order 
# else , show unavailablilty 

snack_input = input ("Enter your Preferred snack ").lower()
print (f"User said : {snack_input}")

if snack_input == "cookies" or snack_input == "samosa":
    print(f"Your order is confirmed :{snack_input} ! We will serve you within 15 minutes")

else:
    print("Oops , we only serve cookies or samosaa")

        

