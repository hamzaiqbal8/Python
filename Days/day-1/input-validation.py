""" Add input validation: disallow blank names or negative numbers """

name = input("Enter your name: ").strip()

if name == "":
    print("Name cannot be blank.")
else:
    print("Welcome,", name)


# def get_user_name():
#     """Gets the user's name from input."""
#     name = input("Please enter your name: ")
#     return name

# def greet_user(name):
#     """Greets the user by name."""
#     print(f"Hello, {name}! Welcome!")

# # Example usage
# user_name = get_user_name()
# greet_user(user_name)
