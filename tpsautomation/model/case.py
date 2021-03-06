#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' case model '''

import re
from tpsautomation.model.basic import Basic
import tpsautomation.common.constvalue as cv


class Case(Basic):
    ''' case model '''
    __MAX_NOTE = 10000
    __MALE = 'male'
    __FEMALE = 'female'
    __MAX_AGE = __MAX_ADDRESS = 100
    __MAX_HEIGHT = __MAX_WEIGHT = 300

    """ use set_xxx and get_xxx so can check value while initializing"""

    def __init__(self, case_id, name, gender, age=0, height=0, weight=0, address='', phone='', note=''):
        #Basic.__init__(self, id, name)
        super(Case, self).__init__(case_id, name)
        self.set_gender(gender)
        self.set_age(age)
        self.set_height(height)
        self.set_weight(weight)
        self.set_address(address)
        self.set_phone(phone)
        self.set_note(note)

    def __str__(self):
        return 'id: %d - name: %s - gender: %s - age: %d - height: %d - weight: %d - address: %s - phone: %s - note: %s' \
            % (self._id, self._name, self._gender, self._age, self._height, self._weight, self._address, self._phone, self._note)

    def get_gender(self):
        ''' get_gender '''
        return self._gender

    def set_gender(self, value):
        ''' set_gender '''
        if not isinstance(value, type(cv.ConstValue.BOOLEAN_FOR_TYPE)):
            raise TypeError
        self._gender = Case.__MALE if value else Case.__FEMALE

    def get_age(self):
        ''' get_age '''
        return self._age

    def set_age(self, value):
        ''' set_age '''
        if not isinstance(value, type(cv.ConstValue.INT_FOR_TYPE)):
            raise TypeError
        if value < Basic.INT_ZERO or value > Case.__MAX_AGE:
            raise ValueError
        self._age = value

    def get_height(self):
        ''' get_height '''
        return self._height

    def set_height(self, value):
        ''' set_height '''
        if not isinstance(value, type(cv.ConstValue.INT_FOR_TYPE)):
            raise TypeError
        if value < Basic.INT_ZERO or value > Case.__MAX_HEIGHT:
            raise ValueError
        self._height = value

    def get_weight(self):
        ''' get_weight '''
        return self._weight

    def set_weight(self, value):
        ''' set_weight '''
        if not isinstance(value, type(cv.ConstValue.INT_FOR_TYPE)):
            raise TypeError
        if value < Basic.INT_ZERO or value > Case.__MAX_WEIGHT:
            raise ValueError
        self._weight = value

    def get_address(self):
        ''' get_address '''
        return self._address

    def set_address(self, value):
        ''' set_address '''
        if not isinstance(value, type(cv.ConstValue.STR_FOR_TYPE)):
            raise TypeError
        if len(value.strip()) > Case.__MAX_ADDRESS:
            raise ValueError
        self._address = value

    def get_phone(self):
        ''' get_phone '''
        return self._phone

    def set_phone(self, value):
        ''' set_phone '''
        if isinstance(value, type(cv.ConstValue.STR_FOR_TYPE)) and value != cv.ConstValue.EMPTY_STRING \
                and not re.search('^1[0-9]{10}$', value.strip()):
            raise ValueError
        elif isinstance(value, type(cv.ConstValue.INT_FOR_TYPE)) and not re.search('^1[0-9]{10}$', str(value).strip()):
            raise ValueError
        self._phone = value

    def get_note(self):
        ''' get_note '''
        return self._note

    def set_note(self, value):
        ''' set_note '''
        if not isinstance(value, type(cv.ConstValue.STR_FOR_TYPE)):
            raise TypeError
        if len(value.strip()) > Case.__MAX_NOTE:
            raise ValueError
        self._note = value
