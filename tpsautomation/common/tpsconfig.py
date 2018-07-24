#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' config wrapper object '''

import configparser
import os
import tpsautomation.utils.typeutils as tu
import tpsautomation.common.constvalue as cv


class ConfigWrapper():
    ''' config wrapper object '''
    config = {}
    file_name = 'conf.ini'

    """ check key of dict """
    @staticmethod
    def __check_str_param(arg):
        if not tu.TypeUtils.is_str(arg):
            raise TypeError

    @staticmethod
    def __read_config_file():
        config_parser = configparser.ConfigParser()
        # os.path means which folder runs py
        # so need to run py at root folder of project C:\\Users\OUR\Desktop\\tpsautomation
        config_parser.read(os.path.abspath('.') + os.sep +
                           ConfigWrapper.file_name, encoding='utf-8')
        return config_parser

    @staticmethod
    def init_config(section=None):
        ''' init_config '''
        length = len(ConfigWrapper.config)
        if length == 0:
            if section is None or not tu.TypeUtils.is_str(section):
                ConfigWrapper.init_config_by_default()
            else:
                ConfigWrapper.init_config_with_section(section)

    @staticmethod
    def init_config_by_default():
        ''' init_config_by_default '''
        default = ConfigWrapper.__read_config_file().defaults()
        for item in default:
            ConfigWrapper.config[item] = default[item].strip()

    @staticmethod
    def init_config_with_section(section):
        ''' init_config_with_section '''
        ConfigWrapper.__check_str_param(section)
        config_parser = ConfigWrapper.__read_config_file()
        # include default pairs
        # if section does not exist return  {}
        if config_parser.has_section(section):
            pairs = config_parser.items(section)
            for key, val in pairs:
                ConfigWrapper.config[key] = val.strip()

    @staticmethod
    def get_value_in_cache(key):
        ''' get_value_in_cache '''
        ConfigWrapper.__check_str_param(key)
        return ConfigWrapper.config.get(key, cv.ConstValue.DICT_NON_EXIST_VALUE)

    @staticmethod
    def get_value_from_config_file(key, section=None):
        ''' get_value_from_config_file '''
        ConfigWrapper.__check_str_param(key)
        config_parser = ConfigWrapper.__read_config_file()
        if section is None or section.upper().strip() == cv.ConstValue.CONFIG_DEFAULT_SECTION:
            return config_parser[cv.ConstValue.CONFIG_DEFAULT_SECTION][key]
        return config_parser[section][key]

    @staticmethod
    def reload_config(section=None):
        ''' reload_config '''
        ConfigWrapper.config.clear()
        ConfigWrapper.init_config(section)
