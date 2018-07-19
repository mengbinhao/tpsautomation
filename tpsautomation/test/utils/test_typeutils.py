import pytest
# from tpsautomation.utils.typeutils import *
import tpsautomation.utils.typeutils as tu


def __internal_fun():
    pass


def test_is_dict():
    assert not tu.TypeUtils.is_dict(1)
    assert not tu.TypeUtils.is_dict(1.2)
    assert not tu.TypeUtils.is_dict('1')
    assert not tu.TypeUtils.is_dict(True)
    assert not tu.TypeUtils.is_dict([1, 2])
    assert not tu.TypeUtils.is_dict((1, 2))
    assert not tu.TypeUtils.is_dict(None)
    f = __internal_fun
    assert not tu.TypeUtils.is_dict(f)

    assert tu.TypeUtils.is_dict({})

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_dict()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_dict(1, 2)
    assert excinfo.type.__name__ == 'TypeError'


def test_is_int():
    assert not tu.TypeUtils.is_int(1.2)
    assert not tu.TypeUtils.is_int('1')
    assert not tu.TypeUtils.is_int(True)
    assert not tu.TypeUtils.is_int([1, 2])
    assert not tu.TypeUtils.is_int((1, 2))
    assert not tu.TypeUtils.is_int(None)
    f = __internal_fun
    assert not tu.TypeUtils.is_int(f)
    assert not tu.TypeUtils.is_int({})

    assert tu.TypeUtils.is_int(1)

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_int()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_int(1, 2)
    assert excinfo.type.__name__ == 'TypeError'


def test_is_float():
    assert not tu.TypeUtils.is_float(1)
    assert not tu.TypeUtils.is_float('1')
    assert not tu.TypeUtils.is_float(True)
    assert not tu.TypeUtils.is_float([1, 2])
    assert not tu.TypeUtils.is_float((1, 2))
    assert not tu.TypeUtils.is_float(None)
    f = __internal_fun
    assert not tu.TypeUtils.is_float(f)
    assert not tu.TypeUtils.is_float({})

    assert tu.TypeUtils.is_float(1.2)

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_float()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_float(1, 2)
    assert excinfo.type.__name__ == 'TypeError'


def test_is_str():
    assert not tu.TypeUtils.is_str(1)
    assert not tu.TypeUtils.is_str(1.2)
    assert not tu.TypeUtils.is_str(True)
    assert not tu.TypeUtils.is_str([1, 2])
    assert not tu.TypeUtils.is_str((1, 2))
    assert not tu.TypeUtils.is_str(None)
    f = __internal_fun
    assert not tu.TypeUtils.is_str(f)
    assert not tu.TypeUtils.is_str({})

    assert tu.TypeUtils.is_str('1')

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_str()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_str(1, 2)
    assert excinfo.type.__name__ == 'TypeError'


def test_is_bool():
    assert not tu.TypeUtils.is_bool(1)
    assert not tu.TypeUtils.is_bool('1')
    assert not tu.TypeUtils.is_bool(1.2)
    assert not tu.TypeUtils.is_bool([1, 2])
    assert not tu.TypeUtils.is_bool((1, 2))
    assert not tu.TypeUtils.is_bool(None)
    f = __internal_fun
    assert not tu.TypeUtils.is_bool(f)
    assert not tu.TypeUtils.is_bool({})

    assert tu.TypeUtils.is_bool(True)

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_bool()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_bool(1, 2)
    assert excinfo.type.__name__ == 'TypeError'


def test_is_tuple():
    assert not tu.TypeUtils.is_tuple(1)
    assert not tu.TypeUtils.is_tuple('1')
    assert not tu.TypeUtils.is_tuple(True)
    assert not tu.TypeUtils.is_tuple([1, 2])
    assert not tu.TypeUtils.is_tuple(1.2)
    assert not tu.TypeUtils.is_tuple(None)
    f = __internal_fun
    assert not tu.TypeUtils.is_tuple(f)
    assert not tu.TypeUtils.is_tuple({})

    assert tu.TypeUtils.is_tuple((1, 2))

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_tuple()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_tuple(1, 2)
    assert excinfo.type.__name__ == 'TypeError'


def test_is_list():
    assert not tu.TypeUtils.is_list(1)
    assert not tu.TypeUtils.is_list('1')
    assert not tu.TypeUtils.is_list(True)
    assert not tu.TypeUtils.is_list((1, 2))
    assert not tu.TypeUtils.is_list(1.2)
    assert not tu.TypeUtils.is_list(None)
    f = __internal_fun
    assert not tu.TypeUtils.is_list(f)
    assert not tu.TypeUtils.is_list({})

    assert tu.TypeUtils.is_list([1, 2])

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_list()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_list(1, 2)
    assert excinfo.type.__name__ == 'TypeError'


def test_is_none():
    assert not tu.TypeUtils.is_none(1)
    assert not tu.TypeUtils.is_dict(1.2)
    assert not tu.TypeUtils.is_none('1')
    assert not tu.TypeUtils.is_none(True)
    assert not tu.TypeUtils.is_none([1, 2])
    assert not tu.TypeUtils.is_none((1, 2))
    assert not tu.TypeUtils.is_none({})
    f = __internal_fun
    assert not tu.TypeUtils.is_none(f)

    assert tu.TypeUtils.is_none(None)
    assert tu.TypeUtils.is_none()

    with pytest.raises(TypeError) as excinfo:
        tu.TypeUtils.is_none(1, 2)
    assert excinfo.type.__name__ == 'TypeError'
