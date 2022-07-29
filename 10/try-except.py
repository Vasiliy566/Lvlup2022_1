try:
    f = open("test1.txt")
    print(f.readlines())
except FileNotFoundError:
    print("Не могу найти файл test.txt")
else:
    print(f.readlines())
finally:
    print("Все закончилось.")


# else:
#     ...
# finally:
#     ...
