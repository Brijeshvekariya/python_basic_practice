import phonenumbers
from phonenumbers import geocoder
num = phonenumbers.parse("+918758169982")
print("\nPhone number :\n")
print(geocoder.description_for_number(num,"en"))