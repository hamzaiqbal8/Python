"""CLI arguments version: Try passing name directly using sys.argv."""

import sys

if len(sys.argv) < 4:
    print("Please provide name, hour, and AM/PM. Example:")
    print("python sys.CLI.py Hamza 7 PM")
    sys.exit()
    
name = sys.argv[1]
hour = int(sys.argv[2])
meridian = sys.argv[3]


if meridian.upper() == "PM" and hour != 12:
    hour += 12
elif meridian.upper() == "AM" and hour == 12:
    hour = 0


if 5 <= hour < 12:
    print("Good morning,", name)
elif 12 <= hour < 18:
    print("Good afternoon,", name)
else:
    print("Good evening,", name)