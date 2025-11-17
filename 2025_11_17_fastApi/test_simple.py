def add(a : int, b : int) -> int:
    return a + b

def test_add() -> None:
    # Given: 무엇인가 주어졌을때
    # 버그는 "경계"를 좋아함
    a, b = 1, 1

    result = add(a, b)

    assert result == 2
    if not result == 2: raise AssertionError

