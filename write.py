f = open("demofile.txt", "a")
f.write("Now the file has more content!\n")
f.close()

f = open("demofile.txt", "r")
print(f.read())
