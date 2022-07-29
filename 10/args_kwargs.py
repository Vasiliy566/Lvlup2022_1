def f(a, b, c):
    print(a + b + c)


def f1(*args, **kwargs):
    print(f"Called with args = {args}, kwargs={kwargs}")
    f(*args, **kwargs)


# f1(1, 2, 3, 123, 12, 2, 2, 3, a=111, v=232)
f1(1, 2, c=3)
# f1(a=1, b=2, c=3)
