# Scopes in Python 
# Local : Inside a function 
# Enclosing from outer function if nested 
# global - top level 

def serve_chai():
    chai_type= "Masala" # local scope 
    print(f"Inside function: {chai_type}")
    
chai_type = "lemon"    
serve_chai()
print(f"Outside function: {chai_type}")



def chai_counter():
    chai_order = "lemon"
    def print_order():
        chai_order = "ginger"
        print("Inner: ",chai_order)
    print_order()    
    print("Outer :",chai_order )    
chai_order = "Tulsi"    
chai_counter()    
print("Global :",chai_order)