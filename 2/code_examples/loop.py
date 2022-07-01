# for
# range (начальное число, конечное число, шаг)
# по умолчанию range(X) = range(0, X, 1)
for x in range(6):
    print(x)

for x in range(0, 6, 1):
    print(x)

# while
# while (выражение = True)

i = 1
while i < 6:
    print(i)
    i += 1

# Break - выход
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Continue - пропустить итерацию
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# else для циклов - если вышли через break, то не отработает

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
  print("Here we go!")
