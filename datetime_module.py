import datetime

print(datetime.datetime.now().strftime("%H : %M : %S"))
print(datetime.datetime.now())
print(datetime.date.today())
data = datetime.datetime.now()
formated = data.strftime('%d_%m_%y')
print(formated)