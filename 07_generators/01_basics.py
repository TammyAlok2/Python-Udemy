



def serve_chai():
    yield "01 ) Alok "
    yield "02) Krishna "
    yield "-3) radha"
    
    
stall = serve_chai()
print(stall)  # gives generator 

for cup in stall :
    print(cup)  
    
# yield pause the value , it does not return value as return gives 

print(next(stall))    