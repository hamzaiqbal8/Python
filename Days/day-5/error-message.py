"""Add error messages when input is out of expected range"""

age = int(input("Enter your age: "))

if 0 < age <= 120:
    print("Valid age.")
else:
    print("Error: Age must be between 1 and 120.")