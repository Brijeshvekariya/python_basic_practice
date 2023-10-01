'''
in python we can raise custom errors byusing keyword 'raise'


'''

# salary = int(input("Enter your salary : "))
# if not 2000 < salary < 5000:
#     print("salary is not in range")
#     raise ValueError("value")

try:
    age = int(input("Enter your age : "))
    if age<18:
        raise ValueError("You cannot get darru")

except ValueError as var:
    print(var)