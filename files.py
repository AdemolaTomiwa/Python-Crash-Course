# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myFile.txt', 'w')

# Get info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I Love Python')
myFile.write(' and Javascript')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write(', I also like SASS')

# Read from a file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)