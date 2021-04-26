dic = {"Teste": 1, "Teste2": 2}
dic2 = dict({"Teste": 1})
dic3 = {"Teste": [1, 2, 3]}
print(dic)
print(dic2)

print(dic["Teste"])
print(dic.get("Teste2"))
print(dic3["Teste"][1])

# Update
dic["Teste"] = 2

# Add
dic["Teste5"] = 20

# Delete
del dic["Teste5"]
