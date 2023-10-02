n = int(input("Enter number of terms : "))
a = 0
b = 1
c = 0
print("Fibannoci series : ",a,end=" ")
for i in range(n):
    print(b,end=" ")
    c = a+b
    a = b
    b = c