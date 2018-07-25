import sys
import pytest


def inc(x):
    return x + 1


@pytest.mark.xfail
def test_answer():
    assert inc(3) == 5


@pytest.mark.xfail
def test_wcf():
    assert inc(3) > 5


def test_hy():
    assert inc(3) < 5


def test_recursion_depth():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1/0
    assert excinfo.type.__name__ == 'ZeroDivisionError'


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("7*9", 63), ])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    assert 0


@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6")
def test_function():
    assert 0 == 0


"""
@pytest.mark.skipif(not pytest.config.getoption("--runslow"))
def test_func_slow_1():
    print('skip slow')
"""
