#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper some convenient method for dict '''

import tpsautomation.utils.typeutils as tu
import tpsautomation.common.constValue as cv

class DictUtils(object):

    ''' makedict '''
    @staticmethod
    def make_dict(**kw):
        if not tu.TypeUtils.is_dict:
            raise TypeError
        return kw

    ''' add_attribute_to_dict '''
    @staticmethod
    def add_word_to_dict(*args, **kw):
        d = {}
        for k, v in args:
            d[k] = v
        d.update(kw)
        return d

    @staticmethod
    def get_specific_word_value(dict_arg, key):
        return dict_arg.get(key, cv.ConstValue.DICT_NON_EXIST_VALUE)

    ''' return a list if condition match'''
    @staticmethod
    def get_intersection_key_of_two_dict(dict1, dict2):
        if not tu.TypeUtils.is_dict(dict1) or not tu.TypeUtils.is_dict(dict2):
            raise TypeError
        return [k for k in dict1 if k in dict2]
    
    @staticmethod
    def class_to_dict(obj):
        is_list = obj.__class__ == [].__class__
        is_set = obj.__class__ == set().__class__

        if is_list or is_set:
            obj_arr = []
            for o in obj:
                dict = {}
                dict.update(o.__dict__)
                obj_arr.append(dict)
            return obj_arr
        else:
            dict = {}
            dict_des = {}
            dict.update(obj.__dict__)
            for key, value in dict.items():
                dict_des[key.replace('_', '')] = value
            return dict_des