"""Validate username/password from a predefined dictionary."""

users = {
    "admin": "123",
    "hamza": "hamza@001",
    "guest": "welcome"
}


username = input("Enter your username: ")
password = input("Enter your password: ")


if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Invalid Credentials")
