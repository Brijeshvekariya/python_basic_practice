class Employe:
    db = {}
    def __init__(self):
        a= int(input("Enter Number of Employee: "))
        for i in range(a):
            # key = int(input(f"Enter Id of {i+1} Employee : "))
            values = input(f"Enter Name of {i+1} Employee : ")
            self.db[(i+1)] = values
    def display(self):
        print("List of All Employees : ")
        for k,v in self.db.items():
            print(f"{k} - {v}")

emp = Employe()
emp.display()