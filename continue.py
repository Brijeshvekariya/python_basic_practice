
print("------------------------------This is a Number Guessing Game-----------------------------\n\n")
status = True
count = 0
while status:   
    num = int(input("Guess Any number from 0 to 100 : "))
    if num ==0 or num >=80 or num == 50:
        print(" You loss ")
        count +=1
        continue
    else:
        print(num)
    if count ==0:
        print("You Won The GAME")        
    choice = int(input("Do you Want to Continue ? press 1 for Yes and 2 for No "))
    if choice == 1:
        status=True
    else:
        status=False