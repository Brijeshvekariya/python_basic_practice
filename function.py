'''
Function :- Function is a block of code or peice of code that we can use again and again.

Function provide reusability because we can use same function multiple times.

so it will reduce your code.

----> There are two types of Function:-
        
        1. Library or Inbuilt Functions :- which is already included in python library
        e.g. print(), input(), len(), zip()....

        2. User defined Functions :- which is defined by User
        e.g. greeetings(), add()....

How we can create Function in python?

using def keyword

Function Declaration :- We will declare the Function
Function Calling :- We will call the function

syntax :- 

    def fun_name():   ---> Function Declaration
        block of code

    fun_name()    ---> Function calling


Categories of Function :-
---> 4 categories of Function:-
1. Function without Parameters and without return values
2. Function with Parameters and without return values
3. Function without Parameters and with return values
4. Function with Parameters and with return values

Parameters :- The Variables which we will declare during function declaration 

Agruments :- The Values which we will write during Funcion calling is called Arguments.

Return values :- it will return some values.

'''

def greetings():      #Function Declaration
    print("Good Morning")
    print("We are Python Developers")

greetings()           #Function Calling
print("-------------------------------------")
greetings()


def printline():
    print("*"*40)
printline()

def sum(n1,n2):
    print(n1+n2)
n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
sum(n1,n2)
printline()

def checkPosNeg():
    num = int(input("Enter any Number : "))
    if num>0:
        return "postive"
    elif num<0:
        return "Negative"
    else:
        return "Number is Zero"
print(checkPosNeg())
printline()

def add(n1,n2):
    return(n1+n2)
print(add(31,40))
