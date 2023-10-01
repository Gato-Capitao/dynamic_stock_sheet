from pytest import mark
from collector import sum


@mark.parametrize("num1, num2, r", [
    (1, 2, 3),
    (2, 3, 5),
    (4, 4, 8),
    (2, 2, 4)
])

def test_sum(num1:int, num2:int, r:int) -> None:
    assert sum(num1, num2) == r

