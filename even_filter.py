dataset = [12,67,23,44,10,22,54,78,2,8]

def myfun(seq):
    if seq%2==0:
        return True
    else:
        return False

filtered_data = filter(myfun,dataset)

for i in filtered_data:
    print(i)