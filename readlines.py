for i in range(20):
    with open("read.txt","a") as file:
        file.write(str(i)+"\n")

f = open("read.txt","r")
for line in f:
    print(line)
