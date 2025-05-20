""" Write  input name and hour, say good morning/evening accordingly. """

name = input("Enter your name: ")
hours = int(input("Enter the current hours: "))
meridian = input("Is it AM or PM? ").strip().upper()


if meridian == "PM" and hours != 12:
    hours += 12
elif meridian == "AM" and hours == 12:
    hours = 0


if 5 <= hours < 12:
    print("Good morning",name)
elif  12 <= hours < 18:
   print("Good afternoon,", name)
else:
    print("Good evening,", name)