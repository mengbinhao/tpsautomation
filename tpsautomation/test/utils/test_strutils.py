import pytest
import tpsautomation.utils.strutils as su


def __internal_fun():
    pass


def test_is_str_like():
    assert not su.StrUtils.is_str_like(1)
    assert not su.StrUtils.is_str_like(1.2)
    assert not su.StrUtils.is_str_like({})
    assert not su.StrUtils.is_str_like(True)
    assert not su.StrUtils.is_str_like([1, 2])
    assert not su.StrUtils.is_str_like((1, 2))
    assert not su.StrUtils.is_str_like(None)
    f = __internal_fun
    assert not su.StrUtils.is_str_like(f)

    assert su.StrUtils.is_str_like('1')

    with pytest.raises(TypeError) as excinfo:
        su.StrUtils.is_str_like()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        su.StrUtils.is_str_like(1, 2)
    assert excinfo.type.__name__ == 'TypeError'
