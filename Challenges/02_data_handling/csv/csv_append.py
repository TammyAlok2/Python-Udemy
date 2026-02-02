# Append some data in the emplooye table 

import csv 

# open student.csv in the append mode 

fh = open("Student.csv","a",newline="")

w = csv.writer(fh)

emp_data = [
    ["106","Muskan Soni","89"],
    ["107","Suman kumari","38"]
]

w.writerows(emp_data)

fh.close()