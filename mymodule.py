def sum(num1,num2):
    ans = num1+num2
    print(ans)
    
product_price = 250
if __name__ == "__main__":
    sum(12,21)
print(__name__)
'''
if we print __name__ , then we get '__main__' if we run from here and if we run from anyother place then we get '__mymodule__', 
so simply we put condition on this, error solved f running two times
'''


'''
we can create our own module and use it when we need
we have to add module_name.py file in our folder

and to use it:

import module_name
module_name.function_name or module_name.variable

'''