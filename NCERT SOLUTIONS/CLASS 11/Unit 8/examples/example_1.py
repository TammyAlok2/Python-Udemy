# Write a program with a user defined function to count the number of times a charcter (passed as argument ) occurs in the given string.

def charCount(ch,st):
    count = 0
    for charcter in st:
        if charcter == ch:
            count+=1
    return count        


st = input("Enter a string")
ch = input("Enter the charcter to be searched ")
count = charCount(ch,st)

print("Number of times charcter ",ch,"occurs in the string is ",count)