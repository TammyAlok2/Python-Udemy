import csv 

with open("Student.csv","r",newline="\r\n") as fh:
    reader = csv.reader(fh)
    for read in reader:
        print(read)
        