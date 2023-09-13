n= int(input("Enter Numbers of Subjects : "))
sum=0
for i in range(1,n+1):
    marks = int(input("Enter %d Subject marks : "%i))
    if marks<33:
        print("\n\nYou Failed The Exam")
        break
    else :
        sum+=marks
    print("Total Marks is : ",sum)
