"""Check the strength of a password based on length and presence of symbols."""

import string  

password = input("Enter your password: ")

has_symbol = any(char in string.punctuation for char in password)


if len(password) < 6:
    print("Weak")
elif len(password) >= 8 and has_symbol:
    print("Strong")
else:
    print("Moderate")
