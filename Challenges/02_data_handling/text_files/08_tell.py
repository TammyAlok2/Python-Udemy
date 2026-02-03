# tell() shows pointer position 

f = open("intro.txt","r")

print("Initial Position :",f.tell())

print(f.read(7))

print("After reading: ",f.tell())

f.seek(2)
print("After seek: ",f.tell())

f.close()