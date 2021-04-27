import json

j = {"Name": "Vitor", "Age": 27}

print(json.dumps(j, indent=4))

with open('json.txt', 'w') as json_file:
    json.dump(j, json_file, indent=4)

with open('json.txt', 'r') as json_file:
    print(json.load(json_file))

with open('json.txt', 'r') as json_file:
    print(json_file.read())
