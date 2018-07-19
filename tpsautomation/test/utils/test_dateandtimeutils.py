import pytest
import datetime
import tpsautomation.utils.dateandtimeutils as du
import tpsautomation.common.constValue as cv


def test_get_today_to_str():
    assert len(du.DateAndTimeUtils.get_today_as_str()) == 10
    assert len(du.DateAndTimeUtils.get_today_as_str('wfwfw')) != 10

def test_get_today_as_str_from_timestamp():
    assert len(du.DateAndTimeUtils.get_today_as_str_from_timestamp()) == 10
    assert len(du.DateAndTimeUtils.get_today_as_str_from_timestamp('wfwfw')) != 10

def test_get_date_and_time_to_str():
    assert len(du.DateAndTimeUtils.get_date_and_time_as_str()) == 19
    assert len(du.DateAndTimeUtils.get_date_and_time_as_str('wfwfw')) != 19

def test_get_date_and_time_as_datetime():
    str = '2018-01-01 16:26:22'
    assert isinstance(du.DateAndTimeUtils.get_date_and_time_as_datetime(str), cv.ConstValue.DATETIME_DATETIME_FOR_TYPE)

    with pytest.raises(ValueError) as excinfo:
        du.DateAndTimeUtils.get_date_and_time_as_datetime(str, 'wfwfw')
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        du.DateAndTimeUtils.get_date_and_time_as_datetime(str, {})
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        du.DateAndTimeUtils.get_date_and_time_as_datetime()
    assert excinfo.type.__name__ == 'TypeError'

def test_get_delta_between_two_days():
    str1 = '2012-03-05'
    str2 = '2012-03-02'
    assert du.DateAndTimeUtils.get_delta_between_two_days(str1, str2) == 3

    with pytest.raises(TypeError) as excinfo:
        du.DateAndTimeUtils.get_delta_between_two_days()
    assert excinfo.type.__name__ == 'TypeError'
  
    with pytest.raises(TypeError) as excinfo:
        du.DateAndTimeUtils.get_delta_between_two_days(str1, {})
    assert excinfo.type.__name__ == 'TypeError'


def test_get_delta_days_from_now():
    pass
    #assert du.DateAndTimeUtils.get_delta_days_from_now(3) == datetime.datetime.now().strftime(r'%Y-%m-%d')

def test_convert_seconds_to_display_time():
    with pytest.raises(TypeError) as excinfo:
        du.DateAndTimeUtils.convert_seconds_to_display_time()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        du.DateAndTimeUtils.convert_seconds_to_display_time('222')
    assert excinfo.type.__name__ == 'TypeError'
    
    with pytest.raises(ValueError) as excinfo:
        du.DateAndTimeUtils.convert_seconds_to_display_time(-1)
    assert excinfo.type.__name__ == 'ValueError'

    assert du.DateAndTimeUtils.convert_seconds_to_display_time(3661) == '1 hours, 1 min, 1 sec'
    assert du.DateAndTimeUtils.convert_seconds_to_display_time(90061) == '1 days, 1 hours, 1 min, 1 sec'