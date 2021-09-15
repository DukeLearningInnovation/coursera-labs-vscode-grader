import assign1
import pytest


@pytest.mark.parametrize("input, expected",[
    ("World", "Hello World!"),
    ("Drew", "Hello Drew!"),
    ("🤖", "Hello 🤖!")
])
def test_greet(input, expected, mocker):
    # Using a pytest-mock spy to make sure the helper function
    # is used and has the expected output
    spy = mocker.spy(assign1, "helper")
    assert expected == assign1.greet(input), "greet() does not return the expected greeting"
    assert spy.call_count == 1, "you didn't call your helper function within the greet function"
    assert spy.spy_return == f"{input}!", ("check your helper function implementation and "
                                           "be sure it passes the included test")


def test_greet_no_args():
    try:
        result = assign1.greet()
    except TypeError:
        result = ''
    assert result != '', "greet() does not handle missing argument"
    assert "Hello World!" == result, "greet() does not have the expected default parameter value"
