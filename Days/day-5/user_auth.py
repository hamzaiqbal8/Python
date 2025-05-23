"""Create a user_auth.py that matches user/pass from preset variables"""

correct__username = "hamzaiqbalatlaif@gmail.com"
correct__password  = "hamza@001"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct__username and password == correct__password:
    print("Login successful! Welcome,", username)
else:
    print("Login failed. Incorrect username or password.")