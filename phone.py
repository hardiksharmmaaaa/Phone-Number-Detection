import phonenumbers
number=(input("Enter the number"))
from phonenumbers import geocoder

#geocoder is a built in function from phonenumbers
cName=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(cName,"en")) 

#for printing the service provider information
from phonenumbers import carrier #carrier is used for service provider
service=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service,"en"))