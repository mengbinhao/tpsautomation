#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' Case_Result model '''

import re
import sys
from tpsautomation.model.basic import Basic
import tpsautomation.common.constvalue as cv
import tpsautomation.utils.dateandtimeutils as datu


class CaseResult(Basic):

    """ use set_xxx and get_xxx so can check value while initializing"""

    def __init__(self, case_result_id, name, run_result, run_time, run_duration, html_class, reason=''):
        #Basic.__init__(self, case_result_id, name)
        super(CaseResult, self).__init__(case_result_id, name)
        self.set_run_result(run_result)
        self.set_run_time(run_time)
        self.set_run_duration(run_duration)
        self.set_html_class(html_class)
        self.set_reason(reason)

    def __str__(self):
        return 'id: %d - name: %s - run_result: %s - run_time: %s - run_duration: %s - html_class: %s - reason: %s' \
            % (self._id, self._name, self._run_result, self._run_time, self._run_duration, self._html_class, self._reason)

    def get_run_result(self):
        ''' get_run_result '''
        return self._run_result

    def set_run_result(self, value):
        ''' set_run_result '''
        if not isinstance(value, type(cv.ConstValue.STR_FOR_TYPE)):
            raise TypeError
        value = value.strip()
        if value not in (cv.ConstValue.CASE_FAIL_RESULT, cv.ConstValue.CASE_PASS_RESULT):
            raise ValueError
        self._run_result = value

    def get_run_time(self):
        ''' get_run_time '''
        return self._run_time

    def set_run_time(self, value):
        ''' set_run_time '''
        if not isinstance(value, type(cv.ConstValue.STR_FOR_TYPE)):
            raise TypeError
        if not re.search(r'^\d{4}-\d{2}-\d{2}$', value.strip()):
            raise ValueError
        self._run_time = value

    def get_run_duration(self):
        ''' get_run_duration '''
        return self._run_duration

    def set_run_duration(self, value):
        ''' set_run_duration '''
        if not isinstance(value, type(cv.ConstValue.INT_FOR_TYPE)):
            raise TypeError
        if value < Basic.INT_ZERO or value > sys.maxsize:
            raise ValueError
        self._run_duration = datu.DateAndTimeUtils.convert_seconds_to_display_time(
            value)

    def get_html_class(self):
        ''' get_html_class '''
        return self._html_class

    def set_html_class(self, value):
        ''' get_html_class '''
        if not isinstance(value, type(cv.ConstValue.STR_FOR_TYPE)):
            raise TypeError
        value = value.strip()
        if value not in (cv.ConstValue.HTML_ACTIVE_CLASS, cv.ConstValue.HTML_PASS_CLASS, cv.ConstValue.HTML_FAIL_CLASS):
            raise ValueError
        self._html_class = value

    def get_reason(self):
        ''' get_reason '''
        return self._reason

    def set_reason(self, value):
        ''' set_reason '''
        if not isinstance(value, type(cv.ConstValue.STR_FOR_TYPE)):
            raise TypeError
        self._reason = value.strip()
