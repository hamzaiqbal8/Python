"""Add percentage input and output grade + remarks"""


percentage = float(input("Enter your percentage: "))
if percentage >= 90:
    grade = "A+"
    remarks = "Excellent!"
elif percentage >= 80:
    grade = "A"
    remarks = "Very Good!"
elif percentage >= 70:
    grade = "B"
    remarks = "Good!"
elif percentage >= 60:
    grade = "C"
    remarks = "Try Harder!"
else:
    grade = "F"
    remarks = "Fail!"


print("\nYour Grade:", grade)
print("Remarks:", remarks)
