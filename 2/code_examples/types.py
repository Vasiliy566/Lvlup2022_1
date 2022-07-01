# Базовые операции и данные

# Числа

# Целые
a = 5
a_type = type(a)
print(type(a))

# С плавающей точкой (13.33)
f = 13.33
f_type = type(f)
print(type(f))


# Строки
b = "Hello there"
b_type = type(b)
print(type(b))

# Логические
c = True
c_type = type(c)
print(type(c))

# Преобразование типов

# Число-> строка
some_string = "5"
print(type(some_string))

some_int = int(some_string)
print(type(some_int))

# Логические
logical = some_int == some_string
print(logical)

logical = some_int == 5
print(logical)

