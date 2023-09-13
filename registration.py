<<<<<<< HEAD
email = input("Enter your Email : ").lower()
password = input("Enter your Password : ")
username = input("Enter your Username : ")
countrycode = input("Enter Your Country Code : ")
mobile = input("Enter your Mobile : ")

if email.endswith(".com") and email.__contains__("@"):
    if len(password) >=6 and len(password) <=16:
        if username.isalnum():
            if mobile.isdigit and len(mobile)==10:
                if countrycode.startswith("+"):
                    print("Email id : ",email)
                    print("Password is : ",end=" ")
                    for i in password:
                        print("*",end="")
                    print("\nUsername = ",username)
                    print("Mobile Number : ",countrycode + "-" + mobile)
                else:
                    print("Email id : ",email)
                    print("Password is : ",end=" ")
                    for i in password:
                        print("*",end="")
                    print("\nUsername = ",username)
                    print("Mobile Number : +"+countrycode + "-" + mobile)

            else:
                print("Enter valid mobile Number")
        else:
            print("Enter valid username") 
    else:
        print("Enter valid Password ")
        
else:
=======
email = input("Enter your Email : ").lower()
password = input("Enter your Password : ")
username = input("Enter your Username : ")
countrycode = input("Enter Your Country Code : ")
mobile = input("Enter your Mobile : ")

if email.endswith(".com") and email.__contains__("@"):
    if len(password) >=6 and len(password) <=16:
        if username.isalnum():
            if mobile.isdigit and len(mobile)==10:
                if countrycode.startswith("+"):
                    print("Email id : ",email)
                    print("Password is : ",end=" ")
                    for i in password:
                        print("*",end="")
                    print("\nUsername = ",username)
                    print("Mobile Number : ",countrycode + "-" + mobile)
                else:
                    print("Email id : ",email)
                    print("Password is : ",end=" ")
                    for i in password:
                        print("*",end="")
                    print("\nUsername = ",username)
                    print("Mobile Number : +"+countrycode + "-" + mobile)

            else:
                print("Enter valid mobile Number")
        else:
            print("Enter valid username") 
    else:
        print("Enter valid Password ")
        
else:
>>>>>>> 3b71dde1f7ecb0185ed1d65d1357b3003d5e95a2
    print("Enter valid Email ID ")