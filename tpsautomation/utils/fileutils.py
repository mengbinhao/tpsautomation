#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper some convenient method for file related '''

import os
import tpsautomation.common.constValue as cv

class FileUtils(object):

    ''' 分解出文件路径所有组成部分 '''
    @staticmethod
    def split_all(path):
        allparts = []
        while True:
            parts = os.path.split(path)
            # print(parts)
            if parts[0] == path:  # sentinel for absolute paths
                allparts.insert(0, parts[0])
                break
            elif parts[1] == path:  # sentinel for relative paths
                allparts.insert(0, parts[1])
                break
            else:
                path = parts[0]
                allparts.insert(0, parts[1])
        # print(allparts)
        return allparts

    @staticmethod
    def list_files(fileDir):
        for root, dirs, files in os.walk(fileDir):
           for dir in dirs:
               pass
               # print(os.path.join(root, dir))
           for file in files:
               pass
               # print(os.path.join(root, file))

    @staticmethod
    def get_file_abolute_path_if_exists(filename, path):
        candidate = os.path.join(path, filename)
        return os.path.abspath(candidate) if os.path.exists(candidate) else None

    @staticmethod
    def is_file_or_dir_exists(arg):
        return os.path.exists(arg)
    
    @staticmethod
    def read_file_by_line(path_and_fileName, encoding = 'utf-8'):
        l = []
        with open(path_and_fileName, 'r', encoding = encoding) as f:
            for line in f:
                l.append(line)
        return l

    @staticmethod
    def write_file_by_line(path_and_fileName, encoding = 'utf-8'):
        with open(path_and_fileName, '+', encoding = encoding) as f:
            for line in f:
                f.write('test' + '\n')

    @staticmethod
    # todo
    def read_big_file_last_line(path_and_fileName, encoding = 'utf-8'):
        with open(path_and_fileName, 'rb') as f:
            # first_line = f.readline()  #读第一行
            off = -50      #设置偏移量
            while True:
                f.seek(off, 2)
                f.readlines()
                lines = f.readlines()
                if len(lines)>=2:
                    last_line = lines[-1] #取最后一行
                    break
                off *= 2
            #print(last_line.decode())
            return last_line.decode()

    @staticmethod
    def read_small_file_last_line(path_and_fileName, encoding = 'utf-8'):
        with open(path_and_fileName, 'r') as f:
            lines  = f.readlines()
            return lines[-1] if len(lines) > 0 else None
    
    @staticmethod
    def get_case_list(root):
        result = []
        for root, dirs, files in os.walk(root):
           for file_name in files:
               if file_name.endswith(cv.ConstValue.PYTHON_SUFFIX):
                    result.append(root + os.sep + file_name)
        return result
