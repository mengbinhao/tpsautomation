#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper some convenient method for list '''


class ListUtils(object):
    ''' wrapper some convenient method for list '''
    @staticmethod
    def filter_empty_string_in_list(target_list):
        ''' get not empty string from one list '''
        return [x for x in target_list if not x.strip() == '']

    @staticmethod
    def join_list_by_symbol(symbol, target_list):
        ''' join list by symbol '''
        return symbol.join(target_list)

    @staticmethod
    def remove_duplicate(target_list):
        ''' remove duplicate '''
        return list(set(target_list))

    @staticmethod
    def is_exist_in_list(target_list, target_str):
        ''' check is target_str in target_str_list '''
        if any(x in target_str for x in target_list):
            return True
        return False
