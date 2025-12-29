#  Presume that a ladder is put upright against 
# a wall. Let variables length and angle store   
# the length of the ladder and the angle that 
# it forms with the ground as it leans against  
# the wall. Write a Python program to compute 
# Reprint 2025-26
# GettinG Started with Python
# 119
# the height reached by the ladder on the   
# wall for the following values of length and angle:
# a) 16 feet and 75 degrees 
# b) 20 feet and 0 degrees 
# c) 24 feet and 45 degrees
# d) 24 feet and 80 degrees


import math

# Function to calculate height reached by ladder
def ladder_height(length, angle_degree):
    angle_radian = math.radians(angle_degree)   # convert degrees to radians
    height = length * math.sin(angle_radian)
    return height

# Given cases
cases = [
    (16, 75),
    (20, 0),
    (24, 45),
    (24, 80)
]

# Compute and print results
for length, angle in cases:
    height = ladder_height(length, angle)
    print(f"Ladder length = {length} ft, Angle = {angle}° → Height = {height:.2f} ft")
