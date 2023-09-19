
"""
If ... Else in One Line
There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short. Here's an example:

syntax : 

value_if_true if condition else value_if_false

this also assigned value to variable as,
variable = value_if_true if condition else value_if_false


This syntax is equivalent to the following if-else statement:

if condition:
    result = value_if_true
else:
    result = value_if_false
"""

a = 330
b = 330
print(" a is less") if a < b else print(" b is less")
print(" a is less") if a < b else print("a and b is equal") if a == b else print("b is less")