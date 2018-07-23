#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper some convenient method for dict '''

import tpsautomation.utils.typeutils as tu
import tpsautomation.common.constvalue as cv


class DictUtils(object):
    ''' wrapper some convenient method for dict '''
    @staticmethod
    def make_dict(**kw):
        ''' makedict '''
        if not tu.TypeUtils.is_dict:
            raise TypeError
        return kw

    @staticmethod
    def add_word_to_dict(*args, **kw):
        ''' add_attribute_to_dict '''
        tmp = {}
        for key, val in args:
            tmp[key] = val
        tmp.update(kw)
        return tmp

    @staticmethod
    def get_specific_word_value(dict_arg, key):
        ''' get_specific_word_value, if not exist return cv.ConstValue.DICT_NON_EXIST_VALUE '''
        return dict_arg.get(key, cv.ConstValue.DICT_NON_EXIST_VALUE)

    @staticmethod
    def get_intersection_key(dict_one, dict2_two):
        ''' return a list if condition match'''
        if not tu.TypeUtils.is_dict(dict_one) or not tu.TypeUtils.is_dict(dict2_two):
            raise TypeError
        return [k for k in dict_one if k in dict2_two]

    @staticmethod
    def class_to_dict(obj):
        ''' convert class_to_dict '''
        is_list = obj.__class__ == [].__class__
        is_set = obj.__class__ == set().__class__

        if is_list or is_set:
            obj_arr = []
            for item in obj:
                tmp = {}
                tmp.update(item.__dict__)
                obj_arr.append(tmp)
            return obj_arr
        else:
            tmp = {}
            dict_des = {}
            tmp.update(obj.__dict__)
            for key, value in tmp.items():
                dict_des[key.replace('_', '')] = value
            return dict_des
