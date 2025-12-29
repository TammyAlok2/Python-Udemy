# the formula E = mc2 states that the 
# equivalent energy (E) can be calculated as the  
# mass (m) multiplied by the speed of light (c = about 
# 3×108 m/s) squared. Write a program that accepts 
# the mass of an object and determines its energy.

m = int(input("Enter the mass of an object"))
c = 3 * (10 ** 8)


e = m * (c**2)
print("Energy will be ", e)