import random

computer = random.randint(1,20)
status = True
while status:
    user = int(input("Enter your Number : "))
    if user > computer:
        print("Choose Lower Number")
    elif user < computer:
        print("choose Higher Number")
    else:
        print("You Win the game")
        status = False