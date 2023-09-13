ans = lambda n1,n2 : n1-n2 if n1>n2 else n2-n1

n1 = int(input("Enter first Number : "))
n2 = int(input("Enter Second Number : "))
print(ans(n1,n2))



print((lambda n1,n2 : n1-n2 if n1>n2 else n2-n1)(10,5))
