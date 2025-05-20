"""Create mad_libs.py – Ask for 5 inputs and generate a story using string interpolation"""

name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")


story = f"""
Once upon a time, there was a person named {name}.
One day, {name} went to {place} and saw a {adjective} {noun}.
Suddenly, the {noun} started to {verb} wildly!
It was the most exciting day of {name}'s life.
"""


print(story)