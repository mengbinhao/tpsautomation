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


def init():
    tc.configWrapper.init_config()
    print('Initialize config Done')
    logger_path_name = tc.configWrapper.config.get(
        'logger_path_name', cv.ConstValue.DICT_NON_EXIST_VALUE)
    if (logger_path_name == cv.ConstValue.DICT_NON_EXIST_VALUE):
        raise ValueError
    logging.config.fileConfig(logger_path_name)
    print('Initialize logging Done')


def get_tps_env(dict):
    tpsexepath = dict.get('tpsexepath', cv.ConstValue.DICT_NON_EXIST_VALUE)
    tpsroot = dict.get('tpsroot', cv.ConstValue.DICT_NON_EXIST_VALUE)
    if tpsexepath == cv.ConstValue.DICT_NON_EXIST_VALUE or tpsroot == cv.ConstValue.DICT_NON_EXIST_VALUE:
        raise ValueError
    return tpsexepath, tpsroot


def get_case_type(args, dict):
    try:
        cases_bh_toudao = 'cases_bh_toudao'
        if args[1]:
            if args[1].lower() == cv.ConstValue.CASE_TYPE_TOUDAO:
                return dict.get(cases_bh_toudao, cv.ConstValue.CASE_TYPE_TOUDAO)
            elif args[1].lower() == cv.ConstValue.CASE_TYPE_TIDAO:
                return dict.get('cases_bh_tidao', cv.ConstValue.CASE_TYPE_TIDAO)
            elif args[1].lower() == cv.ConstValue.CASE_TYPE_PROWESS:
                return dict.get('cases_prowess', cv.ConstValue.CASE_TYPE_PROWESS)
    except Exception as ex:
       return dict.get(cases_bh_toudao, cv.ConstValue.CASE_TYPE_TOUDAO)


if __name__ == '__main__':
    print('Automation Start')
    result_list = []
    try:
        1/0
        init()
        tpsexepath, tpsroot = get_tps_env(tc.configWrapper.config)

        #kill tps if needed
        #co_obj = co.CommonOperation()
        #co_obj.kill_tps_application_if_needed(tpsexepath)

        cases_root = get_case_type(sys.argv, tc.configWrapper.config)
        #get cases list
        case_list = fu.FileUtils.get_case_list(cases_root)
        #case like 01_xxx,  02_yyy
        case_list.sort()
        logging.debug('excute %d cases------%s', len(case_list), case_list)
        count = 1
        for case in case_list:
            run_result = ''
            html_class = cv.ConstValue.HTML_ACTIVE_CLASS
            run_reason = ''
            start_time = time.time()
            x = subprocess.Popen(
                [cv.ConstValue.DEFAULT_PYTHON_EXE, case, tpsexepath],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                cwd=tpsroot)
            #x.wait()
            output, err_output = x.communicate()
            end_time = time.time()
            #retcode = x.poll()
            if (x.returncode == 0):
                run_result = cv.ConstValue.CASE_PASS_RESULT
                html_class = cv.ConstValue.HTML_PASS_CLASS
                run_reason = cv.ConstValue.HTML_REASON_SUCCESS
            else:
                run_result = cv.ConstValue.CASE_FAIL_RESULT
                html_class = cv.ConstValue.HTML_FAIL_CLASS
                run_reason = output.decode(cv.ConstValue.UTF_8_STR)
            case = case.replace(cases_root, '')
            case_result = cr.CaseResult(
                count, case, run_result,
                datu.DateAndTimeUtils.get_today_as_str(),
                math.ceil(end_time - start_time), html_class, run_reason)
            result_list.append(du.DictUtils.class_to_dict(case_result))
            count += 1
    #can not catch any subprocess exception
    except Exception as ex:
        trace = sys.exc_info()[2]
        logging.error('file: %s function: %s lineno: %d args: %s)', __name__,
                      trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
    finally:
        html_title = tc.configWrapper.config.get(
            'html_title', cv.ConstValue.DICT_NON_EXIST_VALUE)
        html_report_path = tc.configWrapper.config.get(
            'html_report_path', cv.ConstValue.DICT_NON_EXIST_VALUE)
        hr.HTMLReport.generete_html_report(result_list, html_title,
                                           html_report_path, cases_root)
        print('Automation Finish')
