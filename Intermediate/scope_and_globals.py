#SCOPE AND GLOBALS

#Demonstration Samples:
x = 'Nikolai'

def function(name):
    global x #Makes the variable for global access. Must only be used in rare cases.
    x = name

print(x)
function('changed')
print(x)