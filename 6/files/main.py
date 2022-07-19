import matplotlib.pyplot as plt


def f(x, a, b, c):
    return (a * x ** 2) + (b * x) + c


a, b, c = 1, 2, -3

x_coords = [x for x in range(-10, 10, 1)]

y_coords = []
for x in x_coords:
    y_coords.append(f(x, a, b, c))

plt.plot(x_coords, y_coords)
plt.show()
