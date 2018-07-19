#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper some convenient method for str '''

class StrUtils(object):

    ''' is_str_likes '''
    @staticmethod
    def is_str_like(arg):
        try:
            arg + ''
        except:
            return False
        else:
            return True