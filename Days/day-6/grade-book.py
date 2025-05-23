"""Create a Student Gradebook with Dictionary"""

grades = {
    "Hamza": 85,
    "Ali": 92,
    "Sara": 78,
    "Zara": 88
}

for student in grades:
    print(f"{student}: {grades[student]}")
    
total = sum(grades.values())
average = total / len(grades)
print(f"\nAverage grade: {average}")
