import pytest
import tpsautomation.model.user as u


def test_instantiation():
    u1 = u.User(1, 'jack', '123', 6)
    print(u1)

    with pytest.raises(TypeError) as excinfo:
        u.User(1, 'jack')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        u.User(1, 'jack', 1111, 6)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        u.User(1, 'jack', '', 6)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        u.User(1, 'jack', '123456789098765', 6)
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        u.User(1, 'jack', '123', '6')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        u.User(1, 'jack', '123', 7)
    assert excinfo.type.__name__ == 'ValueError'
