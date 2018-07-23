#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' PyAutoGUI Wrapper '''

import sys
import re
import pyautogui
import tpsautomation.common.tpslogging as tl
import tpsautomation.common.constvalue as cv
import tpsautomation.common.tpsconfig as tc
import tpsautomation.utils.typeutils as tu


class PyautoGUIWrapper(object):
    ''' PyAutoGUI Wrapper '''
    __DEFAULT_SCREEN_WIDTH = 1920
    __DEFAULT_SCREEN_HEIGHT = 1080
    __DEFAULT_PAUSE_TIME = 3
    __DEFAULT_FAIL_SAFE = True

    def __init__(self):
        # note : same pyautogui in each PyautoGUIWrapper
        self._pyautogui = pyautogui
        self.__init_config()

    def __init_config(self, wait_time=None, fail_safe=None):
        if wait_time is None:
            self._pyautogui.PAUSE = PyautoGUIWrapper.__DEFAULT_PAUSE_TIME
        if fail_safe is None:
            self._pyautogui.FAILSAFE = PyautoGUIWrapper.__DEFAULT_FAIL_SAFE

    # due to same pyautogui, only use once
    def safe_exit(self):
        ''' safe_exit '''
        self._pyautogui.moveTo(0, 0)

    def get_current_screen_resolution(self):
        ''' get_current_screen_resolution '''
        return self._pyautogui.size()

    def get_current_mouse_position(self):
        ''' get_current_mouse_position '''
        return self._pyautogui.position()

    # note : max width = _default_screen_width - 1
    #       max height = _default_screen_height - 1
    def is_mouse_position_in_screen(self):
        ''' is_mouse_position_in_screen '''
        x_px, y_px = self.get_current_mouse_position()
        return self._pyautogui.onScreen(x_px, y_px)

    def check_screen_resolution(self):
        ''' check_screen_resolution '''
        screen_width, screen_height = self._pyautogui.size()
        screen_width = 11
        try:
            if ((screen_width != PyautoGUIWrapper.__DEFAULT_SCREEN_WIDTH) or (screen_height != PyautoGUIWrapper.__DEFAULT_SCREEN_HEIGHT)):
                raise ValueError
        except ValueError as ex:
            trace = sys.exc_info()[2]
            tl.LoggingWrapper.record_error(
                __file__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
            # todo -- exit subprocess
            # os._exit(-1)
        else:
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'checkScreenResolution_successful'])

    def move_mouse(self, x_px, y_px, duration=2):
        ''' move_mouse '''
        try:
            if not isinstance(x_px, type(cv.ConstValue.INT_FOR_TYPE)) or not isinstance(y_px, type(cv.ConstValue.INT_FOR_TYPE)) \
                    or not isinstance(duration, type(cv.ConstValue.INT_FOR_TYPE)):
                raise TypeError
        except TypeError as ex:
            trace = sys.exc_info()[2]
            tl.LoggingWrapper.record_error(
                __file__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
        else:
            self._pyautogui.moveTo(x_px, y_px, duration)
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'move_mouse_successful'])

    def move_mouse_rel(self, x_px, y_px, duration=2):
        ''' move_mouse_rel '''
        try:
            if not isinstance(x_px, type(cv.ConstValue.INT_FOR_TYPE)) or not isinstance(y_px, type(cv.ConstValue.INT_FOR_TYPE)) \
                    or not isinstance(duration, type(cv.ConstValue.INT_FOR_TYPE)):
                raise TypeError
        except TypeError as ex:
            trace = sys.exc_info()[2]
            tl.LoggingWrapper.record_error(
                __file__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
        else:
            self._pyautogui.moveRel(x_px, y_px, duration)
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'move_mouse_rel_successful'])

    def click_mouse(self):
        ''' click_mouse '''
        self._pyautogui.click()

    def move_mouse_to_center(self):
        ''' move_mouse_to_center '''
        width, height = self.get_current_screen_resolution()
        self.move_mouse(width // 2, height // 2)

    def dbclick_mouse(self):
        ''' dbclick_mouse '''
        self._pyautogui.doubleClick()

    def drag_mouse(self, x_px, y_px, duration=0.25):
        ''' drag_mouse '''
        try:
            if not isinstance(x_px, type(cv.ConstValue.INT_FOR_TYPE)) or not isinstance(y_px, type(cv.ConstValue.INT_FOR_TYPE)) \
                    or not isinstance(duration, type(cv.ConstValue.INT_FOR_TYPE)):
                raise TypeError
        except TypeError as ex:
            trace = sys.exc_info()[2]
            tl.LoggingWrapper.record_error(
                __file__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
        else:
            self._pyautogui.dragTo(x_px, y_px, duration)
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'drag_mouse_successful'])

    def drag_mouse_rel(self):
        ''' drag_mouse_rel '''
        pass

    def scorll_mouse(self):
        ''' scorll_mouse '''
        pass

    def draw_rect(self):
        ''' draw_rect '''
        distance = 200
        while distance > 0:
            pyautogui.dragRel(distance, 0, duration=0.5)
            distance -= 5
            pyautogui.dragRel(0, distance, duration=0.5)
            pyautogui.dragRel(-distance, 0, duration=0.5)
            distance -= 5
            pyautogui.dragRel(0, -distance, duration=0.5)

    def type_write(self, str_val, interval=1):
        ''' type_write '''
        self._pyautogui.typewrite(str_val, interval)
        # self._pyautogui.press('enter')

    def press_special_keyboard(self, key_val):
        ''' press_special_keyboard '''
        self._pyautogui.press(key_val)

    def hot_key(self, key1, key2):
        ''' hot_key '''
        self._pyautogui.hotkey(key1, key2)

    def capture_screenshot(self, name):
        ''' capture_screenshot '''
        if name is None or not tu.TypeUtils.is_str(name) or name.strip() == '' or re.search('^(.+)(\\\\|/)$', name) is not None:
            raise ValueError
        self._pyautogui.screenshot(
            tc.ConfigWrapper.config['screenshotfolder'] + name + cv.ConstValue.SCREENSHOT_SUFFIX)
