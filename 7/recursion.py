#   0 1 1 2 3 5 8 13
# n 1 2 3 4 5 6 7 8
# Fn = Fn - 1 + Fn - 2
def fib(n):
    if n == 1:
        return 0

    if n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


print(fib(8))
