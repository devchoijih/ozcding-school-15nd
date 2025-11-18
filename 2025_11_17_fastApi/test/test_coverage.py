from test.math_temp.function import add, mul

def test_add() -> None:
    a, b = 1, 2
    result = add(a, b)
    assert result == 3
