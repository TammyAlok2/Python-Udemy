class Chai:
    def __init__(self,sweetness,milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
        
    def sip(self):
        print("Sipping Chai")
        
    def pour(self):
        print("Pouring chai")    
        
        
my_chai =Chai(sweetness=3,milk_level=10)        
my_chai.pour()
my_chai.sip() 