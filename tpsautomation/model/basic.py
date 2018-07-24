#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' Basic model '''

import tpsautomation.common.constvalue as cv


class Basic():
    ''' Basic model '''
    INT_ZERO = 0  # child can access
    __MAX_NAME_LENGTH = 100
    __MAX_ID = 10000

    """ use set_xxx and get_xxx so can check value while initializing"""

    def __init__(self, id, name):
        self.set_id(id)
        self.set_name(name)

    def __str__(self):
        return 'id: %d - name: %s' % (self._id, self._name)

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):
    #     if not isinstance(name, type(cv.ConstValue.STR_FOR_TYPE)):
    #         raise TypeError
    #     length = len(name.strip())
    #     if length == 0 or length > 20:
    #         raise ValueError
    #     self._name = name

    def get_name(self):
        ''' get_name '''
        return self._name

    def set_name(self, value):
        ''' set_name '''
        if not isinstance(value, type(cv.ConstValue.STR_FOR_TYPE)):
            raise TypeError
        length = len(value.strip())
        if length == Basic.INT_ZERO or length > Basic.__MAX_NAME_LENGTH:
            raise ValueError
        self._name = value

    def get_id(self):
        ''' get_id '''
        return self._id

    def set_id(self, value):
        ''' set_id '''
        if not isinstance(value, type(cv.ConstValue.INT_FOR_TYPE)):
            raise TypeError
        if value < Basic.INT_ZERO or value > Basic.__MAX_ID:
            raise ValueError
        self._id = value
