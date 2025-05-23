"""Handle input case-insensitivity using .lower()"""

correct_username = "hamzaiqbalatlaif@gmail.com"
correct__password  = "hamza@001"


username = input("Enter your username: ").lower()
password = input("Enter your password: ").lower()


if username == correct_username.lower() and password == correct__password.lower():
    print("Login successful! Welcome,", username)
else:
    print("Login failed. Incorrect username or password.")