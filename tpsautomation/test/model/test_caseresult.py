import pytest
import tpsautomation.model.caseresult as c
import tpsautomation.utils.dateandtimeutils as datu


def test_instantiation():
    c1 = c.CaseResult(1, 'case01', 'pass', datu.DateAndTimeUtils.get_today_as_str(), 333, 'success', 'laaaaaaaaa')
    #print(c1)

    c2 = c.CaseResult(2, 'case02', 'fail', datu.DateAndTimeUtils.get_today_as_str(), 333, 'danger')
    #print(c2)
    
    c3 = c.CaseResult(3, 'case03', 'fail', datu.DateAndTimeUtils.get_today_as_str(), 333, 'danger')
    c3.name = "ddddd"
    #print(c3)

    with pytest.raises(TypeError) as excinfo:
        c.CaseResult(1, 'case01', 'pass')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        c.CaseResult(1, 'case01', 111, datu.DateAndTimeUtils.get_today_as_str(), 333, 'success', 'laaaaaaaaa')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        c.CaseResult(1, 'case01', 'pass11111', datu.DateAndTimeUtils.get_today_as_str(), 333, 'success', 'laaaaaaaaa')
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        c.CaseResult(1, 'case01', 'pass', 1111111, 333, 'success', 'laaaaaaaaa')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        c.CaseResult(1, 'case01', 'pass', 'fwfewfwfwfw', 333, 'success', 'laaaaaaaaa')
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        c.CaseResult(1, 'case01', 'pass', datu.DateAndTimeUtils.get_today_as_str(), 'wdwdwd2', 'success', 'laaaaaaaaa')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        c.CaseResult(1, 'case01', 'pass', datu.DateAndTimeUtils.get_today_as_str(), -1, 'success', 'laaaaaaaaa')
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        c.CaseResult(1, 'case01', 'pass', datu.DateAndTimeUtils.get_today_as_str(), 333, 1, 'laaaaaaaaa')
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        c.CaseResult(1, 'case01', 'pass', datu.DateAndTimeUtils.get_today_as_str(), 333, 'success111', 'laaaaaaaaa')
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(TypeError) as excinfo:
        c.CaseResult(1, 'case01', 'pass', datu.DateAndTimeUtils.get_today_as_str(), 333, 'success', 11)
    assert excinfo.type.__name__ == 'TypeError'
