my_tuple=("hello",51,6.1,True)
print(my_tuple)
my_tuple="hello",51,6.1,True
#indexing
print(my_tuple)
print (my_tuple[3])

#my_tuple.append("daniel")
print(len(my_tuple))

for i in my_tuple:
    print(i)

#unpacking
details=("daniel",12,"london","mac and cheese")
name,Age,city,food=details
print(food)

#concatonate
print (details+my_tuple)

#repitition
print(my_tuple*3)

#delete
del my_tuple
print(my_tuple)


a=tuple((1,2,23,"okay"))