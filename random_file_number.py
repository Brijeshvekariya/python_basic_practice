import random
l = []
f = open("tops.txt","w")
for i in range(10):
    a = random.randint(1,1000)
    # l.append(a)
    # f.write(f"{l}")
    f.write(str(a)+"\n")
f.close