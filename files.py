# Open and write file
f = open('file.txt', 'w')
f.write('Writing Test')

# Open and read file
f = open('file.txt', 'r')
text = f.read()
print(text)
