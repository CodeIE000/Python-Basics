#For Loops
for i in range(1, 10):
    print(i)

"""
Note:
Range's order of argument
Stop if one arg - range(1)
Start stop if two args - range(1, 2)
Start, Stop, Step if three args - range(1, 2, 3)
Range - is a function that creates a collection of numbers
based on the input that we give it.
Default - it will start at 0 and stop at whatever number 
you place inside the parenthesis but won't include that number .
"""

#Demonstration Samples:
for x in [1,2,3,4,5,1,2]:
    print(x)

a = [1,123,13,1,5,3,]

for z in range(len(a)):
    print(a[z])

for z, index in enumerate(a):
    print(z, index)

"""
Example:
for item in sequence:
    # Code to be repeated for each item

Syntax:
for - Signals the start of the loop.
item - A temporary variable to hold each item during the loop.
in - Connects the loop to the sequence.
sequence: A collection of items to iterate over (e.g., list, string, range).
: - Marks the beginning of the code block to repeat.
# Code to be repeated for each item - The indented code that runs for each item.
"""