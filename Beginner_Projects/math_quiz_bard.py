# MATH QUIZ BARD VERSION

import random

OPERATIONS = {
    '1': 'Addition',
    '2': 'Subtraction',
    '3': 'Multiplication',
    '4': 'Division',
    '5': 'Mixed',
    '6': 'Quit'
}

QUESTIONS = {
    'addition': {
        "23 + 24": 47,
        "15 + 37": 52,
        "34 + 12": 46
    },
    'subtraction': {
        "16 - 23": -7,
        "45 - 34": 11,
        "23 - 21": 2
    },
    'multiplication': {
        "12 x 2": 24,
        "6 x 7": 42,
        "8 x 9": 72
    },
    'division': {
        "12 ÷ 3": 4,
        "36 ÷ 6": 6,
        "81 ÷ 9": 9
    },
    'mixed': {
        "3 + 13": 16,
        "4 - 23": -19,
        "4 x 9": 36,
        "45 ÷ 5": 9
    },
}


def display_menu():
    print("MATH QUIZ")
    print("Choose an operator:")
    for index, operation in OPERATIONS.items():
        print(f"{index}. {operation}")

def get_user_choice():
    while True:
        try:
            user_choice = int(input("=> "))
            if 1 <= user_choice <= len(OPERATIONS):
                return user_choice
            else:
                print("Invalid choice. Please choose 1-6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz(question_set):
    score = 0
    questions = list(question_set.items())  # Shuffle questions
    random.shuffle(questions)

    for question, answer in questions:
        while True:
            try:
                user_answer = int(input(f"{question} = "))
                if user_answer == answer:
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("Incorrect!")
                    break  # Don't loop indefinitely on incorrect answers
            except ValueError:
                print("Invalid input. Please enter a number.")

    print(f"Finished! Your score is {score}/{len(questions)}.")

def main():
    while True:
        display_menu()
        user_choice = get_user_choice()

        if user_choice == 6:
            print("Thank you!")
            break

        quiz_type = list(OPERATIONS.values())[user_choice - 1].lower()  # Map choice to question set
        run_quiz(QUESTIONS[quiz_type])

if __name__ == "__main__":
    main()
