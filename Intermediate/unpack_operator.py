#UNPACK OPERATOR    

"""
In Python, unpack operators are like magic hands that take a collection of 
items bundled together and "spread" them out into individual variables or 
elements within a list, tuple, or string. They simplify your code and improve readability.

There are two main unpack operators:

1. Star operator (*):
Used for sequences (lists, tuples, strings).
Unpacks the sequence element by element into separate variables or list elements.

2. Double-star operator ():**

Used for dictionaries.
Unpacks the key-value pairs of the dictionary into separate variables or keyword arguments.
"""

#Demonstration Samples:
#Unpack operator with list:
def function(*args, **kwargs):
    pass

x = [1,2,23,345,6,7]
print(x)
print(*x)

#With list of tuples:
def func(x, y):
    print(x, y)

pairs = [(1,2), (3,4)]
for pair in pairs:
    func(*pair)

#With dictionaries:
def func(x, y):
    print(x, y)

dictionary = [(1,2), (3,4)]
for dict in dictionary:
    func(**{'x': 2, 'y': 5})

#Note: Double asterisks is used for dictionaries, and single asterisks is used for the rest.
    
