# write a program to read and display the contents of Emplooyee.csv created in the previous program

import csv

with open("Emplooyee.csv", "r") as fh:
    reader = csv.reader(fh)
    print("file Emplooyee.csv contains:")
    for read in reader:
        print(read)
