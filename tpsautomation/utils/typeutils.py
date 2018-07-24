#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' wrapper some convenient method for type check simple type and complex type '''

# from tpsautomation.enumType import *
import tpsautomation.common.enumtype as et


class TypeUtils():
    ''' wrapper some convenient method for type check simple type and complex type '''
    @staticmethod
    def __get_arg_type(arg):
        ''' __get_arg_type '''
        return type(arg).__name__

    @staticmethod
    def is_dict(arg):
        ''' is_dict '''
        return et.PythonBuildInType.dictType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_int(arg):
        ''' is_int '''
        return et.PythonBuildInType.intType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_float(arg):
        ''' is_float '''
        return et.PythonBuildInType.floatType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_str(arg):
        ''' is_str '''
        return et.PythonBuildInType.strType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_bool(arg):
        ''' is_bool '''
        return et.PythonBuildInType.boolType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_tuple(arg):
        ''' is_tuple '''
        return et.PythonBuildInType.tupleType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_list(arg):
        ''' is_list '''
        return et.PythonBuildInType.listType.value == TypeUtils.__get_arg_type(arg)

    @staticmethod
    def is_none(arg=None):
        ''' default value is none if not pass in arg '''
        return arg is None
