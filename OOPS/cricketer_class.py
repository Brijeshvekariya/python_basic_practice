class Cricket:
    def __init__(self):
        self.name = input("Enter your Name : ")
        self.age = int(input("Enter your Age : "))
        self.role = input("Enter your role : ")

class Batsmen(Cricket):
    def score(self):
        self.run = int(input("Enter Runs : "))
        self.matches = int(input("Enter Number of Matches : "))
        self.average = self.run//self.matches
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Runs : ",self.run)
        print("Total Matches : ",self.matches)
        print("Average : ",self.average)

c = Batsmen()
c.score()
 