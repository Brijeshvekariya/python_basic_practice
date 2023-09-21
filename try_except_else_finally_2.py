l = [34,56,78,98,32,15,20]

try:
    print(l[3])
except:
    print("List index out of range")

else:
    print(l)

finally:
    print("Thank you")