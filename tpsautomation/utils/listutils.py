#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper some convenient method for list '''

class ListUtils(object):

    @staticmethod
    def filter_empty_string_in_list(target_list):
        return [x for x in target_list if not x.strip() == '']

    @staticmethod
    def join_list_by_symbol(symbol, target_list):
        return symbol.join(target_list)

    @staticmethod
    def remove_duplicate(target_list):
        return list(set(target_list))

    @staticmethod
    def is_exist_in_list(target_list, target_str):
        if any(x in target_str for x in target_list):
            return True
        return False