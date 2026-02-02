# get the import statmemnt 
import csv 

# open the csv file in the read mode 

f = open("student.csv","r")

# read the file 

r = csv.reader(f)

# print the data 

for row in r:
    print(row)
    
# close the file 
f.close()    