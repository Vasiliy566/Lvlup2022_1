from math import pi


def is_correct_circle(r):
    if r < 0:
        raise Exception("Радиус круга < 0")


def get_square(r):
    is_correct_circle(r)
    return pi * (r ** 2)
