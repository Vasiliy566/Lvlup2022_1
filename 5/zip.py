names = {"Иван", "Петр", "Петр"}
moneys = tuple([1000, 1500, 1000])

# for a, b, c in zip(names, moneys, pets):
#     print(f"{a} with dog {b} spent {c} moneys")








# a = [i for i in range(10)]

names = ["Ivan", "Sergey", "Name3"]
s_names = ["Ivanov", "Petrov", "Name3"]


# for name, s_name in zip(names, s_names):
#     d[name] = s_name


d = {i: i ** 2 for i in range(10) if i % 2 == 0}

print(d)