import random

# Variable Declaration
name = "Vitor"
age = 27

# Case Sensitive
Name = "Vitor"  # <> name

# Variable type
typeStr = type(name)

# Input
get_name = input('What is your name? ')

# String length
nameLength = len(get_name)

# Number concatenation
numberConcat = str(5) + "5"

# String detection
x = "abc".isnumeric()  # false
y = "123".isnumeric()  # true

# Multi Line String
multiLine = """multi
line
string"""

# Random
print(random.random())
print(random.randint(10, 20))
print(random.choice([1, 2, 3]))
print(random.sample([1, 2, 3], 2))

# *** Operators ***
# Arithmetic
print(20 + 10)
print(30 - 10)
print(3 * 10)
print(12 / 4)
print(12 // 4)  # Integer division
print(12 % 4)
print(12 ** 5)  # Power
# Comparison
print(3 == 3)
print(3 > 3)
print(3 >= 3)
print(3 < 3)
print(3 <= 3)
# Logical
print(3 == 3 and 4 > 3)
print(3 == 3 or 3 < 3)
print(3 == 3 and not 3 > 3)
# Assingment
a = 10
a += 10
# Conditional
x = 20 if a > 10 else 30
print(x)

# List
decList = ['1', '2', '3']
print(len(decList))
print(decList[1:2])
print(decList[-3])
decList.append("4")
del decList[1]
print(decList)
