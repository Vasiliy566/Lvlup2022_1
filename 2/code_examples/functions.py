"""
def <имя функции>(аргумент1, аргумент2):
    логика работы с аргументами
"""


def math_operations(a, b):
    def sum_n(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    s = sum_n(a, b)
    m = multiply(a, b)

    print(s, m)


a, b = 10, 20
math_operations(a, b)


