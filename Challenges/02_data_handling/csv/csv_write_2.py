# You need to create a csv file where , you take input from user (name ,phone no , class , marks) you have to take user input how many students are there and make a csv file for it and make function to read the csv file as well 


import csv 

# open csv file in write mode 
fh = open("Class10Students.csv","w",newline="")

# make a writer object 
w = csv.writer(fh)

# now take user input no of students 
no_of_students = int(input("Enter the no of students"))

for student in range(1,no_of_students):
    print("Student no. ",student)
    name = input("Enter name ")
    phone_no = input("Enter phone number")
    student_class = input("Enter your class")
    
    student_data = [name,phone_no,student_class]
    w.writerow(student_data)


fh.close()    