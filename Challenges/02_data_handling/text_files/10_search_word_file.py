f = open("intro.txt","r")

data = f.read()

if "Python" in data:
    print("Word found")

else :
    print("Word not found")

f.close()    