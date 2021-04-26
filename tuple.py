t = ("1", "2")
x = ("1",)

# List inside tuple
mixed = ("1", ["2", "3"], "4", "5")

# Picking item
print(mixed[0])
print(mixed[0:2])

# Concatenation
y = t + x + mixed
print(y)

del t
print(t)
