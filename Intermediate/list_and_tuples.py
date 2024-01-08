#List and Tuples

#List is an ordered collection
#Uses brackets
x = [4, True, "Nikolai"]
y = 'hello'
x.append("Dostoevskiy") #Adds the element to the list
print(x, len(y))
x.extend([1,2,3]) #Adds an additional list elements to the list
print(x)
print(x.pop(0)) #Prints or return the last element(by default unless specified with index) 
#and remove it from the list
print(x)
#We can access a specific element with the bracket and index number of the element
print(x[2])
#We can also change the element on a specific index value of the list
y = x[:] #Takes the original value of x
x[2] = 'Fyodor'
print(x[2])

#Lists are mutable, they can be changes and the elements can be changed
#They can be updated for the whole program "reference call".

print(x, y)

#Tuples are ordered collection but they are immutable or cannot be changed
#They use parenthesis
b = (0, 0, 2, 2)

#Note we can use a list within a list or a tuple within a list and so on.
