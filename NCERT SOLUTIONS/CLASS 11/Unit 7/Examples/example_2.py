# 2) Program to calculate the payable amount for the tent using user define function 

# function definition (Area of cylindrical area )
def cyclindrical_area(height,radius):
    area= 2 * 3.14 * radius * height
    return area 


# function definition (Area of conical area)
def conical_area(length,radius):
    area = 3.14 * radius * length
    return area


cylinder_area = cyclindrical_area(10,20)
print(cylinder_area)
