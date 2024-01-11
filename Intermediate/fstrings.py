# F-STRINGS

# New in python 3.6
# Used to manipulate and create strings.
# Can embed values into a string without the nexed to concatenate and convert.
# Just use curly braces within a single or double quotation and add value or expressions into it.
# Then it converts those values into strings.

nik = 78
# Indirect printing with f-strings
x = f'hello {6 + 9} {nik}'
print(x)

# Direct printing with f-string
print(f'Hello {nik}')