def multiplication_table(number: int) -> list[str]:
    # Write your code below this line
    result = []
    for num in range(1,11):
        ans = number * num 
        result.append(f'{number} x {num} = {ans}')
    
    return result  

answer = multiplication_table(2)
print(answer)    