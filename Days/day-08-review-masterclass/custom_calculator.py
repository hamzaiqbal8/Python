"""Create a function using *args to calculate total and average of many numbers."""

def calc(*args):
    total = 0
    count = 0
    for num in args:
        total += float(num)
        count += 1
    average = round(total / count, 2)
    print("Sum:", total)
    print("Count:", count)
    print("Average:", average)


user_input = input("Enter numbers (comma-separated): ")


if user_input.strip() == "":
    print("No input provided.")
else:
    numbers = [n.strip() for n in user_input.split(",")]

    try:
        calc(*numbers)
    except ValueError:
        print("Invalid input. Please enter only numbers.")
