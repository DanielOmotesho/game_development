mydictionary={
    'India':'New Delhi',
    'Canada':'Ottawa',
    'Britain':'London',}

#accessing the values
print(mydictionary['India'])

#updating the values
mydictionary['Britain']="glasgow"
print(mydictionary)

#adding values
mydictionary['France']="Paris"
print(mydictionary)

#removing values

del mydictionary['Britain']
print(mydictionary)

#reading the keys
for k in mydictionary.keys():
    print(mydictionary[k])

#reading the values
for e in mydictionary.values():
    print(e)

#finding length of dictionary
print(len(mydictionary))