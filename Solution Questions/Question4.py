import re

phone=input("Phone:")
if re.match(r"^03\d{9}$",phone):
    print("Valid")
else:
    print("invalid")

email=input("Enter email:")
if re.match(r"^[A-Za-z0-9._]+@gmail\.com$",email):
    print("Valid")
else:
    print("invalid")

password=input("Enter password:")
if re.match(r"\d{8}$"):
    print("Valid")
else:
    print("invalid")