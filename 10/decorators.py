from datetime import datetime


def how_long_it_runs(decorate_f):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        decorate_f(*args, **kwargs)
        later = datetime.now()
        print(later - now)

    return wrapper


@how_long_it_runs
def f(a, b, c):
    for i in range(100000):
        s = a + b + c
    print(s)


@how_long_it_runs
def f1(a, b, c):
    print(a * b * c)


@how_long_it_runs
def f2(a, b, c):
    print(a ** b ** c)


f(1, 2, 3)
f1(1, 2, 3)
f2(1, 2, 3)