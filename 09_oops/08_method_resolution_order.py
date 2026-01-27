# Method Resolution Order (MRO)

class A :
    label = "A : Base Class "

class B(A): 
    label = "B : Masala Blend"

class C(A):
    label = "C : Herbal blend "    
    
class D(B,C): # Output decide from here now B label will be printed 
    pass 

cup = D()
print(cup.label)  # B : Masala Blend
print(D.__mro__)
 