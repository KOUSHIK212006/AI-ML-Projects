questions = [
    {
        "question": "Which language is mainly used for AI and ML?",
        "options": ["Java", "Python", "HTML", "CSS"],
        "answer": "B"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for a comment in Python?",
        "options": ["//", "#", "/*", "<!--"],
        "answer": "B"
    },
    {
        "question": "Which collection does not allow duplicate values?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "answer": "C"
    }
]


def display_question(question_data, number):
    """Display a question and its options."""
    
    print(f"\nQuestion {number}:")
    print(question_data["question"])

    for i, option in enumerate(question_data["options"]):
        print(f"{chr(65 + i)}. {option}")


def get_answer():
    """Get and validate the user's answer."""
    
    while True:
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer

        print("Invalid answer. Please enter A, B, C, or D.")


def check_answer(user_answer, correct_answer):
    """Check whether the user's answer is correct."""
    
    return user_answer == correct_answer


def calculate_score(correct, total):
    """Calculate the quiz score as a percentage."""
    
    return (correct / total) * 100


def show_result(correct, total):
    """Display the final quiz result."""
    
    score = calculate_score(correct, total)

    print("\n===== QUIZ RESULT =====")
    print("Correct Answers :", correct)
    print("Wrong Answers   :", total - correct)
    print("Score           :", f"{score:.2f}%")

    if score >= 50:
        print("Result          : PASS")
    else:
        print("Result          : FAIL")


def main():
    """Run the quiz."""
    
    print("===== PYTHON QUIZ =====")

    correct = 0

    for number, question_data in enumerate(questions, start=1):

        display_question(question_data, number)

        user_answer = get_answer()

        if check_answer(user_answer, question_data["answer"]):
            print("Correct!")
            correct += 1
        else:
            print(
                "Wrong!",
                "Correct answer:",
                question_data["answer"]
            )

    show_result(correct, len(questions))


main()
