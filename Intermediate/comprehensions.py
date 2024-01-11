# COMPREHENSIONS

# Demonstration Samples:
x = [x for x in range(5)]
print(x)
x = [x + 4 for x in range(5)]
print(x)
x = [x % 4 for x in range(5)]
print(x)
x = [0 for x in range(5)]
print(x)

x = [[0 for x in range(20)] for x in range(5)]
print(x)

x = [i for i in range(20) if i % 5 == 0]
print(x)

x = {i: 0 for i in range(20) if i % 5 == 0}
print(x)