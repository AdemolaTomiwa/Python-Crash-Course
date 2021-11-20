# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a function
# def sayHello(name):
#     print(f'Hello {name}, Welcome to THE TOM MEDIA')

# def sayHello(name = 'Sam'):
#     print(f'Hello {name}, Welcome to THE TOM MEDIA')


# sayHello('John Doe'.upper())
# sayHello()

# Return values
# def getSum(num1, num2):
#     total = num1 + num2 * 5
#     return total

# # print(getSum(5, 10))
# num = getSum(5, 10)

# print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2 *10

print(getSum(5, 10))