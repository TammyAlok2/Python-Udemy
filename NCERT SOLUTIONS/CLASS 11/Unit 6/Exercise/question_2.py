#  Write a function to print the table of a given number. 
# The number has to be entered by the user

def table_using_for_loop(number):
    for index in range(1,11):
        print(f"{number} * {index} =", number*index)
        
def table_using_while_loop(number):
    index = 1 
    while(index<=10):
        print(f"{number} * {index} = ",number* index)
        index+=1        

number = int(input("Enter number to print multipiclication table"))
table_using_for_loop(number)  
table_using_while_loop(number)      