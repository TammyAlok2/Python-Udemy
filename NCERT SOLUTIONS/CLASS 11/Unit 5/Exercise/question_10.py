# 10.  Write a program to find the grade of a student when  
#  grades are allocated as given in the table below. 
# Percentage of Marks GRADE
# Above 90%            A 
# 80% to 90%           B
# 70% to 80%           C
# 60% to 70%           D
# Below 60 %           E 

# Percentage of the marks obtained by the student is input to the program.

percentage = int (input("Enter your percentage"))

if percentage > 90 :
    print("Grade A ")
elif percentage >= 80 & percentage <=90:
    print("Grade B")    
elif percentage >= 70 & percentage < 80:
    print("Grade C")
elif percentage >= 60 & percentage < 70:
    print("Grade D") 
else :
    print("Grade E")       
        