# import csv file
import csv

# open file in the write mode

f = open("student1.csv", "w", newline="")

# make a writer function

w = csv.writer(f)

# now write in the csv file using writerrow

w.writerow(["Roll no", "first_name","second_name"])

w.writerow([1,"Ananya kumari","jaiswal"])
w.writerow([2,"Pavani kumari","jaiswal"])

f.close()
