class BaseChai:
    def __init__(self,type_):
        pass
    
    def prepare (self):
        print(f"Preparing {self.type} chai....")
    
    
class MasalaChai(BaseChai): # We are inheriting from upper class 
    def add_species(self):
        print("Adding cardmon , ginger , cloves.")
        


class ChaiShop:
    chai_cls = BaseChai
    
    def __init__(self):
        self.chai = self.chai_cls("Regular")
    
    
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")    
                