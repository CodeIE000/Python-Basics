# CALCULATOR

import sys

# Dictionaries

OPERATIONS = {
    '1': 'Addition',
    '2': 'Subtraction',
    '3': 'Multiplication',
    '4': 'Division'
}

CALCULATOR_TYPE = {
    '1': "Manual Type",
    '2': "Pre-Selected Type",
    '3': 'Quit'
}

# First menu
def choice_menu():
    print("Choose a calculator type: ")
    for index, type in CALCULATOR_TYPE.items():
        print(f"{index}. {type}")
    
    while True:
        try:
            user_type_choice = int(input("=> "))
            if 0 <= user_type_choice <= len(CALCULATOR_TYPE):
                return user_type_choice
            else:
                print("Choose only 1 or 2")
                
        except ValueError:
            print("Type only the number of choice!")


# Manual calculator
def manual_calculator():
    while True:
            print("Type your expression below (e.g., 2 + 3)")
            print("Type 'Q' to quit.")
            try:
                user_input = input("=> ")
                if user_input.capitalize() == 'Q':
                    return main()
                else:
                    answer = eval(user_input)
                    print(f"= {answer}")
                
            except ValueError:
                print("Invalid Expression!")


# Pre-selected operation menu
def preselected_operation_menu():
    print("Choose an operation:")
    for index, operation in OPERATIONS.items():
        print(f"{index}. {operation}")
    
    while True:
        try: 
            user_operation_choice = int(input("=> "))
            return user_operation_choice
        except ValueError:
            print("Type only the number of choice!")


# Calculate pre-selected calculator user inputs
def calculate(user_operation_choice, first_number, second_number):
    if user_operation_choice == 1:
        sum = first_number + second_number
        return sum
    elif user_operation_choice == 2:
        difference = first_number - second_number
        return difference
    elif user_operation_choice == 3:
        product = first_number * second_number
        return product
    elif user_operation_choice == 4:
        quotient = first_number / second_number
        return quotient

# Pre-selected operation calculator
def preselected_calculator(user_operation_choice):
    while True:
        if user_operation_choice == 1:
            print("Addition:")
        elif user_operation_choice == 2:
            print("Subtraction")
        elif user_operation_choice == 3:
            print("Multiplication")
        elif user_operation_choice == 4:
            print("Division")
        try:
            first_number = int(input("First Number: "))
            second_number = int(input("second Number: "))
            answer = calculate(user_operation_choice, first_number, second_number)
            print(f"= {answer}")
            while True:
                restart = input("Again?[Y/N]: ")
                if restart.capitalize() == 'Y' or restart.capitalize() == 'N':
                    if restart.capitalize() == 'Y':
                        break
                    else:
                        return main()
                else:
                    print("Type only Y or N!")
            continue
        except ValueError:
            print("Input only a number!")
    
# Main function
def main():
    print("CALCULATOR")
    user_choice = choice_menu()
    if user_choice == 1:
        manual_calculator()
        
    elif user_choice == 2:
        user_operation_choice = preselected_operation_menu()
        preselected_calculator(user_operation_choice)
    elif user_choice == 3:
        print("Thank you!")
        sys.exit()

if __name__ == "__main__":
    main()

# To-do List
# 1. Enhance UX and convenience
        