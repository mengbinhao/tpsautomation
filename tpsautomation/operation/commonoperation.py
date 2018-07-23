#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper method for operating common function of TPS '''

import time
import sys
import tpsautomation.common.tpslogging as tl
import tpsautomation.model.pywinautowrapper as pw
import tpsautomation.model.pyautoguiwrapper as pg
import tpsautomation.common.constvalue as cv


class CommonOperation(object):
    ''' wrapper method for operating common function of TPS'''

    def __init__(self):
        self._pw = pw.PywinautoWrapper('uia')
        self._pg = pg.PyautoGUIWrapper()

    def kill_tps_application_if_needed(self, tpsexepath):
        ''' kill_tps_application_if_needed, do not handle exception '''
        try:
            self._pw.connect(tpsexepath)
            self._pw.kill_application()
        except ValueError:
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'kill_tps_application_if_needed_fail'])
        else:
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'kill_tps_application_if_needed_successful'])
            self.sleep()

    def start_tps(self, tpsexepath):
        ''' start_tps '''
        try:
            self._pw.start(tpsexepath)
        except Exception as ex:
            trace = sys.exc_info()[2]
            tl.LoggingWrapper.record_error(
                __file__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
            self._pg.capture_screenshot(trace.tb_frame.f_code.co_name)
            raise
        else:
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'start_tps_successful'])
            self.sleep(30)

    def connect_tps(self, tpsexepath):
        ''' connect_tps '''
        try:
            self._pw.connect(tpsexepath)
        except Exception as ex:
            trace = sys.exc_info()[2]
            tl.LoggingWrapper.record_error(
                __file__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
            self._pg.capture_screenshot(trace.tb_frame.f_code.co_name)
            # have to raise so main process can know subprocss fail
            raise
        else:
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'connect_tps_successful'])
            self.sleep()

    def login_tps(self, user_name, password):
        ''' login_tps '''
        try:
            self._pg.move_mouse_to_center()
            self._pg.click_mouse()
            self._pg.type_write(user_name)
            # notice input method editor
            self._pg.press_special_keyboard('tab')
            self._pg.type_write(password)
            self._pg.press_special_keyboard('enter')
        except Exception as ex:
            trace = sys.exc_info()[2]
            tl.LoggingWrapper.record_error(
                __file__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
            self._pg.capture_screenshot(trace.tb_frame.f_code.co_name)
            raise
        else:
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'login_tps_successful'])

    def logout_tps(self, tpsexepath):
        ''' logout_tps '''
        try:
            self.connect_tps(tpsexepath)
            self._pg.move_mouse(120, 961)
            self._pg.click_mouse()
        except Exception as ex:
            trace = sys.exc_info()[2]
            tl.LoggingWrapper.record_error(
                __file__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
            self._pg.capture_screenshot(trace.tb_frame.f_code.co_name)
            raise
        else:
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'logout_tps_successful'])

    def close_tps_by_x(self):
        ''' close_tps_by_x '''
        try:
            self._pg.move_mouse(1280, 329)
            self._pg.click_mouse()
        except Exception as ex:
            trace = sys.exc_info()[2]
            tl.LoggingWrapper.record_error(
                __file__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
            # capture_screenshot for future use
            self._pg.capture_screenshot(trace.tb_frame.f_code.co_name)
            raise
        else:
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'close_tps_by_x_successful'])

    def sleep(self, second=3):
        ''' sleep '''
        if not isinstance(second, type(cv.ConstValue.INT_FOR_TYPE)) or second < cv.ConstValue.ZERO_INT or second > cv.ConstValue.SIXTY_INT:
            second = 3
        time.sleep(second)
