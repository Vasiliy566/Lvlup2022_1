f1 = input()
f2 = input()


try:
    f1 = open(f1)
    f2 = open(f2, mode="w")
except FileNotFoundError:
    print("Файл не найден")
else:
    lines = f1.readlines()
    for line in lines:
        if not line.startswith("#"):
            f2.write(line)
    f1.close()
    f2.close()


# else:
#     ...
# finally:
#     ...
