a = ["a001", "a002", "a003"]
b = ["Иван Иванов", "Петр Петров", "Сидор Сидоров"]
c = [55, 70, 88]

# [{a: {b:c}},]

students = []
for i in range(len(a)):
    group_number = a[i]
    name = b[i]
    mark = c[i]

    d = {}
    d_m = {name: mark}
    d[group_number] = d_m

    students.append(d)
print(students)
