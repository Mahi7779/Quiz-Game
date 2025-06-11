
def run_quiz():
    """
    Runs a simple command-line quiz game.
    """
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. O2", "B. H2O", "C. CO2", "D. NaCl"],
            "answer": "B"
        }
    ]

    score = 0
    total_questions = len(questions)

    print("Welcome to the Python Quiz Game!\n")
    print("Answer the following multiple-choice questions by typing the letter (A, B, C, or D).\n")

    for i, q_data in enumerate(questions):
        print(f"Question {i + 1}/{total_questions}: {q_data['question']}")
        for option in q_data['options']:
            print(option)

        while True:
            user_answer = input("Your answer: ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")

        if user_answer == q_data['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q_data['answer']}.\n")

    print("--- Quiz End ---")
    print(f"You scored {score} out of {total_questions} questions.")
    percentage = (score / total_questions) * 100
    print(f"That's {percentage:.2f}%!")

    if score == total_questions:
        print("Amazing! You got all the answers correct!")
    elif score >= total_questions * 0.7:
        print("Great job! You have a good knowledge base.")
    elif score >= total_questions * 0.4:
        print("Good effort! Keep learning.")
    else:
        print("You can do better! Time to brush up on your knowledge.")



if __name__ == "__main__":
    run_quiz()

