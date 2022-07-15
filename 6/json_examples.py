import json

#

with open('json_data.json') as json_file:
    data = json.load(json_file)
    print(data['Тест1'])
