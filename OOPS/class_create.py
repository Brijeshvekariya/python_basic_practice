class Student:
    stid = 1
    stname = "Brijesh"

    def getdata(self):
        print("This is the data of Student")

# object creation
st = Student()
print(st.stid)
print(st.stname)
st.getdata()