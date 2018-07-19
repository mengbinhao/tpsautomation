#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper some convenient method for type check include simple type and complex type '''

# from tpsautomation.enumType import *
import tpsautomation.common.enumType as et

class TypeUtils(object):

    ''' __get_arg_type '''
    @staticmethod
    def __get_arg_type(arg):
        return type(arg).__name__

    ''' is_dict '''
    @staticmethod
    def is_dict(arg):
        return et.PythonBuildInType.dictType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_int(arg):
        return et.PythonBuildInType.intType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_float(arg):
        return et.PythonBuildInType.floatType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_str(arg):
        return et.PythonBuildInType.strType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_bool(arg):
        return et.PythonBuildInType.boolType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_tuple(arg):
        return et.PythonBuildInType.tupleType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_dict(arg):
        return et.PythonBuildInType.dictType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_list(arg):
        return et.PythonBuildInType.listType.value == TypeUtils.__get_arg_type(arg)

    ''' default value is none if not pass in arg'''
    @staticmethod
    def is_none(arg=None):
        return arg is None
