#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' User model '''

from tpsautomation.model.basic import Basic
import tpsautomation.common.constValue as cv

class User(Basic):

    __MIN_PASSWORD_LENGTH= 1
    __MAX_PASSWORD_LENGTH= 10
    
    '''
        1 Visitor
        2 PlanningPhysicist
        3 RadiationPhysicist
        4 RadiationTherapist
        5 ChiefDoctor
        6 Technician
    '''
    __USER_TYPE = [1,2,3,4,5,6]

    """ use set_xxx and get_xxx so can check value while initializing"""

    def __init__(self, id, name, password, user_type):
        #Basic.__init__(self, id, name)
        super(User,self).__init__(id, name)
        self.set_password(password)
        self.set_user_type(user_type)
        self._login_information = 'Unknown'

    def __str__(self):
        return 'id: %d - name: %s - password: %s - user_type: %d' % (self._id, self._name, self._password, self._user_type)

    def get_password(self):
         return self._password

    def set_password(self, value):
        if not isinstance(value, type(cv.ConstValue.STR_FOR_TYPE)):
            raise TypeError
        length = len(value.strip())
        if length < User.__MIN_PASSWORD_LENGTH or length > User.__MAX_PASSWORD_LENGTH: 
            raise ValueError
        self._password = value

    def get_user_type(self):
         return self._user_type

    def set_user_type(self, value):
        if not isinstance(value, type(cv.ConstValue.INT_FOR_TYPE)):
            raise TypeError
        if value not in User.__USER_TYPE:
            raise ValueError
        self._user_type = value
