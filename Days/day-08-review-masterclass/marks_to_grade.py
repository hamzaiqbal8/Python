"""Take 3 subject marks, calculate average, return letter grade (A to F)."""


marks1 = float(input("Enter first marks: "))
marks2 = float(input("Enter second marks: "))
marks3 = float(input("Enter third marks: "))

average = (marks1 + marks2 + marks3) / 3


if average >= 90:
    grade = 'A'
elif 80 <= average < 89:
    grade = 'B'
elif 70 <= average < 79:
    grade = 'C'
elif 60 <= average < 69:
    grade = 'D'
else:
    grade = 'F'


print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
