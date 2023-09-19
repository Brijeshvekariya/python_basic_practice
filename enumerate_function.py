# The enumerate  function # this red line is know as linter
# function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) 
# and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:


marks = [12,98,36,45,20,75,84]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("Brijesh Vekariya")
#     index+=1

for index,mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Brijesh Vekariya")



# Loop over a list and print the index and value of each element
