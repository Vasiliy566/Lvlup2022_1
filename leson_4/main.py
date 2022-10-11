def resolve_tri_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть больше нуля")
    if a == b and a == c and b == c:
        return "равносторонний"
    elif a == b or b == c or a == c:
        return "равнобедренный"
    else:
        return "разносторонний"


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    result = resolve_tri_type(a, b, c)

    print(result)
