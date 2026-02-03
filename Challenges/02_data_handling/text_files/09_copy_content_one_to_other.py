# open text file in read mode which one you want to copy content

# open copy file in write mode 

# call f1.read() function from f2.write 

# Close both files

f1 = open("intro.txt","r")
f2 = open("copy.txt","w")

f2.write(f1.read())

f1.close()
f2.close() 