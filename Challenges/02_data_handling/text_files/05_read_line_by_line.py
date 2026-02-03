f = open("intro.txt","r")

fh_single = f.readline() # reads one line 

fh_all = f.readlines() # returns list of lines 

fh_single_list = f.read() # read 


print(fh_all)

print(fh_single)

print(fh_single_list)


f.close()