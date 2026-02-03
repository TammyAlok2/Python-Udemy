# Program to write multiple lines using writelines() 


f= open("intro.txt","w")

f.write("We are going to learn by this one of the mode ")

f.writelines(["Python\n","SQL\n","EMRS\n"])

f.close()