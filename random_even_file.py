import random

for i in range(20):
    a = random.randrange(0,999,5)
    if a%2 == 0:
        with open("even.txt","a") as f:
            f.write(str(a)+"\n")

    else:
        f = open("odd.txt","a")
        f.write(str(a)+"\n")
f.close()    