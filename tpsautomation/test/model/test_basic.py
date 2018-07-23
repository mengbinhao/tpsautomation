import pytest
import tpsautomation.model.basic as p


def test_instantiation():
    p1 = p.Basic(1, 'jack')
    print(p1)

    # do not work, have to set name
    # do not work, have to set name
    p1.name = "do not work"
    print(p1)

    with pytest.raises(TypeError) as excinfo:
        p.Basic(1, 'jack', 2)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        p.Basic()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        p.Basic(1, 2)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        p.Basic(1, '           ')
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        p.Basic(1, 'a' * 333)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        p.Basic('2', 'jack')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        p.Basic(-1, 'jack')
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        p.Basic(1000000, 'jack')
    assert excinfo.type.__name__ == 'ValueError'
