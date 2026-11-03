
import re

phone = input("Enter phone number: ")

if re.match(r"^03\d{9}$", phone):
    print("Valid")
else:
    print("Invalid")

email = input("Enter email: ")

if re.match(r"^[A-Za-z0-9._]+@gmail\.com$", email):
    print("Valid")
else:
    print("Invalid")

password = input("Enter password: ")

if re.match(r"^\d{8}$", password):
    print("Valid")
else:
    print("Invalid")
