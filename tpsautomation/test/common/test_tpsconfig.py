import pytest
import tpsautomation.common.tpsconfig as c

# path = r'C:\Users\T5810\Desktop\tpsautomation\conf.ini'
# file_name = 'configure.ini'

""" first to run for init config """


def test_init_config():
    c.configWrapper.init_config()
    c.configWrapper.init_config()
    # print(c.configWrapper.config)
    assert id(c.configWrapper.config) == id(c.configWrapper.config) and len(c.configWrapper.config) > 0
    c.configWrapper.config.clear()

    c.configWrapper.init_config(1)
    c.configWrapper.init_config(1)
    # print(c.configWrapper.config)
    assert id(c.configWrapper.config) == id(c.configWrapper.config) and len(c.configWrapper.config) > 0
    c.configWrapper.config.clear()

    conf5 = c.configWrapper.init_config('ourunited.org')
    conf6 = c.configWrapper.init_config('ourunited.org')
    # print(c.configWrapper.config)
    assert id(c.configWrapper.config) == id(c.configWrapper.config) and len(c.configWrapper.config) > 0
    c.configWrapper.config.clear()

    c.configWrapper.init_config('ourunited.org_none')
    c.configWrapper.init_config('ourunited.org_none')
    # print(c.configWrapper.config)
    assert id(c.configWrapper.config) == id(c.configWrapper.config) and len(c.configWrapper.config) == 0


def test_get_special_value_in_cache():
    c.configWrapper.init_config()
    assert c.configWrapper.get_special_value_in_cache('tester') == 'djack'
    assert c.configWrapper.get_special_value_in_cache('testerlala') == 'not found'

    with pytest.raises(TypeError) as excinfo:
        c.configWrapper.get_special_value_in_cache()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        c.configWrapper.get_special_value_in_cache(1)
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        c.configWrapper.get_special_value_in_cache(())
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        c.configWrapper.get_special_value_in_cache([])
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        c.configWrapper.get_special_value_in_cache({})
    assert excinfo.type.__name__ == 'TypeError'

    c.configWrapper.config.clear()


def test_get_special_value_from_config_file():
    c.configWrapper.init_config('jack.com')
    ret = c.configWrapper.get_special_value_from_config_file('tester')
    assert ret == 'djack'
    # conf.config.clear()

    with pytest.raises(KeyError) as excinfo:
        c.configWrapper.get_special_value_from_config_file('tester1')
    assert excinfo.type.__name__ == 'KeyError'

    with pytest.raises(TypeError) as excinfo:
        c.configWrapper.get_special_value_from_config_file()
    assert excinfo.type.__name__ == 'TypeError'

    ret2 = c.configWrapper.get_special_value_from_config_file('tester', 'ourunited.org')
    assert ret2 == 'ojack1'

    with pytest.raises(KeyError) as excinfo:
        c.configWrapper.get_special_value_from_config_file('tester','ourunited.org1')
    assert excinfo.type.__name__ == 'KeyError'

    with pytest.raises(KeyError) as excinfo:
        c.configWrapper.get_special_value_from_config_file('tester1','ourunited.org')
    assert excinfo.type.__name__ == 'KeyError'

    c.configWrapper.config.clear()


def test_reload_config():
    c.configWrapper.init_config()
    # print(conf.config)
    c.configWrapper.reload_config('ourunited.org')
    assert c.configWrapper.config.get('tester') == 'ojack1'

    c.configWrapper.reload_config()
    assert c.configWrapper.config.get('tester') == 'djack'

    c.configWrapper.reload_config(1)
    assert c.configWrapper.config.get('tester') == 'djack'