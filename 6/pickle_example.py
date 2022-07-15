import pickle

data = [123, "test", [1, 2, 3]]

with open('important', 'wb') as file:
    pickle.dump(data, file)


with open('important', 'rb') as file:
    data = pickle.load(file)
    print(data)