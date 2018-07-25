#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper method for operating user '''
import sys
import tpsautomation.common.tpslogging as tl
import tpsautomation.model.pywinautowrapper as pw
import tpsautomation.model.pyautoguiwrapper as pg


class UserOperation():
    ''' wrapper method for operating user '''

    def __init__(self):
        self._pw = pw.PywinautoWrapper('uia')
        self._pg = pg.PyautoGUIWrapper()

    def add_user(self, user):
        ''' add_user '''
        try:
            self._pg.move_mouse(127, 718)
            self._pg.click_mouse()
            self._pg.move_mouse(603, 805)
            self._pg.click_mouse()
            self._pg.type_write(user.get_name())
            self._pg.press_special_keyboard('tab')
            self._pg.type_write(user.get_password())
            self._pg.press_special_keyboard('tab')
            self._pg.type_write(user.get_password())
            # below is choice user type
            self.__choice_user_type(user.get_user_type())

            self._pg.press_special_keyboard('enter')
            self._pg.move_mouse(1305, 805)
            self._pg.click_mouse()
        except Exception as ex:
            trace = sys.exc_info()[2]
            tl.LoggingWrapper.record_error(
                __file__, trace.tb_frame.f_code.co_name, trace.tb_lineno, ex.args)
            self._pg.capture_screenshot(trace.tb_frame.f_code.co_name)
            raise
        else:
            tl.LoggingWrapper.record_debug(
                r'file: %s -- message: %s', *[__file__, 'login_tps_successful'])

    def __choice_user_type(self, user_type):
        ''' 1	Visitor
            2	PlanningPhysicist
            3	RadiationPhysicist
            4	RadiationTherapist
            5	ChiefDoctor
            6	Technician
        '''
        self._pg.move_mouse(1033, 561)
        self._pg.click_mouse()
        if user_type == 1:
            self._pg.click_mouse()
        elif user_type == 2:
            self._pg.move_mouse(1014, 601)
            self._pg.click_mouse()
        elif user_type == 3:
            self._pg.move_mouse(1020, 622)
            self._pg.click_mouse()
        elif user_type == 4:
            self._pg.move_mouse(1017, 638)
            self._pg.click_mouse()
        elif user_type == 5:
            self._pg.move_mouse(1021, 656)
            self._pg.click_mouse()
        elif user_type == 6:
            self._pg.move_mouse(1023, 675)
            self._pg.click_mouse()
        else:
            return

    def edit_user(self, user):
        ''' edit_user '''
        pass

    def delete_user(self):
        ''' delete_user '''
        self._pg.move_mouse(127, 718)
        self._pg.click_mouse()
        self._pg.move_mouse(888, 558)
        self._pg.click_mouse()
        self._pg.move_mouse(776, 804)
        self._pg.click_mouse()
        self._pg.move_mouse(965, 555)
        self._pg.click_mouse()
        self._pg.move_mouse(1305, 805)
        self._pg.click_mouse()

    def delete_user_by_id(self, user_id):
        ''' delete_user_by_id '''
        pass
