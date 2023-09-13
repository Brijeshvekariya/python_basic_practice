"""
    This concept is wedely used in python which containkey and values in pair
    it can contain unique key

    Syntax :-

        dictionary_name = {
                            "key":"values"
        }
"""
student = {
    'name' : {'brijesh' : 'Vekariya'},
    'sub' : 'Python',
    'score' : 78
}
print(student)

# for k,v in student.items():
#     print(f"{k} = {v}")
for k in student.keys():
    print(k)
for v in student.values():
    print(v)