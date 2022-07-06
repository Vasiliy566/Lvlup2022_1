from calculator.calucator_funcs import read_input, calculate

x, x1, sign = read_input()
print(x, sign, x1, end=" = ")
result = calculate(x, x1, sign)
if result is not None:
    print(result)
