# Длинный вариант
a = input().split()
l = []
for i in range(len(a)):
    l.append(int(a[i]))

# Однострочный
l = [int(x) for x in input().split()]

l = []
for x in input().split():
    l.append(int(x))