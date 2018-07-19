#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' Pywinauto Wrapper '''

import time
import tpsautomation.model.pyautoguiwrapper as pw
from pywinauto import application, mouse

class PywinautoWrapper(object):

    SLEEP_TIME = 2
    TITLE_BAR = 'TitleBar'
    LOGIN_DESKTOP = 'Login Desktop'

    def __init__(self, type = None):
        # note : same application in each PywinautoWrapper
        # note : same application in each PywinautoWrapper
        # Application()
        # default is win32
        if not 'uia' == type:
            self._app = application.Application() 
        else:
            self._app = application.Application(backend="uia")
        self._mouse = mouse

    def start(self, tool_name):
        self._app.start(tool_name)

    def connect(self, title_or_path, type = None):
        """
        defuale conncect by path, or by title
        _app.connect_(path = r"c:\windows\system32\notepad.exe")
        _app.connect_(process = 2341)
        _app.connect_(handle = 0x010f0c)
        """
        if type is not None:
            self._app.connect(title = title_or_path)
        else:
            self._app.connect(path = title_or_path)

    def close_tps(self):
        self._app[PywinautoWrapper.LOGIN_DESKTOP].close()

    def close_tps_by_button(self):
        self._app[PywinautoWrapper.LOGIN_DESKTOP][PywinautoWrapper.TITLE_BAR].Button.click()

    ''' there is no need to click confirm window '''
    def kill_application(self):
        self._app.kill()

    def max_window(self, window_name):
        self._app[window_name].maximize()

    def menu_click(self, window_name, menulist):
        self._app[window_name].menu_select(menulist)

    def input(self, window_name, controller, content):
        self._app[window_name][controller].TypeKeys(content)

    def click(self, window_name, controller):
        """
        support regex
        _app[u'关于“记事本”'][u'确定'].Click()
        _app.window_(title_re = u'关于“记事本”').window_(title_re = u'确定').Click()
        """
        self._app[window_name][controller].Click()

    def double_click(self, window_name, controller, x=0, y=0):
        self._app[window_name][controller].DoubleClick(
            button="left", pressed="",  coords=(x, y))

    def right_click(self, window_name, controller, order):
        self._app[window_name][controller].RightClick()
        time.sleep(2)
        for down in range(order):
            time.sleep(2)
            self._app[window_name].type_keys('{DOWN}')

        self._app[window_name].type_keys('{ENTER}')