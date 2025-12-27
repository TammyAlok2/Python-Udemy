#  By the end of this chapter , you will able to 
#  . Use for and While Loops effectively 
#  Loop through sequence using range() , enumerate() and zip()
 
# Control loop behaiour using break , continue and else clauses 
# Identify when to us for vs while loops 
# Build real-world logic through repetition 

# A tea stall owner has a digital token display . 
# for every customer in line , a token number is pritinted aand chai is served .set 
# Task : 
#     use a for loop to generate token numbers from 1 to 10 using range ()


for token in range (1,11):
    print(f"Serving chai to Token # {token}")
    
    
for chai in range (1,5):
    print(f"Serving chai to {chai}")    

for chai in range(5):
    print(f"Serving tea to {chai}")    

def multiplication_table(number: int) -> list[str]:
    # Write your code below this line
    result = []
    for num in range(1,11):
        ans = number * num 
        result.append(f'{number} x {num} = {ans}')
    
    return result  

answer = multiplication_table(2)
print(answer)    