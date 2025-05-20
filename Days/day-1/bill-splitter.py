# Ask for bill amount, # of people, output per-person share 


bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))
share = bill / people
print("Per Person:", share)