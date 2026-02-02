import csv 

f = open("student.csv","w",newline="")

w= csv.writer(f) # Writer creates a writer object 

w.writerow(["Roll no","Name","Marks"]) # Writes one row at a time 

w.writerow([1,"Aman",80]) 

w.writerow([2,"Neha",90])

f.close()

