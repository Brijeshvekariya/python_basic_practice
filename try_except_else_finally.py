'''
try :
    exception bloxk

except:
    after exception execution block

else:
    without exception 

finally:
    it will always executed



'''

try:
    a=10
    b=5  # if b = int and on error occur then else part will also executed

    ans = a+b
    print(ans)

except:
    print("Invalid input")

else:
    print("Welcome to our application")

finally:
    print("Thank you for using our application")