# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 30

# Concatenate
# print('My name is ' + name + ' and I am ' + str(age) + ' age')


# String Formatting

# Arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings
# print(f'Hello, my name is {name} and I am {age} years old')

# String Methods

s = 'hello world'

# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(len(s))
# print(s.replace('world', 'everyone'))
# sub = 'e'
# print(s.count(sub))
print(s.startswith('world'))
print(s.endswith('hello'))
print(s.split())
print(s.find('r'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())

