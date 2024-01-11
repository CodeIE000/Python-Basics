# FUNCTIONS

# Demonstration Samples:
# Without parameters:
def function():
    print("Run")
    def func():
        print('hi')
    func()

function() # Function call

# With parameters:
def function(x, y):
    print("Run", x, y)
    def func(z):
        print('hi', z + 2)
    func(5)

function(5, 6) # Function call with parameters

# With multiple returns:
def function(x, y):
    print("Run", x, y)
    return x ** y, x * y, x / y # Can return multiple values and will return in a form of tuple.
    def func(z):
        print('hi', z + 2)
    func(5)

print(function(5, 6)) # Function call with parameters

# With assigning multiple variable:
def function(x, y):
    print("Run", x, y)
    return x ** y, x * y, x / y # Can return multiple values and will return in a form of tuple.
    def func(z):
        print('hi', z + 2)
    func(5)

r1, r2, r3 = function(5, 6) # Function call set in a respective variables

print(r1, r2, r3)

# With z as optional parameter:
def function(x, y, z=None): # You can either assign value to the parameter or not.
    print("Run", x, y)
    return x ** y, x * y, x / y # Can return multiple values and will return in a form of tuple.
    def func(z):
        print('hi', z + 2)
    func(5)

r1, r2, r3 = function(5, 6) # Function call set in a respective variables

print(r1, r2, r3)

# Advanced example:
def function(x):
    def func2():
        print(x)
    return func2

function(3)()
x = function(3)
x()