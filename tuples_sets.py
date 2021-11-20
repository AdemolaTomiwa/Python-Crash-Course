# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# create tuples
fruits = ('Apples', 'Mangoes', 'Pineapples')

# Use constructor
# fruits2 = tuple(('Apples', 'Mangoes', 'Pineapples'))

# Single value needs trailing comma
# fruits2 = ('Apples',)

# print(fruits2, type(fruits2))

# Get value
# print(fruits[1])

# You can't change value
# fruits[0] = 'Pears'

# Delete
# del fruits

# print(len(fruits))
 


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Creates a set
cars = {'Ford', 'Toyota', 'Nissan', 'Tesla'}

# print(cars, type(cars))

# Check if in set
# print('Ford' in cars)

# Add to set
# cars.add('Ferrari')

# Add duplicate member
cars.add('Ford')

# remove from to set
# cars.remove('Ford')

# clear set
# cars.clear()

# Delete set
# del cars

print(cars)