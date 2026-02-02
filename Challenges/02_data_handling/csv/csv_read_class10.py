
# Using method 1 to read the file 
# import csv 

# # open file in the read mode 

# fh = open("Class10Students.csv","r")

# # use reader object 
# read = csv.reader(fh)

# for data in read:
#     print(data)

# fh.close()    

# using method 2 to read the file 
import csv 

with open("Class10Students.csv","r",newline="") as fh:
    reader = csv.reader(fh)
    for data in reader:
        print(data)
    