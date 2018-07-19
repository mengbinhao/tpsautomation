#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' config wrapper object '''

import configparser
import os
import tpsautomation.utils.typeutils as tu
import tpsautomation.common.constValue as cv

class configWrapper(object):

    config = {}
    file_name = 'conf.ini'

    """ check key of dict """
    @staticmethod
    def __check_str_param(arg):
        if not tu.TypeUtils.is_str(arg):
            raise TypeError

    @staticmethod
    def __read_config_file():
        cp = configparser.ConfigParser()
        ''' 
            os.path means which folder runs py 
            so need to run py at root folder of project C:\\Users\OUR\Desktop\\tpsautomation
        '''
        cp.read(os.path.abspath('.') + os.sep + configWrapper.file_name, encoding='utf-8')
        return cp

    @staticmethod
    def init_config(section=None):
        if len(configWrapper.config) == 0:
            if section is None or not tu.TypeUtils.is_str(section):
                configWrapper.init_config_by_default()
            else:
                configWrapper.init_config_with_section(section)

    @staticmethod
    def init_config_by_default():
        cp = configWrapper.__read_config_file()
        default = cp.defaults()
        for item in default:
            configWrapper.config[item] = default[item].strip()

    @staticmethod
    def init_config_with_section(section):
        configWrapper.__check_str_param(section)
        cp = configWrapper.__read_config_file()
        # include default pairs
        # if section does not exist return  {}
        if cp.has_section(section):
            pairs = cp.items(section)
            for key, val in pairs:
                configWrapper.config[key] = val.strip()

    @staticmethod
    def get_special_value_in_cache(key):
        configWrapper.__check_str_param(key)
        return configWrapper.config.get(key, cv.ConstValue.DICT_NON_EXIST_VALUE)

    @staticmethod
    def get_special_value_from_config_file(key, section=None):
        configWrapper.__check_str_param(key)
        cp = configWrapper.__read_config_file()
        if section is None or section.upper().strip() == cv.ConstValue.CONFIG_DEFAULT_SECTION:
            return cp[cv.ConstValue.CONFIG_DEFAULT_SECTION][key]
        return cp[section][key]

    @staticmethod
    def reload_config(section = None):
        configWrapper.config.clear()
        configWrapper.init_config(section)
