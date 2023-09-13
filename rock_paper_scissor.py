import random
l1 = ['Rock','Paper','Scissor']
computer = random.choice(l1)
status = True
while status:
    user = input("Enter Your Choice : ").title()
    if user == 'Rock' and computer == 'Scissor':
        print('User Wins')
    elif user == 'Scissor' and computer == 'Paper':
        print("User Wins")
    elif user == 'Paper' and computer == 'Rock':
        print("User Wins")
    elif user == 'Rock' or user == 'Paper' or user == 'Scissor':
        print("Computer Wins")
    elif user == computer:
        print("It's a Tie")
    else:
        print("exiting Game")
        status = False
    
    