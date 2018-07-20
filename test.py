import datetime
import sys
import logging
import logging.config
import tpsautomation.report.htmlreport as hr
import tpsautomation.common.tpslogging as tg

if __name__ == '__main__':
    #print(__name__)
    #print(__file__)

    logging.config.fileConfig(r'C:\Users\T5810\Desktop\tpsautomation\logger.conf')

    #logging.debug('excute %d cases------%s', [1111, [1,2,3]])
    case_list= [1,2,3]
    #eval("logging.debug('excute %d cases------%s', len(case_list), case_list)")
    l = [1111, [1,2,3]]
    tg.LoggingWrapper.record_debug(r'excute %s cases------%s', *l)
    tg.LoggingWrapper.record_error(__file__, 'xxxx', 2, ())
    

    # result_list = [{'id': 1, 'name': 'case01', 'runresult': 'pass', 'runtime': datetime.datetime.now(), 'runduration': '10分', 'htmlclass': 'success', 'reason': '成功'},
    #               {'id': 2, 'name': 'case02', 'runresult': 'pass', 'runtime': datetime.datetime.now(), 'runduration': '10分', 'htmlclass': 'success', 'reason': '成功'},
    #               {'id': 3, 'name': 'case03', 'runresult': 'fail', 'runtime': datetime.datetime.now(), 'runduration': '10分', 'htmlclass': 'danger', 'reason': '失败'},
    #               {'id': 4, 'name': 'case04', 'runresult': 'fail', 'runtime': datetime.datetime.now(), 'runduration': '10分', 'htmlclass': 'danger', 'reason': '失败'},
    #               {'id': 5, 'name': 'case05', 'runresult': 'fail', 'runtime': datetime.datetime.now(), 'runduration': '10分', 'htmlclass': 'danger', 'reason': '失败'}
    #                ]
    # title = '自动化测试报告'
    # path = r'C:\Users\T5810\Desktop\tpsautomation\report'
    # casepath = r'C:\Users\T5810\Desktop\tpsautomation\tpsautomation\testcases\beihang\toudao'

    # #result_list = []
    # try:
    #     hr.HTMLReport.generete_html_report(result_list, title, path, casepath)
    # except Exception as ex:
    #     trace = sys.exc_info()[2]
    #     logging.error('file: %s function: %s lineno: %d args: %s)', __name__,
    #                   trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
    