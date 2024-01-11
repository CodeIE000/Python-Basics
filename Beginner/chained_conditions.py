# CHAINED CONDITIONS

# Definition:
# Chained conditions is combining multiple conditions together to create one larger condition.
# Keywords used: and, or, not

# Demonstration Samples:
x = 7
y = 8
z = 0

result1 = x == y 
result2 = y > x
result3 = z < x + 2

result4 = result1 or not result2 or result3
result5 = result1 and result3
print(result4)
print(result5)

print(not False)
print(not (False or True))
print(not (False and True))