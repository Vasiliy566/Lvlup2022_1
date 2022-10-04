# Вариант со вводом n
n = int(input())
my_list = []
for i in range(n):
    number = int(input())
    my_list.append(number)


# Длинный вариант
a = input().split()
l = []
for i in range(len(a)):
    l.append(int(a[i]))

# Однострочный
l = [int(x) for x in input().split()]

