#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' main py '''

import subprocess
import logging
import logging.config
import time
import math
import sys
import tpsautomation.common.constValue as cv
import tpsautomation.common.tpsconfig as tc
import tpsautomation.utils.fileutils as fu
import tpsautomation.utils.dictutils as du
import tpsautomation.utils.dateandtimeutils as datu
import tpsautomation.model.caseresult as cr
import tpsautomation.operation.commonoperation as co
import tpsautomation.report.htmlreport as hr

CASE_ROOT = r'C:\Users\T5810\Desktop\tpsautomation\tpsautomation\testcases\beihang\toudao'


def init():
    tc.configWrapper.init_config()
    print('Initialize config Done')
    logger_path_name = tc.configWrapper.get_special_value_in_cache('logger_path_name')
    if (cv.ConstValue.DICT_NON_EXIST_VALUE == logger_path_name):
        raise ValueError
    logging.config.fileConfig(logger_path_name)
    print('Initialize logging Done')


def get_tps_env(dict):
    tpsexepath = tc.configWrapper.get_special_value_in_cache('tpsexepath')
    tpsroot = tc.configWrapper.get_special_value_in_cache('tpsroot')
    if tpsexepath == cv.ConstValue.DICT_NON_EXIST_VALUE or tpsroot == cv.ConstValue.DICT_NON_EXIST_VALUE:
        raise ValueError
    return tpsexepath,tpsroot

if __name__ == '__main__':
    print('Automation Start')
    result_list = []
    try:
        init()
        tpsexepath, tpsroot = get_tps_env(tc.configWrapper.config)

        #kill tps if needed
        co_obj = co.CommonOperation()
        co_obj.kill_tps_application_if_needed(tpsexepath)

        #get cases list
        case_list = fu.FileUtils.get_case_list(CASE_ROOT)
        case_list.sort()
        logging.debug('excute %d cases------%s', len(case_list), case_list)
        count = 1
        for case in case_list:
            run_result = ''
            html_class = 'active'
            run_reason = ''
            start_time = time.time()
            x = subprocess.Popen([cv.ConstValue.DEFAULT_PYTHON_EXE, case, tpsexepath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=tpsroot)
            #x.wait()
            oc = x.communicate()
            end_time = time.time()
            if (x.returncode == 0):
                run_result = cv.ConstValue.CASE_PASS_RESULT
                html_class = cv.ConstValue.HTML_PASS_CLASS
                run_reason = cv.ConstValue.HTML_REASON_NONE
            else:
                run_result = cv.ConstValue.CASE_FAIL_RESULT
                html_class = cv.ConstValue.HTML_FAIL_CLASS
                run_reason = oc[0].decode('utf-8')
            case = case.replace(CASE_ROOT, '')
            case_result = cr.CaseResult(count, case, run_result, datu.DateAndTimeUtils.get_today_as_str(), math.ceil(end_time - start_time), html_class, run_reason)
            result_list.append(du.DictUtils.class_to_dict(case_result))
            count += 1
    #any subprecess exception can not catch here
    except Exception as ex:
        trace = sys.exc_info()[2]
        logging.error('file: %s function: %s lineno: %d args: %s)',
                              __name__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
    finally:
        html_title = tc.configWrapper.get_special_value_in_cache('html_title')
        html_report_path = tc.configWrapper.get_special_value_in_cache('html_report_path')
        hr.HTMLReport.generete_html_report(
            result_list, html_title, html_report_path)
        print('Automation Finish')
