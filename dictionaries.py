# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create Dict
person = {
    'first_name': 'John',
    'last_name':'Doe',
    'age':30
}

# Use a constructor
# person2 = dict(first_name='Sara', last_name='William')
# print(person2, type(person2))

# print(person, type(person))

# Get value
# print(person['first_name'])
# print(person.get('last_name'))

# Add key/value
# person['phone'] = '555 555 5555'

# # Get Dict keys
# print(person.keys())

# # Get Dict items
# print(person.items())

# print(person)

# Copy dict
# person2 = person.copy()
# person2['city'] = 'Boston'

# print(person2)

# Remove an item
# del person['age']
# person.pop('first_name')

# Clear
# person.clear()

# Length

# print(len(person))

# print(person)

# List of dict
people = [
    {'name':'John Doe', 'age': 50},
    {'name':'Kevin Jiden', 'age': 25}
]

print(people)
print(people[0]['name'])