"""Ask the user 3 questions and give them a score at the end."""


questions = {
    "What is the capital of France? ": "Paris",
    "What is 2 + 2? ": "4",
    "What color is the sky? ": "blue"
}

score = 0

for question in questions:
    answer = input(question)
    if answer.lower() == questions[question].lower():
        print("Correct")
        score += 1
    else:
        print("Wrong answer")
        
print(f"\n Your final score is: {score}/{len(questions)}")