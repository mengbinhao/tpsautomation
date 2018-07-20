#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' const paramter for project '''

import datetime

class ConstValue():

    CONFIG_DEFAULT_SECTION = 'DEFAULT'
    DICT_NON_EXIST_VALUE = 'not found'
    
    STR_FOR_TYPE = 'str'
    INT_FOR_TYPE = 888
    BOOLEAN_FOR_TYPE = True
    EMPTY_STRING = ''

    DEFAULT_CONFIG_FILE_PATH = r'C:\Users\T5810\Desktop\tpsautomation\logger.conf'
    # point to virtualenv
    DEFAULT_PYTHON_EXE = r'C:\Users\T5810\Desktop\python_envs\env36\Scripts\python.exe'

    DATETIME_DATETIME_FOR_TYPE = datetime.datetime

    ZERO_INT = 0
    SIXTY_INT = 60
    EXIT_STATUS_CODE = -1

    CUT_OFF_RULE = '__'

    SCREENSHOT_SUFFIX = '.png'
    HTML_SUFFIX = '.html'
    PYTHON_SUFFIX = '.py'

    CASE_PASS_RESULT = 'pass'
    CASE_FAIL_RESULT = 'fail'
    CASE_TYPE_TOUDAO = 'toudao'
    CASE_TYPE_TIDAO = 'tidao'
    CASE_TYPE_PROWESS = 'prowess'

    HTML_ACTIVE_CLASS = 'active'
    HTML_PASS_CLASS = 'success'
    HTML_FAIL_CLASS = 'danger'
    HTML_REASON_SUCCESS = 'success'

    UTF_8_STR = 'utf-8'