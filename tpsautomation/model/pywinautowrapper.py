#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' Pywinauto Wrapper '''

import time
from pywinauto import application, mouse


class PywinautoWrapper():
    ''' Pywinauto Wrapper '''
    SLEEP_TIME = 2
    TITLE_BAR = 'TitleBar'
    LOGIN_DESKTOP = 'Login Desktop'

    def __init__(self, type_val=None):
        # note : same application in each PywinautoWrapper
        # note : same application in each PywinautoWrapper
        # Application()
        # default is win32
        if not type_val == 'uia':
            self._app = application.Application()
        else:
            self._app = application.Application(backend="uia")
        self._mouse = mouse

    def start(self, tool_name):
        ''' start '''
        self._app.start(tool_name)

    def connect(self, title_or_path, type_val=None):
        ''' defuale conncect by path, or by title
            _app.connect_(path = r'c:\windows\system32\notepad.exe')
            _app.connect_(process = 2341)
            _app.connect_(handle = 0x010f0c)
        '''
        if type_val is not None:
            self._app.connect(title=title_or_path)
        else:
            self._app.connect(path=title_or_path)

    def close_tps(self):
        ''' close_tps '''
        self._app[PywinautoWrapper.LOGIN_DESKTOP].close()

    def close_tps_by_button(self):
        ''' close_tps_by_button '''
        self._app[PywinautoWrapper.LOGIN_DESKTOP][PywinautoWrapper.TITLE_BAR].Button.click()

    def kill_application(self):
        ''' kill_application, there is no need to click confirm window '''
        self._app.kill()

    def max_window(self, window_name):
        ''' max_window '''
        self._app[window_name].maximize()

    def menu_click(self, window_name, menulist):
        ''' menu_click '''
        self._app[window_name].menu_select(menulist)

    def input(self, window_name, controller, content):
        ''' input '''
        self._app[window_name][controller].TypeKeys(content)

    def click(self, window_name, controller):
        """
        support regex
        _app[u'关于“记事本”'][u'确定'].Click()
        _app.window_(title_re = u'关于“记事本”').window_(title_re = u'确定').Click()
        """
        self._app[window_name][controller].Click()

    def double_click(self, window_name, controller, x_px=0, y_px=0):
        ''' double_click '''
        self._app[window_name][controller].DoubleClick(
            button="left", pressed="", coords=(x_px, y_px))

    def right_click(self, window_name, controller, order):
        ''' right_click '''
        self._app[window_name][controller].RightClick()
        time.sleep(2)
        for down in range(order):
            time.sleep(2)
            self._app[window_name].type_keys('{DOWN}')
        self._app[window_name].type_keys('{ENTER}')
