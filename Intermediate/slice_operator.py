#SLICE OPERATOR

#Demonstration Samples:
x = [0,1,2,3,4,5,6,7,8,9]
y = ["Hi", "Hello", "Sure", "Cya"]
z = "Hello"

sliced1 = x[0:9:2]
sliced2 = y[:2:]
sliced3 = z[::-1]
sliced4 = (1,2,3,4,5,6,7,8,9,10)[::-1]

print(sliced1)
print(sliced2)
print(sliced3)
print(sliced4)

#Slice order of argument is the same as for loop, Stop, Start-Stop, Start-Stop-Step
#Stop stops at the specified element but doesn't include that element
#Default for start is beginning, stop is end, step is one