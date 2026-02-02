# Show the data of student.csv without EOL Supression 

# using simple method 

# import csv 

# # open file in the read mode 

# fh = open("Student.csv","r",newline="")

# student_data = csv.reader(fh)

# for data in student_data:
#     print(data)
    
# fh.close()    


import csv 

with open("Student.csv","r",newline="\r\n") as fh:
    reader = csv.reader(fh)
    for read in reader:
        print(read)
        
        