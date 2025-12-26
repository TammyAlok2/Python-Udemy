# You are building a smart thermostat alert system : 
# if the device_status is active : 
# And temperatur > 35 Warn : "High temperatur "
# Else : "Temperature normal "
# If device is off : "Device is offline"


device_status = input("Enter device status (Online / offline) ").lower()
temperture = input ("Enter the temperature").isnumeric()

if device_status =="online":
    if temperture > 35 :
        print("High temperature ")
    
    else :
        print("Temperature normal ") 

else :
    print("Device is Offline")        
           