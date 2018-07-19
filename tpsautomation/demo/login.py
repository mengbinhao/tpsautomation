#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' first demo '''

import time
import os
import random
import sys
import logging
import tpsautomation.model.pywinautowrapper as pw
import tpsautomation.model.pyautoguiwrapper as pg
import tpsautomation.common.tpsconfig as c
import tpsautomation.common.constValue as cv
import tpsautomation.utils.dictutils as du
import tpsautomation.utils.dateandtimeutils as dtt

ran_num = str(random.randint(100,10000))
LOGIN_TITLE = 'Login Desktop'
MAIN_UI = 'IndelPlanV2.0 CurrentUser: our(Technician)'
USER_NAME = 'our'
PASSWORD = '123'
CASE_NAME = 'jack_' + ran_num
CASE_ID = 'id_' + ran_num
NEW_USER_NAME = 'ZZZ'
NEW_USER_PASSWORD = '123'

def get_locations(dict):
    tpsexepath = du.DictUtils.get_specific_word_value(dict, 'tpsexepath')
    tpsroot = du.DictUtils.get_specific_word_value(dict, 'tpsroot')
    projectroot = du.DictUtils.get_specific_word_value(dict, 'projectroot')
    if tpsexepath == cv.ConstValue.DICT_NON_EXIST_VALUE or tpsroot == cv.ConstValue.DICT_NON_EXIST_VALUE or projectroot == cv.ConstValue.DICT_NON_EXIST_VALUE:
        raise ValueError
    return tpsexepath,tpsroot,projectroot

def login(pg):
    pg.move_mouse_to_center()
    pg.click_mouse()
    pg.type_write(USER_NAME)
    # notice input method editor
    pg.press_special_keyboard('tab')
    pg.type_write(PASSWORD)
    pg.press_special_keyboard('enter')

def add_new_user(pg):
    pg.move_mouse(125, 803)
    pg.click_mouse()
    pg.move_mouse(1111, 1065)
    pg.click_mouse()
    pg.type_write(NEW_USER_NAME)
    pg.press_special_keyboard('tab')
    pg.type_write(NEW_USER_PASSWORD)
    pg.press_special_keyboard('tab')
    pg.type_write(NEW_USER_PASSWORD)
    pg.move_mouse(1505, 819)
    pg.click_mouse()
    pg.move_mouse(1481, 943)
    pg.click_mouse()
    pg.press_special_keyboard('enter')
    pg.move_mouse(1781, 1068)
    pg.click_mouse()


def delete_new_user(pg):
    pg.move_mouse(125, 803)
    pg.click_mouse()
    pg.move_mouse(1326, 845)
    pg.click_mouse()
    pg.move_mouse(1352, 1070)
    pg.click_mouse()
    pg.move_mouse(1458, 843)
    pg.click_mouse()
    pg.move_mouse(1781, 1068)
    pg.click_mouse()

def close_if_exists(pw, tpsexepath):
    try:
        pw.connect(tpsexepath)
        pw.kill_application()
    except Exception as identifier:
        logging.debug('close_if_exists fail')
        pass

# need to run py under root folder of IndelPlan because IndelOanl reads sysconfig.ini
if __name__ == '__main__':

    print('Automation Start')
    c.configWrapper().init_config()
    print('Init config Done')
    pw = pw.PywinautoWrapper('uia')
    pg = pg.PyautoGUIWrapper()
    
    try:  
        tpsexepath, tpsroot, projectroot = get_locations(c.configWrapper().config)
        close_if_exists(pw, tpsexepath)
        #change dir to tpsroot
        os.chdir(tpsroot)

        pw.start(tpsexepath)
        # wait IndelPlan launches
        time.sleep(30)
        pw.connect(tpsexepath)
        #print(pw._app.windows())
        #pw._app[LOGIN_TITLE].print_control_identifiers()
        
        login(pg)
        add_new_user(pg)

        pg.move_mouse(103, 978)
        pg.click_mouse()

        pw.kill_application()
        #pw.close(tpsexepath)

        time.sleep(10)

        pw.start(tpsexepath)
        # wait IndelPlan launches
        time.sleep(30)
        pw.connect(tpsexepath)

        login(pg)
        delete_new_user(pg)

        pg.move_mouse(103, 978)
        pg.click_mouse()

        pw.kill_application()
    except Exception as ex:
        trace = sys.exc_info()[2]
        pg.capture_screenshot(dtt.DateAndTimeUtils.get_today_and_timestamp_as_str_from_timestamp())
        logging.error('file: %s exception: %s', __name__, ex.args)
        pw.kill_application()
    finally:
        close_if_exists(pw, tpsexepath)
        print("Automation FInish")
    