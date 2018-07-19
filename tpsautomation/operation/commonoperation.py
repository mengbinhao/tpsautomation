#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper method for operating common function of TPS'''

import time
import logging
import sys
import tpsautomation.common.tpslogging as tl
import tpsautomation.model.pywinautowrapper as pw
import tpsautomation.model.pyautoguiwrapper as pg
import tpsautomation.common.constValue as cv


class CommonOperation(object):

    def __init__(self):
        self._pw = pw.PywinautoWrapper('uia')
        self._pg = pg.PyautoGUIWrapper()

    ''' do not handle exception '''

    def kill_tps_application_if_needed(self, tpsexepath):
        try:
            self._pw.connect(tpsexepath)
            self._pw.kill_application()
        except Exception as ex:
            logging.debug('close_if_exists fail')
            pass
        self.sleep()

    def start_tps(self, tpsexepath):
        try:
            self._pw.start(tpsexepath)
        except Exception as ex:
            logging.debug('can not start tps')
            raise
        else:
            self.sleep(30)

    def connect_tps(self, tpsexepath):
        try:
            self._pw.connect(tpsexepath)
        except Exception as ex:
            logging.debug('can not connect tps')
            raise
        self.sleep()

    def login_tps(self, tpsexepath, user_name, password):
        try:
            self._pg.move_mouse_to_center()
            self._pg.click_mouse()
            self._pg.type_write(user_name)
            # notice input method editor
            self._pg.press_special_keyboard('tab')
            self._pg.type_write(password)
            self._pg.press_special_keyboard('enter')
        except Exception as ex:
            logging.debug('login_tps fail')
            raise

    def logout_tps(self, tpsexepath):
        try:
            self.connect_tps(tpsexepath)
            self._pg.move_mouse(120, 961)
            self._pg.click_mouse()
        except Exception as ex:
            logging.debug('logout_tps fail')
            raise

    def close_tps_by_x(self):
        try:
            self._pg.move_mouse(1280, 329)
            self._pg.click_mouse()
        except Exception as ex:
            trace = sys.exc_info()[2]
            tl.LoggingWrapper.record_logger(__name__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
            self._pg.capture_screenshot()
            raise

    def sleep(self, second=3):
        if not isinstance(second, type(cv.ConstValue.INT_FOR_TYPE)) or second < cv.ConstValue.ZERO_INT or second > cv.ConstValue.SIXTY_INT:
            second = 3
        time.sleep(second)
