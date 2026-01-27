class Chai:
    temperature = "hot"
    strength = "Strong"


cutting = Chai()

print(cutting.temperature)

cutting.temperature = "mild"
print('after changing temperature',cutting.temperature   )
print('Directly look into the class',Chai.temperature)

# If we change any property in object and deleted it , then class property take place that is attribute shadowing


del cutting.temperature
print(cutting.temperature   )