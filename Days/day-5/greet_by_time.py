"""Input hour → return morning, afternoon, evening greeting"""

hour = float(input("Enter the time: "));

if 5 <= hour <= 12:
    print("Good Morning")
elif 12 < hour <= 18:
    print("Good Afternoon")
else:
    print("Good Evening")