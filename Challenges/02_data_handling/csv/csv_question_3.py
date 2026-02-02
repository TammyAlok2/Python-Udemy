# Write a program to create a csv file to store student data (Roll no,Name, marks ) . obtain data
# from user and write 5 records into the file 

import csv 

# open the file in the write mode 

fh = open("Student.csv","w")

# Making a writer object 
stuwriter = csv.writer(fh)

# putting the values in csv file using writerrow
stuwriter.writerow(["Roll no ","Name ","marks"])


# now taking 5 user values 

for i in range(5):
    print("Student record ",i+1)
    roll_no = input("Enter roll no")
    name = input("name")
    marks = input("marks")
    student_record = [roll_no,name,marks]
    stuwriter.writerow(student_record)
    
fh.close()    
