import pytest
import datetime
import tpsautomation.report.htmlreport as hr

def test_get_date_and_time_as_datetime():
    result_list = [{'id': 1, 'name': 'case01', 'runresult': 'pass', 'runtime': datetime.datetime.now(), 'runduration': '10分', 'htmlclass': 'success', 'reason': '成功'},
                  {'id': 2, 'name': 'case02', 'runresult': 'pass', 'runtime': datetime.datetime.now(), 'runduration': '10分', 'htmlclass': 'success', 'reason': '成功'},
                  {'id': 3, 'name': 'case03', 'runresult': 'fail', 'runtime': datetime.datetime.now(), 'runduration': '10分', 'htmlclass': 'danger', 'reason': '失败'},
                  {'id': 4, 'name': 'case04', 'runresult': 'fail', 'runtime': datetime.datetime.now(), 'runduration': '10分', 'htmlclass': 'danger', 'reason': '失败'},
                  {'id': 5, 'name': 'case05', 'runresult': 'fail', 'runtime': datetime.datetime.now(), 'runduration': '10分', 'htmlclass': 'danger', 'reason': '失败'}
                   ]
    title = '自动化测试报告'
    path = r'C:\Users\T5810\Desktop\tpsautomation\report'
    casepath = r'C:\Users\T5810\Desktop\tpsautomation\tpsautomation\testcases\beihang\toudao'
    with pytest.raises(TypeError) as excinfo:
        hr.HTMLReport.generete_html_report()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(TypeError) as excinfo:
        hr.HTMLReport.generete_html_report(result_list)
    assert excinfo.type.__name__ == 'TypeError'

    #result_list = []
    hr.HTMLReport.generete_html_report(result_list, title, path, casepath)