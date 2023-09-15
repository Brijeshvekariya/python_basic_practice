from googlesearch import search

data = input("Enter your Search : ")
print(search(data))

for i in search(data):
    print(i)