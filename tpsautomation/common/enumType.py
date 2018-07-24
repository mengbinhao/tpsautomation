#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' enum of python bulid-in type '''

from enum import Enum, unique


@unique
class PythonBuildInType(Enum):
    ''' enum of python bulid-in type

        for name, member in PythonBuildInType.__members__.items():
            print(name, '=>', member, member.value)
    '''
    intType = 'int'
    strType = 'str'
    boolType = 'bool'
    floatType = 'float'
    listType = 'list'
    tupleType = 'tuple'
    rangeType = 'range'
    setType = 'set'
    dictType = 'dict'
    NoneType = 'NoneType'
    function = 'function'
    module = 'module'

    bytesType = 'byte'
    bytearrayType = 'bytearray'
    memoryviewType = 'memoryview'
    frozensetType = 'frozenset'
    complexType = 'complex'
