import json

data = {
    'employees': [
        {
            'name': 'John Doe',
            'department': 'Marketing',
            'place': 'Remote'
        },
        {
            'name': 'Jane Doe',
            'department': 'Software Engineering',
            'place': 'Remote'
        },
    ]
}


with open('json_data.json', 'w') as outfile:
    json.dump(data, outfile)

with open('json_data.json') as json_file:
    data = json.load(json_file)
    print(data)
