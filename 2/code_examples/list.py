my_list = ['p', 'r', 'o', 'b', 'e']
#           0    1    2    3    4
#          -5    -4   -3   -2  -1
print(my_list[0])  # p

print(my_list[-1])

print(len(my_list))

# получаем элементы со второго по четвертый - [2:5)
print(my_list[2:5])

# Добавление
my_list.append("Hey!")
print(my_list[0])  # p

# Сложение и умножение списков
new_list = ["additional", "list"]
print(my_list + new_list)

some_list = [1, 2, 3]
print(some_list * 3)


# Удаление
my_list.remove('p')
print(my_list)


# списки  циклы
for i in my_list:
    print(i)
