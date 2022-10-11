import pytest

from leson_4.main import resolve_tri_type


def test_resolve_tri_type():
    a, b, c = 3, 4, 5
    result = resolve_tri_type(a, b, c)
    assert result == "разносторонний"


def test_resolve_tri_type_same():
    a, b, c = 10, 10, 10
    result = resolve_tri_type(a, b, c)
    assert result == "равносторонний"


def test_resolve_tri_type_isosceles():
    a, b, c = 4, 4, 5
    result = resolve_tri_type(a, b, c)
    assert result == "равнобедренный"

    a, b, c = 3, 5, 3
    result = resolve_tri_type(a, b, c)
    assert result == "равнобедренный"

    a, b, c = 3, 7, 7
    result = resolve_tri_type(a, b, c)
    assert result == "равнобедренный"


def test_resolve_tri_type_incorrect_input():
    a, b, c = -1, 2, 3
    with pytest.raises(ValueError):
        resolve_tri_type(a, b, c)

