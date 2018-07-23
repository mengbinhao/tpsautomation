#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper some convenient method for str '''


class StrUtils(object):
    ''' wrapper some convenient method for str '''
    @staticmethod
    def is_str_like(arg):
        ''' is_str_likes '''
        try:
            arg + ''
        except TypeError:
            return False
        else:
            return True
