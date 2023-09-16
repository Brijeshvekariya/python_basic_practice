'''
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
