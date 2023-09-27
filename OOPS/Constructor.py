'''
Constructor :- Constructor is a special method which will call itself automatically when an object is created.

--> it will call utomatically when we create the object

---> the main purpose of constructor is to assign values to the methods and attributes.

--> Inpython the name of constructor will always be __init__

There are two types of constructor:
1. Default Constructor :- which does not have parameters
2. Parameterized Constructor :- which have parameters
'''

class Demo:
    a=10
    def __init__(self):  # default Constructor
        print("Welcome to the constructor")
        
    def show(self):
        print(self.a*self.a)
    
#object creation
obj = Demo()
obj.show()


class Student:
    def __init__(self,id,name):
        print("Student Id : ",id)
        print("Student name : ",name)

st = Student(1,"Brijesh")


 # Method Override       
class Demos:
    def __init__(self):
        print("First Constructor")
    def __init__(self):
        print("Second Constructor")

d = Demos()