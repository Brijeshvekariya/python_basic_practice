'''
finally code block always excute

syntax :

try:
    statment
except:
    solution
finally:
    code which is going to executed at any situation



'''

def myfun(n):
    try:
        l = [1,2,3,4]
        print(l[n])
        return 1 
    except:
        print("Index Error")
        return 0
    
    # print("Thank you")    ----> This will not executed
    finally:
        print("Thank you")

n = int(input("Enter Index : "))
print(myfun(n))