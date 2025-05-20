# Input bill and tip %, output total with tip and per person cost

bill = float(input("Enter the total bill amount: "))
tip_percent = float(input("Enter the tip percentage: "))
people = int(input("Enter the number of people: "))

tip_amount = (tip_percent / 100) * bill
total_with_tip = bill + tip_amount
per_person = total_with_tip / people



print("Tip amount:", tip_amount)
print("Total bill with tip:", total_with_tip)
print("Each person should pay:", per_person)