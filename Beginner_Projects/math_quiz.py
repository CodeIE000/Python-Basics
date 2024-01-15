# MATH QUIZ

# Todolist
# 1. Fix input validation in each quizzes and find alt for exceptions.

import sys
import time

delay = 5

OPERATIONS = {
	'1': 'Addition', 
	'2': 'Subtraction', 
	'3': 'Multiplication', 
	'4': 'Division', 
	'5': 'Mixed', 
	'6': 'Quit'
}

ADDITIONS = {
	"23 + 24": 47, 
	"15 + 37": 52, 
	"34 + 12": 46
}

SUBTRACTIONS = {
	"16 - 23": -7,
	"45 - 34": 11,
	"23 - 21": 2
}

MULTIPLICATIONS = {
	"12 x 2": 24,
	"6 x 7": 42,
	"8 x 9": 72
}

DIVISIONS = {
	"12 ÷ 3": 4,
	"36 ÷ 6": 6,
	"81 ÷ 9": 9
}

MIXED = {
	"3 + 13": 16,
	"4 - 23": -19,
	"4 x 9": 36,
	"45 ÷ 5": 9
}

# Introduction Display
def intro_display():
    print("MATH QUIZ")

    print("Choose an operator:")

    for index, operation in OPERATIONS.items():
        print(f"{index}. {operation}")
	

def get_user_choice():
	while True:
		try:
			user_choice = int(input("=> "))
			if 1 <= user_choice <= 6:
				return user_choice
			else:
				print("Choose only 1-5")
		except ValueError:
			print("Invalid Input!")
			return get_user_choice()


def addition_quiz():
	item = 1
	score = 0
	for question, answer in ADDITIONS.items():
		while True:
			print(f"Question #{item}")
			try:
				user_answer = int(input(f"{question} = "))
				if user_answer == answer:
					print("Correct!")
					score += 1
					item += 1
					break
				else:
					print("Incorrect!")
					item += 1
					break
			except ValueError:
				print("Invalid Input!")
			
	print(f"Finished! Your score is {score}/{item - 1}.")
	time.sleep(delay)
	return main_section()
	
	
def subtractionQuiz():
	item = 1
	score = 0
	for question, answer in SUBTRACTIONS.items():
		while True:
			print(f"Question #{item}")
			try:
				user_answer = int(input(f"{question} = "))
				if user_answer == answer:
					print("Correct!")
					score += 1
					item += 1
					break
				else:
					print("Incorrect!")
					item += 1
					break
			except ValueError:
				print("Invalid Input!")
			
	print(f"Finished! Your score is {score}/{item - 1}.")
	time.sleep(delay)
	return main_section()
	

def multiplication_quiz():
	item = 1
	score = 0
	for question, answer in MULTIPLICATIONS.items():
		while True:
			print(f"Question #{item}")
			try:
				user_answer = int(input(f"{question} = "))
				if user_answer == answer:
					print("Correct!")
					score += 1
					item += 1
					break
				else:
					print("Incorrect!")
					item += 1
					break
			except ValueError:
				print("Invalid Input!")
			
	print(f"Finished! Your score is {score}/{item - 1}.")
	time.sleep(delay)
	return main_section()
	
	
def division_quiz():
	item = 1
	score = 0
	for question, answer in DIVISIONS.items():
		while True:
			print(f"Question #{item}")
			try:
				user_answer = int(input(f"{question} = "))
				if user_answer == answer:
					print("Correct!")
					score += 1
					item += 1
					break
				else:
					print("Incorrect!")
					item += 1
					break
			except ValueError:
				print("Invalid Input!")
			
	print(f"Finished! Your score is {score}/{item - 1}.")
	time.sleep(delay)
	return main_section()
	

def mixed_quiz():
	item = 1
	score = 0
	for question, answer in MIXED.items():
		while True:
			print(f"Question #{item}")
			try:
				user_answer = int(input(f"{question} = "))
				if user_answer == answer:
					print("Correct!")
					score += 1
					item += 1
					break
				else:
					print("Incorrect!")
					item += 1
					break
			except ValueError:
				print("Invalid Input!")
			
	print(f"Finished! Your score is {score}/{item - 1}.")
	time.sleep(delay)
	return main_section()
	

def main_section():
	intro_display()
	user_choice = get_user_choice()
	if user_choice == 1:
		addition_quiz()
	elif user_choice == 2:
		subtractionQuiz()
	elif user_choice == 3:
		multiplication_quiz()
	elif user_choice == 4:
		division_quiz()
	elif user_choice == 5:
		mixed_quiz()
	elif user_choice == 6:
		print("Thank you!")
		sys.exit


main_section()