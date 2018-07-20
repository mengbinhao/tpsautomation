#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' logging wrapper object '''

import logging
import logging.config
import os
import tpsautomation.utils.typeutils as tu
import tpsautomation.common.constValue as cv

class LoggingWrapper(object):

    conf_path = r'C:\Users\T5810\Desktop\tpsautomation'
    __file_name = 'logger.conf'
    logging.config.fileConfig(conf_path + os.sep + __file_name)

    @staticmethod
    def reload_logging_config():
        logging.config.fileConfig(LoggingWrapper.conf_path + os.sep + LoggingWrapper.__file_name)
    
    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        return logger if len(logger.handlers) != 0 else None

    @staticmethod
    def load_configuration(config_file = cv.ConstValue.DEFAULT_CONFIG_FILE_PATH):
        if not os.path.exists(config_file) or not os.path.isfile(config_file):
            msg = '%s configuration file does not exist!', config_file
            logging.getLogger(__name__).error(msg)
            raise ValueError(msg)

        try:
            logging.config.fileConfig(config_file, disable_existing_loggers=False)
            logging.getLogger(__name__).info(
                '%s configuration file was loaded.', config_file)
        except RuntimeWarning as e:
            logging.getLogger(__name__).error(
                'Failed to load configuration from %s!', config_file)
            logging.getLogger(__name__).debug(str(e), exc_info=True)
            raise e 

    ''' file_name is __file__, not __name__ '''
    @staticmethod
    def record_error(file_name, fun_name, line_number, args):
        logging.error('file: %s function: %s lineno: %d args: %s)',file_name, fun_name, line_number, args)

    ''' use eval handle Dynamic param, but can not record detailed info in log
        like :2018-07-20 14:24:30       <string>  [line:1] root:  DEBUG    excute 3 cases------[case1, case2, case3]
        message_template only use %s
    '''
    @staticmethod
    def record_debug_eval(message_template, *args):
        tmp = "logging.debug(message_template, "
        for item in args:
            tmp += 'r\'' + str(item) + '\''
            tmp += ', '
        tmp = tmp[:-2] + ")"
        eval(tmp)

    @staticmethod
    def record_debug(message_template, *args):
        if len(args) != 2:
            raise ValueError
        logging.debug(message_template, args[0], args[1])