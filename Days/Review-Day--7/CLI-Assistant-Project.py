"""CLI Assistant Project"""

import datetime
import webbrowser



print("Welcome to Smart CLI Assistant")
print("Type 'help' to see what I can do.\n")

while True:
    command = input(">>> ").lower()

    if command == "help":
        print("""
        I can do the following:
        - say hello
        - tell time
        - tell date
        - do math (add, subtract, multiply, divide)
        - search google
        - open youtube
        - exit
        """)
    
    elif "hello" in command:
        print("Hello Hamza! I'm your CLI Assistant")
    elif "time" in command:
        now = datetime.datetime.now()
        print("Current Time:", now.strftime("%H:%M:%S"))
    elif "day" in command:
        today = datetime.datetime.today()
        print("Today's Date:", today.strftime("%Y-%m-%d"))
    elif "add" in command:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)
    elif "substract" in command:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)
    elif "multiply" in command:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)
    elif "multiply" in command:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero!")
    elif "google" in command:
        search = input("What do you want to search on Google? (Type and press ENTER key.)\n")
        webbrowser.open(f"https://www.google.com/search?q={search}")

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command:
        print("Goodbye, Hamza! See you soon.")
        break

    else:
        print("Sorry, I didn’t understand that. Type 'help' to see commands.")



