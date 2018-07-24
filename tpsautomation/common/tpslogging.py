#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' logging wrapper object '''

import logging
import logging.config
import os
import tpsautomation.common.constvalue as cv


class LoggingWrapper():
    ''' logging wrapper object '''
    conf_path = r'C:\Users\T5810\Desktop\tpsautomation'
    __file_name = 'logger.conf'
    logging.config.fileConfig(conf_path + os.sep + __file_name)

    @staticmethod
    def reload_logging_config():
        ''' reload_logging_config '''
        logging.config.fileConfig(
            LoggingWrapper.conf_path + os.sep + LoggingWrapper.__file_name)

    @staticmethod
    def get_logger(name):
        ''' get_logger '''
        logger = logging.getLogger(name)
        length = len(logger.handlers)
        return logger if length != 0 else None

    @staticmethod
    def load_configuration(config_file=cv.ConstValue.DEFAULT_CONFIG_FILE_PATH):
        ''' load_configuration '''
        if not os.path.exists(config_file) or not os.path.isfile(config_file):
            msg = '%s configuration file does not exist!', config_file
            logging.getLogger(__name__).error(msg)
            raise ValueError(msg)

        try:
            logging.config.fileConfig(
                config_file, disable_existing_loggers=False)
            logging.getLogger(__name__).info(
                '%s configuration file was loaded.', config_file)
        except RuntimeWarning as ex:
            logging.getLogger(__name__).error(
                'Failed to load configuration from %s!', config_file)
            logging.getLogger(__name__).debug(str(ex), exc_info=True)
            raise ex

    @staticmethod
    def record_error(file_name, fun_name, line_number, args):
        ''' file_name is __file__, not __name__ '''
        logging.error('file: %s function: %s lineno: %d args: %s)',
                      file_name, fun_name, line_number, args)

    @staticmethod
    def record_debug_eval(*args):
        ''' use eval handle Dynamic param, but can not record detailed info in log
            like :2018-07-20 14:24:30       <string>  [line:1] root:  DEBUG    excute 3 cases------[case1, case2, case3]
            message_template only use %s
        '''
        tmp = "logging.debug(message_template, "
        for item in args:
            tmp += 'r\'' + str(item) + '\''
            tmp += ', '
        tmp = tmp[:-2] + ")"
        eval(tmp)

    @staticmethod
    def record_debug(message_template, *args):
        ''' record_debug '''
        if len(args) != 2:
            raise ValueError
        logging.debug(message_template, args[0], args[1])
