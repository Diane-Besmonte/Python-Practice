# Variables, Print, Input, and Data Types
# x = input("Enter a first number: ")
# y = input("Enter a second  number: ")
# total = int(x) + int(y)

# print(total)

# Conditionals
# if(int(x) > int(y)):
#     print(x + " is greater than " + y)
# elif(int(x) < int(y)):
#     print(x + " is less than " + y)
# else:
#     print(x + " is equal to " + y)

# For loop
# for i in range(1, 11):
#     print(i)

#While loop
# count = 0
# while count is not 10:
#     print(count)
#     count += 1

# DATA STRUCTURES
# List
# fruits = ["apple", "banana", "orange", "grapes"]
# print("I ate a/an", fruits[1])

# Dictionary
# dictionary = {"motor": "Jett", "color": "Matte Black"}
# print("I have a", dictionary["motor"], "named motor with a color of", dictionary["color"])

# # Append() and pop()
# fruits = ["apple", "banana", "orange", "grapes"]

# Append()
# input = input("Enter a new fruit: ")
# fruits.append(input)
# print(fruits)

# # pop()
# fruits.pop(2)
# print(fruits)

# Comments
# # -> single line comment
# """ + """ multi-line  comment

# Functions
# def addTwoNumbers(x, y):
#     return x + y

# sum = addTwoNumbers(2, 3)
# print(sum)

def countDown(startingNumber):
    while startingNumber > 0:
        print(startingNumber)
        startingNumber -= 1
    print("Zero")
    
countDown(10)