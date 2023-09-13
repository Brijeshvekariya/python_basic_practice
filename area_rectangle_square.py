print("\n\nSelect any options from below : ")
print("1. Rectangle \n2. Square")
choice= int(input("Enter your Choice : "))
if choice == 1:
    l = int(input(("Enter Length : ")))
    b = int(input("Enter Breadth : "))
    print("\nArea of Rectangle is : %f"%(l*b))
elif choice == 2:
    l=int(input("Enter Length : "))
    print("\nThe Area of Square is : ",(l*l))
else :
    print("Enter valid input")