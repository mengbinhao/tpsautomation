import pytest
import tpsautomation.model.case as c


def test_instantiation():
    c1 = c.Case(1, 'jack', True, 11, 111, 111, 'test address', '18088888888', 'test note')
    #print(c1)
    c2 = c.Case(1, 'jack', True)
    #print(c2)
    c3 = c.Case(1, 'jack', True,22)
    #print(c3)
    # do not work 
    # do not work 
    # do not work 
    # do not work 
    c3.name = "ddddd"
    #print(c3)

    with pytest.raises(TypeError) as excinfo:
        c.Case(1, 123, True)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, '', True)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, '    ', True)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        c.Case('ddd', 'jack', True)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(-1, 'jack', True)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(111111, 'jack', True)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        c.Case(1, 'jack', 1)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        c.Case(1, 'jack', True,'jack')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, 'jack', True,-1)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, 'jack', True,300)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        c.Case(1, 'jack', True, 50, 'ddqqdwq')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, 'jack', True, 50, -1)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, 'jack', True, 50, 10000)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        c.Case(1, 'jack', True, 50, 100,'jack')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, 'jack', True, 50, 100, -1)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, 'jack', True, 50, 100, 100000)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        c.Case(1, 'jack', True, 50, 100, 180, 111)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, 'jack', True, 50, 100, 180, 'a' * 200)
    assert excinfo.type.__name__ == 'ValueError'

    c.Case(1, 'jack', True, 50, 100, 180, 'test address', '18088888888')
    c.Case(1, 'jack', True, 50, 100, 180, 'test address', 18088888888)

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, 'jack', True, 50, 100, 180, 'test address', 180888888888888)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, 'jack', True, 50, 100, 180, 'test address', '180888188888')
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, 'jack', True, 50, 100, 180, 'test address', 'fwfwfwfew')
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        c.Case(1, 'jack', True, 50, 100, 180, 'test address', 18088888888, 1111)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        c.Case(1, 'jack', True, 50, 100, 180, 'test address', 18088888888, 'a' * 100000)
    assert excinfo.type.__name__ == 'ValueError'