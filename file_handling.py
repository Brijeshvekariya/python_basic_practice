'''
File- handlling :- We can create, read, and write file using Python

There are 4 modes of file in Python:-

r - read mode
w - write mode
x - create mode
a - append mode

'''

# f = open("tops.txt","x")
# f = open("tops.txt","r")

# print(f.read())
# name = input("Enter your name : ")
# f.write(name)
# f.close()

f = open("tops.txt","a")
name = input("Enter your name : ")
f.write(name)
f.close()