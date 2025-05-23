"""Ask user personality traits → decide house"""

print("Answer yes or no to these personality questions:")

houses = []

brave = input("Are you brave? ").lower()
if brave == "yes":
    houses.append("Gryffindor")

ambitious = input("Are you ambitious? ").lower()
if ambitious == "yes":
    houses.append("Slytherin")

intelligent = input("Are you intelligent? ").lower()
if intelligent == "yes":
    houses.append("Ravenclaw")

loyal = input("Are you loyal? ").lower()
if loyal == "yes":
    houses.append("Hufflepuff")


if not houses:
    print("You did not match any house.")
else:
    print("\nYou belong to:")
    for house in houses:
        print(f"- {house}")
