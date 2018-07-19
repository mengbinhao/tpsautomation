import pytest
import tpsautomation.common.tpslogging as c

def test_get_logger():
    assert c.LoggingWrapper.get_logger('example01') is not None
    assert c.LoggingWrapper.get_logger('example022222') is None

def test_get_logger2():
    logger = c.LoggingWrapper.get_logger('example01')
    logger.debug('This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')

    logger2 = c.LoggingWrapper.get_logger('example02')
    logger2.debug('This is debug message')
    logger2.info('This is info message')
    logger2.warning('This is warning message')

def test_load_configuration():
    c.LoggingWrapper.load_configuration(r'C:\Users\T5810\Desktop\tpsautomation\logger.conf')
