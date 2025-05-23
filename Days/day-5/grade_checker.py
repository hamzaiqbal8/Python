"""grade_checker.pyInput score → print A/B/C/D/F using if-elif"""

print("Welcome to the Simple Exam Grader!")

score = int(input("Enter the score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'


print("Score:", score)
print("Your Grade is:", grade)
