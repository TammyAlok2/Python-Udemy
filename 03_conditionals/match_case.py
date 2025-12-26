#  You are building a ticket info system for arailway app. 
#  Based on seat type , show this features  
#  Task: 
#      Input : Sleeper , ac ,general ,luxurly 
#      match using match case 
#      unknown : show "Invalid seat type "

seat_type= input("Enter seat type (sleeper/AC/general/luxury)").lower()

print(seat_type)

match seat_type :
    case "sleeper":
        print("Sleeper - No AC, beds are available")
    
    case "ac":
        print("A.C , Great choice but missed luxury")    
    
    case "luxury":
        print("Luxury, Great Choice , you are great")    
    
    case "general":
        print("General - Worst Choice")
       
    case _:
        print("Invalid Seat Type")        

