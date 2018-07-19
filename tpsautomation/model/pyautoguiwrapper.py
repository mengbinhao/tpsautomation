#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' PyAutoGUI Wrapper '''

#import logging
import sys
import os
import re
import logging.config
import pyautogui
import tpsautomation.common.tpslogging as tl
import tpsautomation.common.constValue as cv
import tpsautomation.common.tpsconfig as tc
import tpsautomation.utils.typeutils as tu

class PyautoGUIWrapper(object):

    __DEFAULT_SCREEN_WIDTH = 1920
    __DEFAULT_SCREEN_HEIGHT = 1080
    __DEFAULT_PAUSE_TIME = 3
    __DEFAULT_FAIL_SAFE = True

    # logger = c.LoggingWrapper.get_logger(__name__)
    # todo:can not get config from LoggingWrapper
    # todo:can not get config from LoggingWrapper
    logging.config.fileConfig(cv.ConstValue.DEFAULT_CONFIG_FILE_PATH)

    def __init__(self):
        # note : same pyautogui in each PyautoGUIWrapper
        # note : same pyautogui in each PyautoGUIWrapper
        self._pyautogui = pyautogui
        self.__init_config()
    
    def __init_config(self, wait_time = None, fail_safe = None):
        if wait_time is None:
            self._pyautogui.PAUSE = PyautoGUIWrapper.__DEFAULT_PAUSE_TIME
        if fail_safe is None:
            self._pyautogui.FAILSAFE = PyautoGUIWrapper.__DEFAULT_FAIL_SAFE

    # due to same pyautogui, only use once
    def safe_exit(self):
        self._pyautogui.moveTo(0,0)

    def get_current_screen_resolution(self):
        return self._pyautogui.size()

    def get_current_mouse_position(self):
        return self._pyautogui.position()

    #note : max width = _default_screen_width - 1
    #       max height = _default_screen_height - 1
    def is_mouse_position_in_screen(self):
        x, y = self.get_current_mouse_position()
        return self._pyautogui.onScreen(x, y)

    def check_screen_resolution(self):
        screen_width, screen_height = self._pyautogui.size()
        try:
            if ((screen_width != PyautoGUIWrapper.__DEFAULT_SCREEN_WIDTH) or (screen_height != PyautoGUIWrapper.__DEFAULT_SCREEN_HEIGHT)):
                raise
        except:
            trace = sys.exc_info()[2]
            logging.error('file: %s function: %s lineno: %d (screen_width: %d, screen_height: %d)',
                              __name__, trace.tb_frame.f_code.co_name, trace.tb_lineno, screen_width, screen_height)
            # todo -- exit subprocess
            #os._exit(-1)
        else:
            logging.debug('file: %s -- message: %s',
                              __name__, 'checkScreenResolution successful')

    def move_mouse(self, x, y, duration=2):
        try:
            if ((type(x) != int) or (type(y) != int) or (type(duration) != int)):
                raise
        except:
            trace = sys.exc_info()[2]
            logging.error('file: %s function: %s lineno: %d (x: %d, y: %d, duration: %s)',
                              __name__, trace.tb_frame.f_code.co_name, trace.tb_lineno, x, y, duration)
            # todo -- exit subprocess
            #os._exit(-1)
        else:
            logging.debug('file: %s -- message: %s', __name__, 'move_mouse successful')
            self._pyautogui.moveTo(x, y, duration)

    def move_mouse_rel(self, x, y, duration=2):
        try:
            if ((type(x) != int) or (type(y) != int) or (type(duration) != int)):
                raise
        except:
            trace = sys.exc_info()[2]
            logging.error('file: %s function: %s lineno: %d (x: %d, y: %d, duration: %s)',
                              __name__, trace.tb_frame.f_code.co_name, trace.tb_lineno, x, y, duration)
            # todo -- exit subprocess
            #os._exit(-1)
        else:
            logging.debug('file: %s -- message: %s', __name__, 'move_mouse_rel successful')
            self._pyautogui.moveRel(x, y, duration)

    def click_mouse(self):
        self._pyautogui.click()

    def move_mouse_to_center(self):
        width, height = self.get_current_screen_resolution()
        self.move_mouse(width // 2, height // 2)

    def dbclick_mouse(self):
        self._pyautogui.doubleClick()

    def drag_mouse(x, y, duration=0.25):
        try:
            if ((type(x) != int) or (type(y) != int) or (type(duration) != int)):
                raise
        except:
            trace = sys.exc_info()[2]
            logging.error('file: %s function: %s lineno: %d (x: %d, y: %d, duration: %s)',
                              __name__, trace.tb_frame.f_code.co_name, trace.tb_lineno, x, y, duration)
            # todo -- exit subprocess
            #os._exit(-1)
        else:
            logging.debug('file: %s -- message: %s',__name__, 'drag_mouse successful')
            self._pyautogui.dragTo(x, y, duration)
        
    def drag_mouse_rel(self):
        pass

    def scorll_mouse(self):
        pass

    def draw_rect(self):
        distance = 200
        while distance > 0:
            pyautogui.dragRel(distance, 0, duration=0.5)
            distance -= 5
            pyautogui.dragRel(0, distance, duration=0.5)
            pyautogui.dragRel(-distance, 0, duration=0.5)
            distance -= 5
            pyautogui.dragRel(0, -distance, duration=0.5)
    
    def type_write(self, str, interval = 1):
        self._pyautogui.typewrite(str, interval)
        #self._pyautogui.press('enter')

    def press_special_keyboard(self, Key):
        self._pyautogui.press(Key)

    def hot_key(self, key1, key2):
        self._pyautogui.hotkey(key1, key2)

    """ just pass name """
    def capture_screenshot(self, name):
        if name is None or not tu.TypeUtils.is_str(name) or '' == name.strip() or re.search('^(.+)(\\\\|/)$', name)  is not None:
            raise ValueError
        self._pyautogui.screenshot(tc.configWrapper.config['screenshotfolder'] + name + cv.ConstValue.SCREENSHOT_SUFFIX)