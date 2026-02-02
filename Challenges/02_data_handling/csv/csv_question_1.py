# Write a program to create a csv file by suppressing the EOL translation 

import csv 

# open file in the write mode 

fh = open("Emplooyee.csv","w",newline="")

empData = [
    ['Empno','Name','Destination','Salary'],
    ['1','Alok Tamrakar','TGT CS','90,000'],
    ['2','Sneha Pathak','TGT CS','90,000']
]

# make a writer 

w = csv.writer(fh)

# using writerrows function to store the data 


w.writerows(empData)

print("file created successfully ")

fh.close()