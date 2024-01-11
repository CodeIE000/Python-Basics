# Exceptions

# Definition:
"""
Exceptions are like alarms that signal unexpected errors or 
problems during code execution. They interrupt the normal flow 
and demand attention to prevent crashes or unexpected outcomes.

Think of them as specialized objects with these properties:

Types: Python has built-in exception types (e.g., ValueError, 
TypeError, ZeroDivisionError) for different error categories.

Messages: Exceptions often contain informative messages describing 
the error, helping you pinpoint the issue.

Tracebacks: They provide a stack trace, a "breadcrumb trail" of 
function calls leading to the error, aiding debugging.

Key Processes:

Raising Exceptions: Use the raise keyword to intentionally signal an error:

raise ValueError("Invalid input!")


Handling Exceptions: Use try-except blocks to catch and manage errors gracefully:
try:
    # Code that might raise an exception
except ExceptionType as e:
    # Code to handle the exception

    
Benefits:
- Prevent program crashes: Catch exceptions and handle them meaningfully.
- Improve code robustness: Handle unexpected inputs or errors gracefully.
- Provide meaningful error messages: Inform users about issues and guide them.
- Enhance debugging: Tracebacks make it easier to track down the error's source.

Key Points:
- Exceptions are essential for writing robust and user-friendly Python code.
- Understanding exception types, raising, and handling them is crucial for effective error management.
- Proper exception handling ensures a more reliable and user-friendly experience.

"""

# Demonstration Samples:
# try:
#    x = 7 / 0
# except Exception as e:
#    print(e)
# finally:
#    print("finally")

# try:
#     age = int(input("How old are you?: "))
#     print("You are", age, "years old!")
# except:
#     print("Invalid Input!")
    

# raise Exception('Bad')

