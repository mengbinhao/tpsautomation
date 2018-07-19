import pytest
import tpsautomation.utils.listutils as lu


def test_filter_empty_string_in_list():
    l_with_str_empty = ['1', '', '    ']
    assert len(lu.ListUtils.filter_empty_string_in_list(l_with_str_empty)) == 1

    l_with_other_type = ['1', '', '    ', 1]
    with pytest.raises(AttributeError) as excinfo:
        lu.ListUtils.filter_empty_string_in_list(l_with_other_type)
    assert excinfo.type.__name__ == 'AttributeError'


def test_join_list_by_symbol():
    assert lu.ListUtils.join_list_by_symbol(':', ['j','a','c','k']) == 'j:a:c:k'

    assert lu.ListUtils.join_list_by_symbol(':', []) == ''

    with pytest.raises(TypeError) as excinfo:
        lu.ListUtils.join_list_by_symbol(':', [1])
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        lu.ListUtils.join_list_by_symbol(':', (1))
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        lu.ListUtils.join_list_by_symbol(':')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        lu.ListUtils.join_list_by_symbol()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(AttributeError) as excinfo:
        lu.ListUtils.join_list_by_symbol(1, ['j','a','c','k'])
    assert excinfo.type.__name__ == 'AttributeError'

def test_remove_duplicate():
    assert len(lu.ListUtils.remove_duplicate([1,2,2,3,3,3,4,'5','4','5'])) == 6
    assert len(lu.ListUtils.remove_duplicate([])) == 0

    with pytest.raises(TypeError) as excinfo:
        assert len(lu.ListUtils.remove_duplicate(1)) == 0
    assert excinfo.type.__name__ == 'TypeError'
    
    with pytest.raises(TypeError) as excinfo:
        lu.ListUtils.remove_duplicate([{}])
    assert excinfo.type.__name__ == 'TypeError'

def test_remove_duplicate():
    assert lu.ListUtils.is_exist_in_list(['1','2','3'], '3') is True

    assert lu.ListUtils.is_exist_in_list(['1','2','3'], '4') is False

    assert lu.ListUtils.is_exist_in_list([], '4') is False

    with pytest.raises(TypeError) as excinfo:
        lu.ListUtils.is_exist_in_list(['1','2','3'], 3)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        lu.ListUtils.is_exist_in_list()
    assert excinfo.type.__name__ == 'TypeError'