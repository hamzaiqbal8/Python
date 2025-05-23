"""Sort into house based on 2–3 character inputs"""

short_input = input("Enter your 2,3 charater code: ").lower()

if short_input == "gr" or short_input == "gly":
    house = "Gryffindor"
elif short_input == "sl" or short_input == "sly":
    house = "Slytherin"
elif short_input == 'ra' or short_input == 'rav':
    house = "Ravenclaw"
elif short_input == 'hu' or short_input == 'huf':
    house = "Hufflepuff"
else:
    house = "Unkown house"
    
print(f"You belong to: {house}")