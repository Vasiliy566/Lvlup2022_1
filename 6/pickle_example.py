import pickle
#
data = set([x for x in range(123)])
print(data)
with open('important.pickle', 'wb') as file:
    pickle.dump(data, file)

with open('important.pickle', 'rb') as file:
    data = pickle.load(file)
    print(data)