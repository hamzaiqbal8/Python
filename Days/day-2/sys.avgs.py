"""Try sys.argv to pass name and age via CLI arguments (hint: import sys)"""

import sys


if len(sys.argv) < 3:
    print("Usage: python cli_info.py <name> <age>")
    sys.exit()


name = sys.argv[1]
age = sys.argv[2]

print(f"Hello, {name}! You are {age} years old.")

