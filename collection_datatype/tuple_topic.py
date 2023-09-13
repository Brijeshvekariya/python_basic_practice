
"""
    tuple : tuple is a collection datatype
    which contain similar and dis-similar data elements in single entity

    tuple which is represent by () braces

    main difference between tupleand list is tuple are immutable 

    we can't perform any operations like append, delete, remove..

    if tuple created of one element, then you have to add , at last. if not comma then python interpreter consider it as a integer.
    t = (1)   ----> it is intereger 
    t = (1,) ---> it is tuple.

"""
t = (1,2,3,4)
print(t)

print(len(t))
count = 0
for i in t:  #we can display all elements in tuple by etration
    print(i)
    count +=1
print(count)