questions = ("What is the correct file extension for Python files?: ",
             "Which data type is used to store multiple items in a single variable?: ",
             "Which keyword is used to define a function in Python?: ",
             "Which loop is used to iterate over a sequence (like a list or string)?: ",
             "Which keyword is used for decision making in Python?: ")

options = (("A. .py", "B. .python", "C. .pt", "D. .pyth"),
           ("A. list", "B. tuple", "C. set", "D. dict"),
           ("A. def", "B. function", "C. define", "D. func"),
           ("A. for", "B. while", "C. loop", "D. iterate"),
           ("A. if", "B. else", "C. elif", "D. switch"))

answers = ("A", "A", "A", "A", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print("The correct answer is: " + answers[question_num])

    question_num += 1

print("----Results----")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print("Your score is: " + str(score) + "%")