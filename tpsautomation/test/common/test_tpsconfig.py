import pytest
import tpsautomation.common.tpsconfig as c

""" first to run for init config """


def test_init_config():
    c.ConfigWrapper.init_config()
    c.ConfigWrapper.init_config()
    # print(c.ConfigWrapper.config)
    assert id(c.ConfigWrapper.config) == id(
        c.ConfigWrapper.config) and len(c.ConfigWrapper.config) > 0
    c.ConfigWrapper.config.clear()

    c.ConfigWrapper.init_config(1)
    c.ConfigWrapper.init_config(1)
    # print(c.ConfigWrapper.config)
    assert id(c.ConfigWrapper.config) == id(
        c.ConfigWrapper.config) and len(c.ConfigWrapper.config) > 0
    c.ConfigWrapper.config.clear()

    conf5 = c.ConfigWrapper.init_config('ourunited.org')
    conf6 = c.ConfigWrapper.init_config('ourunited.org')
    # print(c.ConfigWrapper.config)
    assert id(c.ConfigWrapper.config) == id(
        c.ConfigWrapper.config) and len(c.ConfigWrapper.config) > 0
    c.ConfigWrapper.config.clear()

    c.ConfigWrapper.init_config('ourunited.org_none')
    c.ConfigWrapper.init_config('ourunited.org_none')
    # print(c.ConfigWrapper.config)
    assert id(c.ConfigWrapper.config) == id(c.ConfigWrapper.config) and len(
        c.ConfigWrapper.config) == 0


def test_get_value_in_cache():
    c.ConfigWrapper.init_config()
    assert c.ConfigWrapper.get_value_in_cache('tester') == 'jack'
    assert c.ConfigWrapper.get_value_in_cache(
        'testerlala') == 'not found'

    with pytest.raises(TypeError) as excinfo:
        c.ConfigWrapper.get_value_in_cache()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        c.ConfigWrapper.get_value_in_cache(1)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        c.ConfigWrapper.get_value_in_cache(())
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        c.ConfigWrapper.get_value_in_cache([])
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        c.ConfigWrapper.get_value_in_cache({})
    assert excinfo.type.__name__ == 'TypeError'

    c.ConfigWrapper.config.clear()


def test_get_value_from_config_file():
    c.ConfigWrapper.init_config('ourunited.org')
    ret = c.ConfigWrapper.get_value_from_config_file('tester')
    assert ret == 'jack'
    # conf.config.clear()

    with pytest.raises(KeyError) as excinfo:
        c.ConfigWrapper.get_value_from_config_file('tester1')
    assert excinfo.type.__name__ == 'KeyError'

    with pytest.raises(TypeError) as excinfo:
        c.ConfigWrapper.get_value_from_config_file()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(KeyError) as excinfo:
        c.ConfigWrapper.get_value_from_config_file(
            'tester', 'ourunited.org1')
    assert excinfo.type.__name__ == 'KeyError'

    with pytest.raises(KeyError) as excinfo:
        c.ConfigWrapper.get_value_from_config_file(
            'tester1', 'ourunited.org')
    assert excinfo.type.__name__ == 'KeyError'

    c.ConfigWrapper.config.clear()


def test_reload_config():
    c.ConfigWrapper.init_config()
    # print(conf.config)
    c.ConfigWrapper.reload_config('ourunited.org')
    assert c.ConfigWrapper.config.get('tester') == 'jack1'

    c.ConfigWrapper.reload_config()
    assert c.ConfigWrapper.config.get('tester') == 'jack'

    c.ConfigWrapper.reload_config(1)
    assert c.ConfigWrapper.config.get('tester') == 'jack'
