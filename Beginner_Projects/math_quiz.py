# MATH QUIZ

# Todolist
# 1. Fix input validation in each quizzes and find alt for exceptions.

import sys
import time

delay = 5

operations = {
	'1': 'Addition', 
	'2': 'Subtraction', 
	'3': 'Multiplication', 
	'4': 'Division', 
	'5': 'Mixed', 
	'6': 'Quit'
}

additions = {
	"23 + 24": 47, 
	"15 + 37": 52, 
	"34 + 12": 46
}

subtractions = {
	"16 - 23": -7,
	"45 - 34": 11,
	"23 - 21": 2
}

multiplications = {
	"12 x 2": 24,
	"6 x 7": 42,
	"8 x 9": 72
}

divisions = {
	"12 ÷ 3": 4,
	"36 ÷ 6": 6,
	"81 ÷ 9": 9
}

mixed = {
	"3 + 13": 16,
	"4 - 23": -19,
	"4 x 9": 36,
	"45 ÷ 5": 9
}

# Introduction Display
def introDisplay():
    print("MATH QUIZ")

    print("Choose an operator:")

    for index, operation in operations.items():
        print(f"{index}. {operation}")
	

def getUserChoice():
	while True:
		try:
			user_choice = int(input("=> "))
			if 1 <= user_choice <= 6:
				return user_choice
			else:
				print("Choose only 1-5")
		except ValueError:
			print("Invalid Input!")
			return getUserChoice()


def additionQuiz():
	item = 1
	score = 0
	for question, answer in additions.items():
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
	return mainSection()
	
	
def subtractionQuiz():
	item = 1
	score = 0
	for question, answer in subtractions.items():
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
	return mainSection()
	

def multiplicationQuiz():
	item = 1
	score = 0
	for question, answer in multiplications.items():
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
	return mainSection()
	
	
def divisionQuiz():
	item = 1
	score = 0
	for question, answer in divisions.items():
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
	return mainSection()
	

def mixedQuiz():
	item = 1
	score = 0
	for question, answer in mixed.items():
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
	return mainSection()
	

def mainSection():
	introDisplay()
	user_choice = getUserChoice()
	if user_choice == 1:
		additionQuiz()
	elif user_choice == 2:
		subtractionQuiz()
	elif user_choice == 3:
		multiplicationQuiz()
	elif user_choice == 4:
		divisionQuiz()
	elif user_choice == 5:
		mixedQuiz()
	elif user_choice == 6:
		print("Thank you!")
		sys.exit


mainSection()