"""Check if password length ≥ 8 and contains special character"""

import string
password = input("Enter your password: ")
long__enough = len(password) >= 8
special_char = string.punctuation
contain_special = any(char in special_char for char in password)

if long__enough and contain_special:
    print("Password is strong.")
else:
    print("Password must be at least 8 characters and contain a special character.")