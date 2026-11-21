
# ==================================
#       PYTHON QUIZ APPLICATION
# ==================================

import random

# Store quiz questions
questions = [
    {
        "question": "1. Which language is used for AI?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "2. What is the output of 5 + 5?",
        "options": ["A. 10", "B. 15", "C. 20", "D. 25"],
        "answer": "A"
    },
    {
        "question": "3. Which keyword defines a function?",
        "options": ["A. function", "B. fun", "C. def", "D. define"],
        "answer": "C"
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. float", "D. bool"],
        "answer": "D"
    },
    {
        "question": "5. Which symbol is used for comments?",
        "options": ["A. //", "B. #", "C. /*", "D. @"],
        "answer": "B"
    },
    {
        "question": "6. Which function displays output in Python?",
        "options": ["A. input()", "B. print()", "C. show()", "D. display()"],
        "answer": "B"
    },
    {
        "question": "7. Which loop is used to iterate over a list?",
        "options": ["A. if", "B. else", "C. for", "D. break"],
        "answer": "C"
    },
    {
        "question": "8. Which operator is used for multiplication?",
        "options": ["A. +", "B. -", "C. *", "D. /"],
        "answer": "C"
    },
    {
        "question": "9. Which function gets user input?",
        "options": ["A. input()", "B. print()", "C. type()", "D. len()"],
        "answer": "A"
    },
    {
        "question": "10. Which data structure stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    }
]


# Quiz function
def start_quiz():

    score = 0
    total = len(questions)

    print("\n===================================")
    print("       WELCOME TO PYTHON QUIZ")
    print("===================================")

    username = input("Enter your name: ")

    print("\nHello", username, "!")
    print("Answer the following questions.")
    print("Each correct answer gives 1 mark.")
    print("There is no negative marking.")

    # Randomize question order
    random.shuffle(questions)

    # Display questions
    for q in questions:

        print("\n-----------------------------------")
        print(q["question"])

        for option in q["options"]:
            print(option)

        # Get valid user input
        while True:
            user_answer = input(
                "Enter your answer (A/B/C/D): "
            ).strip().upper()

            if user_answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input! Enter A, B, C or D.")

        # Check answer
        if user_answer == q["answer"]:
            print("Correct Answer!")
            score += 1

        else:
            print("Wrong Answer!")
            print("Correct answer:", q["answer"])

    # Calculate result
    percentage = (score / total) * 100

    # Display final result
    print("\n===================================")
    print("             QUIZ RESULT")
    print("===================================")

    print("Student Name:", username)
    print("Total Questions:", total)
    print("Correct Answers:", score)
    print("Wrong Answers:", total - score)
    print("Final Score:", score, "/", total)
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 80:
        print("Grade: Excellent!")
    elif percentage >= 60:
        print("Grade: Good!")
    elif percentage >= 40:
        print("Grade: Average!")
    else:
        print("Grade: Needs Improvement!")

    print("===================================")


# Main program
while True:

    print("\n1. Start Quiz")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        start_quiz()

    elif choice == "2":
        print("Thank you for playing!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1 or 2.")
