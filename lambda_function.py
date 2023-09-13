'''
Lambda function :- Lambda functoin i a special type of function which does not have any name or anonymous

Lambda functon does not have any identity

syntax :-
    varname = lambda expression: operation



'''

#normal function

def sum(n1,n2):
    ans = n1+n2
    print(ans)
sum(40,60)

# using Lambda function
ans = lambda n1,n2: n1+n2
print(ans(40,60))

ans = lambda n1,n2,n3: n1*n2*n3
n1 = int(input("Enter first Number : "))
n2 = int(input("Enter Second Number : "))
n3 = int(input("Enter Third Number : "))
print(ans(n1,n2,n3))