# *args, **kwargs

"""
*args (star-args):

Gathers an unlimited number of positional arguments into a tuple.
Useful when you don't know exactly how many arguments a function might receive.
"""
# Example:
def sum_all(*args):
    total = 0
    for number in args:
        total += number
    return total

result = sum_all(1, 2, 3, 4, 5)  # Works with any number of arguments

"""
 **kwargs (double-star-kwargs):

Gathers an unlimited number of keyword arguments into a dictionary.
Useful for handling arbitrary keyword arguments with their associated values.
"""
# Example:
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")  # Accepts any keyword arguments


# Demonstration Samples:

def function(*args, **kwargs):
    print(args, kwargs)

function(1,2,3,4,5, one=0, two=1)

# Note: You can assign unlimited amount of value within *args and **kwargs.
     