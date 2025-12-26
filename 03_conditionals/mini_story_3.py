# A tea stall offers different prices for differnt cup sizes , write a prograqm that calculates the price based on size. 
# Task : 
# Input : "small", "medium","large"
# Small : 10 , medium : 15 and large : 20 
# if invalid show "unknow cup size"


tea_input = input("Enter the chai size (Small/ Medium / Large)").lower()

if tea_input == "small":
    print("Price is 10 rupees")

elif tea_input == "medium":
    print("Price is 15 rupees")

elif tea_input == "large":
    print("Price is 20 rupees")

else :
    print("Unknow Cup Size")    
    