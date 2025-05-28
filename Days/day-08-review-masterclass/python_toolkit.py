"""Create a CLI utility app offering tools through a menu system."""

import string

def calculator():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        op = input("Choose operation (+ - * /): ")

        if op == '+':
            print("Result:", a + b)
        elif op == '-':
            print("Result:", a - b)
        elif op == '*':
            print("Result:", a * b)
        elif op == '/':
            print("Result:", a / b)
        else:
            print("Invalid operation")
    except:
        print("Error: Please enter valid numbers")

def converter():
    print("1. cm to inch\n2. inch to cm\n3. kg to lb\n4. lb to kg")
    choice = input("Choose option: ")
    try:
        val = float(input("Enter value: "))
        if choice == '1':
            print("Result:", round(val / 2.54, 2), "inch")
        elif choice == '2':
            print("Result:", round(val * 2.54, 2), "cm")
        elif choice == '3':
            print("Result:", round(val * 2.2, 2), "lb")
        elif choice == '4':
            print("Result:", round(val / 2.2, 2), "kg")
        else:
            print("Invalid option")
    except:
        print("Error: Enter a valid number")

def check_password():
    pwd = input("Enter password: ")
    has_symbol = any(char in string.punctuation for char in pwd)
    if len(pwd) < 6:
        print("Weak password")
    elif len(pwd) >= 8 and has_symbol:
        print("Strong password")
    else:
        print("Moderate password")

def word_count():
    text = input("Type a sentence: ")
    words = text.split()
    print("Words:", len(words))
    print("Characters:", len(text))

def main():
    while True:
        print("\n--- Python Toolkit ---")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Password Check")
        print("4. Word Count")
        print("0. Exit")
        choice = input("Pick 1-4 or 0 to exit: ")

        if choice == '1':
            calculator()
        elif choice == '2':
            converter()
        elif choice == '3':
            check_password()
        elif choice == '4':
            word_count()
        elif choice == '0':
            print("Bye!")
            break
        else:
            print("Wrong choice")


if __name__ == "__main__":
    main()
