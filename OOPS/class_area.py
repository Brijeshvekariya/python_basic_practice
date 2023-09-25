class Area:
    def rectangle(self):
        l = int(input("Enter Length of Rectangle : "))
        b = int(input("Enter Breadth of Rectangle : "))
        return l*b

    def square(self):
        l = int(input("Enter Length of Square : "))
        return l*l

    def triangle(self):
        l = int(input("Enter Base of Triangle : "))
        h = int(input("Enter Height of Triangle : "))
        return (l*h)//2 
    
shape = Area()

status = True
while status:
    menu = '''
                press 1 for Rectangle 

                press 2 for Square

                press 3 for Triangle 

                press other any key to exit


'''
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        print("Area of Rectangle is : ",shape.rectangle())
    elif choice == 2:
        print("Area of Rectangle is : ",shape.square())
    elif choice == 3:
        print("Area of Rectangle is : ",shape.triangle())
    else:
        status=False