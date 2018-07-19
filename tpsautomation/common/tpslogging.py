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

    @staticmethod
    def record_logger(file_name, fun_name, line_number, args):
        logging.error('file: %s function: %s lineno: %d args: %s)',file_name, file_name, line_number, args)