chai = "ginger chai"

def prepare_chai(order):
    print("Preparing ",order)


# prepare_chai(chai)
# print(chai)

# string are not immutable while list are mutable


chai = [1,2,3,4,5]
def edit_chai(cup):
    cup[1] = 42


edit_chai(chai)
print(chai)    

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

    
make_chai("darjeeling",'yes','Low') # positional 
 
make_chai(tea="Green",sugar="high",milk="no") # Keywords    


# (args, *kwargs) this is called handling multiple arguments 
def special_chai(*ingredients,**extras):
    print("Ingridients",ingredients) # This gives tuple
    print("Extras",extras) # This give dictionary 
    
special_chai("Cinnamon","Cardomom",sweetner = "Honey",foam="yes")    


# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order =None):
    if order is None:
        order= []
        order.append("masala")
        print(order)
        
        
        
    
chai_order() 
chai_order()
chai_order()       