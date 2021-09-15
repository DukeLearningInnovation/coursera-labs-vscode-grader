import assign2
import pytest


@pytest.mark.parametrize("input, expected", [
    ((2, 4), 6),
    ((1, 2.4), 3.4),
    (("add", "ing"), "adding"),
    (([1, 2], [3, 4]), [1, 2, 3, 4])
])
def test_add(input, expected):
    assert expected == assign2.add(input[0], input[1])
