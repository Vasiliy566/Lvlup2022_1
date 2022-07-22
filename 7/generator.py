def counter():
    i = 1
    while i <= 10:
        yield i
        i += 1
