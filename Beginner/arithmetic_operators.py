#Arithmetic Operators
x = 10
y = 5
sum = x + y
difference = x - y
product = x * y
quotient = x / y
power = x ** y
remainder = x % y
print("x =", x, "y =", y)
print("Sum:", sum, "Difference:", difference, "Product:", product, "Quotient:", quotient, "Power", power, "Remainder: ", remainder)

#Note Points
#Float dominates interger type
#Division operator always returns float value, Convert to interger if you dont want float, or use //
quotient = int(x/y)
print(quotient)
quotient = x // y
print(quotient)

#Order of Operators