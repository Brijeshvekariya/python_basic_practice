'''
Exception : 



Try block runs when there is no error.
if try block catches the error, then except block is executed


snytax :

try:
    statement which can generate exception

except:
    solution of generated exception


'''

try:
    n = int(input("Enter an integer: "))
    a = [1,2,3]
    print(a[n])
except ValueError:
    print("Number is not an integer")
except IndexError:
    print("Index Error")


try:    
    a = int(input("Enter any number : "))
    b = int(input("Enter divisor : "))

    ans = a/b
    print(ans)
# except:
#     print("Cannot divide by zero")

except ZeroDivisionError:
    print("Invalid input- Cannot divide by zero")
except ValueError:
    print("Invalid Input- only 0-9 allowed")



try :
    a=45
    b=56
    print("sum: ",a+B)
except:
    print("Error")

x=67
y=3
print("Multiplication : ",x*y)
