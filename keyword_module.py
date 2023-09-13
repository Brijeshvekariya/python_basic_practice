import keyword

keyword_list = keyword.kwlist
# print(keyword_list)
n = input("Enter word : ")
if n in keyword_list:
    print("It is keyword")
else:
    print("It is not keyword")