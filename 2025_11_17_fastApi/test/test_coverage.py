def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


def test_add() -> None:
    a, b = 1, 2
    result = add(a, b)
    assert result == 3
