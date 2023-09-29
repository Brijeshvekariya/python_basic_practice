'''
Encapsulation :- Encapsulation is a process to wrap the data in a single entity.
which provide security to data.
two types:
setter : is used to set the data 
getter : is used to get the data

private mode : It is only accessible within the class : "__"before datamember_name or methid_name

'''

class Product:

    def __init__(self):
        self.__mobile = 20000
        self.laptop = 80000

    def display(self):
        print("Mobile : ",self.__mobile)
        print("Laptop : ",self.laptop)

    def changedata(self,newprice):
        self.__mobile = newprice

m1 = Product()
m1.display()

print("*"*50)
m1.__mobile = 40000
m1.laptop = 90000
m1.display()

print("*"*50)
print("Change data using method")

m1.changedata(40000)
m1.display()
