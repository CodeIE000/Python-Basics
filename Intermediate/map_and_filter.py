# MAP AND FILTER

# Definition:
# 2 useful function in python which can makes use of lambda function.

# Demonstration Samples:

# Map:
x = [1,2,4,5,6,3,312,3,1,2,3,1,452,76]
# Map takes all the element of the list and use a function to map them to a new list.
mp = map(lambda y: y + 2, x)
# This maps all the elements in x to the lambda function and adds 2 to each of them.
# Then puts the result into a new list.
print(list(mp))

# Filter:
x = [1,2,4,5,6,3,312,3,1,2,3,1,452,76]
# Filter returns and make use of a true or false statement.
mp = filter(lambda y: y % 2 == 0, x)
# Then puts the result into a new list, if the conditions of each updated element is satisfied.
print(list(mp))

# Alternative way instead of using lambda but a bit complicated:
def func(i):
    return i % 2 == 0
mp = filter(func, x)
print(list(mp))
# This emphasizes  that we may just utilize the lambda right away inside the map or filter statement
# rather than defining your own function in some cases.
