
# if else

num = 50

if num > 10:
    print("Greater")
else:
    print("Lower")

if num > 50:
    print("if")
elif 10 < num >= 50:
    print("elif")
else:
    print("else")

# Ternary Operator
x = 10
print("Smaller than 10" if x < 10 else "Greater or equal 10")

# While
y = 1

while y < 10:
    print(y)
    y += 1
    if y == 5:
        break

# While..else
while y < 5:
    print(y)
    y += 1
    # with break, the else block doesn't execute
    # if y == 2:
    #    break
else:
    print(y)

# For loopx
l = ["Vitor", "Tais"]
for i in l:
    print(i)

