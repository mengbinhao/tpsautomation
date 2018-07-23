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
import tpsautomation.common.constvalue as cv
import tpsautomation.utils.dictutils as du
import tpsautomation.utils.dateandtimeutils as dtt

ran_num = str(random.randint(100, 10000))
LOGIN_TITLE = 'Login Desktop'
MAIN_UI = 'IndelPlanV2.0 CurrentUser: our(Technician)'
USER_NAME = 'our'
PASSWORD = '123'
CASE_NAME = 'jack_' + ran_num
CASE_ID = 'id_' + ran_num
NEW_USER_NAME = 'ZZZ'
NEW_USER_PASSWORD = '123'


def get_locations(config):
    ''' get_locations '''
    tps_exe_path = du.DictUtils.get_specific_word_value(config, 'tpsexepath')
    tps_root = du.DictUtils.get_specific_word_value(config, 'tpsroot')
    project_root = du.DictUtils.get_specific_word_value(config, 'projectroot')
    if tps_exe_path == cv.ConstValue.DICT_NON_EXIST_VALUE or tps_root == cv.ConstValue.DICT_NON_EXIST_VALUE \
            or project_root == cv.ConstValue.DICT_NON_EXIST_VALUE:
        raise ValueError
    return tps_exe_path, tps_root, project_root


def login(mypg):
    ''' login '''
    mypg.move_mouse_to_center()
    mypg.click_mouse()
    mypg.type_write(USER_NAME)
    # notice input method editor
    mypg.press_special_keyboard('tab')
    mypg.type_write(PASSWORD)
    mypg.press_special_keyboard('enter')


def add_new_user(mypg):
    ''' login '''
    mypg.move_mouse(125, 803)
    mypg.click_mouse()
    mypg.move_mouse(1111, 1065)
    mypg.click_mouse()
    mypg.type_write(NEW_USER_NAME)
    mypg.press_special_keyboard('tab')
    mypg.type_write(NEW_USER_PASSWORD)
    mypg.press_special_keyboard('tab')
    mypg.type_write(NEW_USER_PASSWORD)
    mypg.move_mouse(1505, 819)
    mypg.click_mouse()
    mypg.move_mouse(1481, 943)
    mypg.click_mouse()
    mypg.press_special_keyboard('enter')
    mypg.move_mouse(1781, 1068)
    mypg.click_mouse()


def delete_new_user(mypg):
    ''' delete_new_user '''
    mypg.move_mouse(125, 803)
    mypg.click_mouse()
    mypg.move_mouse(1326, 845)
    mypg.click_mouse()
    mypg.move_mouse(1352, 1070)
    mypg.click_mouse()
    mypg.move_mouse(1458, 843)
    mypg.click_mouse()
    mypg.move_mouse(1781, 1068)
    mypg.click_mouse()


def close_if_exists(mypw, tps_exe_path):
    ''' close_if_exists '''
    try:
        mypw.connect(tps_exe_path)
        mypw.kill_application()
    except RuntimeError:
        logging.debug('close_if_exists fail')


# need to run py under root folder of IndelPlan because IndelOanl reads sysconfig.ini
if __name__ == '__main__':

    print('Automation Start')
    c.ConfigWrapper().init_config()
    print('Init config Done')
    pw = pw.PywinautoWrapper('uia')
    pg = pg.PyautoGUIWrapper()

    try:
        tpsexepath, tpsroot, projectroot = get_locations(
            c.ConfigWrapper().config)
        close_if_exists(pw, tpsexepath)
        # change dir to tpsroot
        os.chdir(tpsroot)

        pw.start(tpsexepath)
        # wait IndelPlan launches
        time.sleep(30)
        pw.connect(tpsexepath)
        # print(pw._app.windows())
        # pw._app[LOGIN_TITLE].print_control_identifiers()

        login(pg)
        add_new_user(pg)

        pg.move_mouse(103, 978)
        pg.click_mouse()

        pw.kill_application()
        # pw.close(tpsexepath)

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
    except RuntimeError as ex:
        trace = sys.exc_info()[2]
        pg.capture_screenshot(
            dtt.DateAndTimeUtils.get_today_and_timestamp_as_str_from_timestamp())
        logging.error('file: %s exception: %s', __name__, ex.args)
        pw.kill_application()
    finally:
        close_if_exists(pw, tpsexepath)
        print("Automation FInish")
