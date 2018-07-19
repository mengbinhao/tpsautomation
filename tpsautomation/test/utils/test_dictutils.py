import pytest
# from tpsautomation.utils.dictutils import *
# from tpsautomation.utils.typeutils import *
import tpsautomation.utils.typeutils as tu
import tpsautomation.utils.dictutils as du
import tpsautomation.utils.dateandtimeutils as datu
import tpsautomation.model.caseresult as cr


def test_make_dict():
    with pytest.raises(TypeError) as excinfo:
        du.DictUtils.make_dict('2')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        du.DictUtils.make_dict({'a': 1, 'b': 2})
    assert excinfo.type.__name__ == 'TypeError'

    d = {'a': 1, 'b': 2}

    with pytest.raises(TypeError) as excinfo:
        du.DictUtils.make_dict(d)
    assert excinfo.type.__name__ == 'TypeError'

    assert tu.TypeUtils.is_dict(du.DictUtils.make_dict(red=1, green=2, blue=3))

    assert tu.TypeUtils.is_dict(du.DictUtils.make_dict(**d))
    # return {}
    assert tu.TypeUtils.is_dict(du.DictUtils.make_dict())


def test_add_word_to_dict():
    # return {}
    assert tu.TypeUtils.is_dict(du.DictUtils.make_dict())

    d = {'a': 1, 'b': 2}
    e = {'b': 3, 'c': 4}
    ret = du.DictUtils.add_word_to_dict(*d.items(), **e)
    assert 3 in ret.values()
    assert 4 in ret.values()
    assert 'c' in ret.keys()

    ret2 = du.DictUtils.add_word_to_dict(*d.items(), yellow=22, green=33)
    assert 'yellow' in ret2.keys()
    assert 'green' in ret2.keys()
    assert 22 in ret2.values()
    assert 33 in ret2.values()

    assert tu.TypeUtils.is_dict(
        du.DictUtils.add_word_to_dict(*d.items(), ))

    with pytest.raises(TypeError) as excinfo:
        du.DictUtils.add_word_to_dict(*d.items(), None)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        du.DictUtils.add_word_to_dict(*d.items(), '12313')
    assert excinfo.type.__name__ == 'ValueError'


def test_get_intersection_key_of_two_dict():
    d = {'a': 1, 'b': 2, 'c': 3}
    e = {'b': 2, 'c': 3, 'd': 4}

    assert tu.TypeUtils.is_list(
        du.DictUtils.get_intersection_key_of_two_dict(d, e))

    with pytest.raises(TypeError) as excinfo:
        du.DictUtils.get_intersection_key_of_two_dict()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
         du.DictUtils.get_intersection_key_of_two_dict(None, None)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
         du.DictUtils.get_intersection_key_of_two_dict(d, 1)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
         du.DictUtils.get_intersection_key_of_two_dict(1, d)
    assert excinfo.type.__name__ == 'TypeError'


def test_get_specific_word_value():
    d = {'a': 1, 'b': 2}
    key = 'a'
    t = (1, 2, 3)
    l = [1, 2, 3]

    assert du.DictUtils.get_specific_word_value(d, key) != 'not found'
    assert du.DictUtils.get_specific_word_value(d, 'c') == 'not found'
    assert du.DictUtils.get_specific_word_value(d, None) == 'not found'
    assert du.DictUtils.get_specific_word_value(d, True) == 'not found'
    assert du.DictUtils.get_specific_word_value(d, 1) == 'not found'
    assert du.DictUtils.get_specific_word_value(d, 1.2) == 'not found'
    assert du.DictUtils.get_specific_word_value(d, t) == 'not found'

    with pytest.raises(TypeError) as excinfo:
        du.DictUtils.get_specific_word_value(d,)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        du.DictUtils.get_specific_word_value(d, l)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        du.DictUtils.get_specific_word_value(d, d)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(AttributeError) as excinfo:
        du.DictUtils.get_specific_word_value(None, key)
    assert excinfo.type.__name__ == 'AttributeError'

    with pytest.raises(AttributeError) as excinfo:
        du.DictUtils.get_specific_word_value(1, key)
    assert excinfo.type.__name__ == 'AttributeError'

    with pytest.raises(AttributeError) as excinfo:
        du.DictUtils.get_specific_word_value('1', key)
    assert excinfo.type.__name__ == 'AttributeError'

    with pytest.raises(AttributeError) as excinfo:
        du.DictUtils.get_specific_word_value(t, key)
    assert excinfo.type.__name__ == 'AttributeError'

    with pytest.raises(AttributeError) as excinfo:
        du.DictUtils.get_specific_word_value(l, key)
    assert excinfo.type.__name__ == 'AttributeError'


def test_class_to_dict():
    c1 = cr.CaseResult(1, 'case01', 'pass', datu.DateAndTimeUtils.get_today_as_str(), 333, 'success', 'laaaaaaaaa')
    #print(c1.__dict__)
    print(du.DictUtils.class_to_dict(c1))