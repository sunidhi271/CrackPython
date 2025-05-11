# LIST can also be created with strings
# It is allowed to have list mixed with integer, string and floats datatypes.
# It is also allowed to have Lists inside Lists.
# Follow the below example exercise for more clarity.

animals = ['cat', 'dog' ]
print(len(animals))               #O/P: ['cat', 'dog' ]

# animals.append(['tiger'])       #O/P: ['cat', 'dog', ['tiger'] ]
# Also remember that append takes explicitly one argument. It can not take mutiple arguments. 
animals.append('tiger')           
print(animals)                    #O/P: ['cat', 'dog', 'tiger' ]
# To insert mutiple strings you can use extend.
animals.extend(['snake', 'puppy'])   
print(animals)                    #O/P: ['cat', 'dog', 'tiger', 'snake', 'puppy']
# Insert takes two arguments, 1st one should be the index and second one the value to be inserted.
animals.insert(2,'cow')
print(animals)                    #O/P: ['cat', 'dog', 'cow', 'tiger', 'snake', 'puppy']
# List can be extended with + operator as well
animals += ['Lion', 'Monkey']
print(animals)                    #O/P: ['cat', 'dog', 'cow', 'tiger', 'snake', 'puppy', 'Lion', 'Monkey']

animals.remove('cat')             
print(animals)                    #O/P: ['dog', 'cow', 'tiger', 'snake', 'puppy', 'Lion', 'Monkey']

# To delete value on the basis of their index
del animals[3]                    
print(animals)                    #O/P: ['dog', 'cow', 'tiger', 'puppy', 'Lion', 'Monkey']

# If you want to print an item from the last, then you can use Negative Indexing
print(animals[-1])              #O/P: Monkey
print(animals[-4])              #O/P: tiger
