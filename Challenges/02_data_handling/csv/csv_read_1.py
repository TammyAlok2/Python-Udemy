import csv

# open the file in the read mode 
f = open("student.csv","r")


# read the file 
r = csv.reader(f)


# print the statement 
for row in r:
    print(row)
    
# close the file 
    

f.close()    