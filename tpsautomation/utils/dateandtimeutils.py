#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper some convenient method for date and time '''

import datetime
import time
import sys
import math
import tpsautomation.common.constValue as cv


class DateAndTimeUtils(object):

    @staticmethod
    def get_today_as_str(fmt=r'%Y-%m-%d'):
        return datetime.date.today().strftime(fmt)

    @staticmethod
    def get_today_as_str_from_timestamp(fmt=r'%Y-%m-%d'):
        return datetime.datetime.fromtimestamp(time.time()).strftime(fmt)

    @staticmethod
    def get_today_and_timestamp_as_str_from_timestamp(fmt=r'%Y-%m-%d'):
        return datetime.datetime.fromtimestamp(time.time()).strftime(fmt) + cv.ConstValue.CUT_OFF_RULE + str(time.time())

    @staticmethod
    def get_date_and_time_as_str(fmt=r'%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.now().strftime(fmt)

    @staticmethod
    def get_date_and_time_as_datetime(str, fmt=r'%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.strptime(str, fmt)

    @staticmethod
    def get_delta_between_two_days(str1, str2, fmt=r'%Y-%m-%d'):
        d1 = datetime.datetime.strptime(str1, fmt)
        d2 = datetime.datetime.strptime(str2, fmt)
        return (d1 - d2).days

    @staticmethod
    def get_delta_days_from_now(number, fmt=r'%Y-%m-%d'):
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=number)
        return (now + delta).strftime(fmt)

    @staticmethod
    def convert_seconds_to_display_time(all_time):
        if not isinstance(all_time, type(cv.ConstValue.INT_FOR_TYPE)):
            raise TypeError
        if all_time < cv.ConstValue.ZERO_INT or all_time > sys.maxsize:
            raise ValueError
        day = 24*60*60
        hour = 60*60
        min = 60
        if all_time >= 0 and all_time < 60:
            return "%d sec" % math.ceil(all_time)
        elif all_time >= min and all_time < hour:
            mins = divmod(all_time, min)
            return "%d min, %d sec" % (int(mins[0]), math.ceil(mins[1]))
        elif all_time >= hour and all_time < day:
            hours = divmod(all_time, hour)
            return '%d hours, %s' % (int(hours[0]), DateAndTimeUtils.convert_seconds_to_display_time(hours[1]))
        elif all_time >= day:
            days = divmod(all_time, day)
            return "%d days, %s" % (int(days[0]), DateAndTimeUtils.convert_seconds_to_display_time(days[1]))
        else:
            raise ValueError
