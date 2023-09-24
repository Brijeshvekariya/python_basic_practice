
e_sum = 0
o_sum = 0
status = True
while status:
    num = int(input("Enter Any Number : "))
    if num%2==0:
        e_sum+=num
    else:
        o_sum+=num
    choice = int(input("Do you want to add more Numbers ? press 1 for Yes and 2 for No "))
    if choice == 1:
        status=True
    else:
        status = False
print("The Even Sum is : ",e_sum)
print("The Odd Sum is : ",o_sum)


