class Student:
    db = {} # create blank dictionary
    # input method to take input
    def input(self):
        email = input("Enter your Email: ")
        password = input("Enter your Password : ")

        # storing data in db
        # here email is key and password is value

        self.db[email] = password
    
    def display(self):
        print("All Student List is : ")
        for k,v in self.db.items():
            print(f"{k} : {v}")

class Faculty:
    df = {}
    def input(self):
        email = input("Enter your Email : ")
        password = input("enter your password : ")
        self.df[email] = password
        
    def display(self):
        print("All Faculty List is : ")
        for k,v in self.df.items():
            print(f"{k} : {v}")
        
# object creation
st = Student()
ft = Faculty()
status = True
while status:
    data = '''
                press 1 for Student Registration
                press 2 for Faculty Registration
                press 3 for View all Students
                press 4 for View all Faculty
                press 5 for exit

'''
    print(data)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        st.input()
    elif choice == 2:
        ft.input()
    elif choice == 3:
        st.display()
    elif choice == 4:
        ft.display()
    else:
        status = False