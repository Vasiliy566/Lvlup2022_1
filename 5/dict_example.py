my_d = {1: "Value", 2: "Value2"}

# Добавление
my_d["MyKey"] = [1, 2, 3]
my_d["MyKey"] = [1, 2]

if "MyKey" in my_d:
    print(my_d["MyKey"])

# Получение элемента
print(my_d["MyKey"])

# Посмотреть
print(list(my_d.values()))
print(list(my_d.keys()))

for k in my_d.keys():
    print(k)
    print(my_d[k])

for k, v in my_d.items():
    print(f"{k}: {v}")

# дополнительные методы

# get
my_d["MyKey"] = [1, 2]

print("with get:", my_d.get("MyKey1", "Unknown key"))

# update
update_dict = {123: 123, 222: 222}
my_d.update(update_dict)
print(my_d)

# pop
a = my_d.pop("MyKey")
print(a)
print(my_d)

