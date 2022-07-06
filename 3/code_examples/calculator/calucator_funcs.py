def read_input():
    in_str = input().split()  # ["23", "+", "11"]
    x = in_str[0]
    x1 = in_str[2]
    sign = in_str[1]
    return int(x), int(x1), sign


# x - число, x1 - число, sign - строка, знак операции
def calculate(x, x1, sign):
    if sign == "+":
        return x + x1
    elif sign == "-":
        return x - x1
    elif sign == "*":
        return x * x1
    elif sign == "/":
        if x1 == 0:
            print("Знаменатель не равен нулю!")
        else:
            return x / x1


if __name__ == "__main__":
    read_input()