'''
Filter():- filter is a method which is used to filter the given sequence with help of function that test each element of sequence

syntax :- 

    filter(fun,sequence)


'''

# vowels with normal function

l1 = ['a','h','m','e','b','o','c','u']
vowel_list = ['a','e','i','o','u']
l2 =[]

def vowel_check():
    for i in l1:
        if i in vowel_list:
            l2.append(i)
vowel_check()
print(l2)



# using filter method

def myfun(seq):
    if seq in vowel_list:
        return True
    else:
        return False

filtered_data = filter(myfun,l1)

for i in filtered_data:
    print(i)