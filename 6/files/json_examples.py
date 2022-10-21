import json

with open('json_data.json') as json_file:
    data = json.load(json_file)
    print(data)


data2 = {"User": 1, "User2": 2}
with open('json_data2.json', "w") as json_file:
    json.dump(data2, json_file)
