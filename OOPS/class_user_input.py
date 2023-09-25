class Student:

    def inputdata(self):
        self.stid=int(input("Enter Student ID : "))
        self.stnm = input("Enter Name : ")
    
    def displaydata(self):
        print("Student id : ",self.stid)
        print("Student Name : ",self.stnm)

# object creation

st = Student()
st.inputdata()
st.displaydata()