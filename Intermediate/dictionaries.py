#Dictionaries 
#Are key valued pairs

x = {'key': 2}
print(x['key']) 

#Adding key to existing dictionary
x['key2'] = 5
x[2] = [1,2,3,4,5,6]

print(x)
print('key' in x) #Checks if a key is in the dictionary
print(x.values()) #Gives the values of the dictionary
print(list(x.values())) #"" as list
print(list(x.keys())) # " " gives the list of keys
del x['key2'] #deletes a key
print(list(x.keys())) # " " gives the list of keys

for key, value in x.items():
    print(key, value)

for key in x:
    print(key, x[key]) 