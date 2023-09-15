import phonenumbers
from phonenumbers import geocoder,timezone,carrier
# num = phonenumbers.parse("+918758169982")
# print("\nPhone number :\n")
# print(geocoder.description_for_number(num,"en"))

num = input("Enter your Number with Country-code : ")
phone = phonenumbers.parse(num)

time = timezone.time_zones_for_number(phone)

reg = geocoder.description_for_number(phone,'en')

car = carrier.name_for_number(phone,'en')

print(time)
print(reg)
print(car)