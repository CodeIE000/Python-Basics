#For Loops
for i in range(1, 10):
    print(i)
#Range order of argument
#stop if one arg
#start stop if two args
#start, stop, step if three args
#Range is a function that creates a collection of numbers based on the input that we give it.
#Default it will start a 0 and stop at whatever number you place inside the parenthesis but won't include that number .
    
for x in [1,2,3,4,5,1,2]:
    print(x)

a = [1,123,13,1,5,3,]

for z in range(len(a)):
    print(a[z])

for z, index in enumerate(a):
    print(z, index)