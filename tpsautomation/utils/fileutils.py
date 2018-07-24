#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' wrapper some convenient method for file related '''

import os
import tpsautomation.common.constvalue as cv


class FileUtils():
    ''' wrapper some convenient method for file related '''
    @staticmethod
    def split_all(path):
        ''' 分解出文件路径所有组成部分 '''
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
    def list_files(file_dir):
        ''' list_files '''
        pass
        # for dirs, files in os.walk(fileDir):
        #     for folder in dirs:
        #         pass
        #         # print(os.path.join(root, dir))
        #     for file in files:
        #         pass
        #         # print(os.path.join(root, file))

    @staticmethod
    def get_file_abolute_path_if_exists(filename, path):
        ''' get_file_abolute_path_if_exists '''
        candidate = os.path.join(path, filename)
        return os.path.abspath(candidate) if os.path.exists(candidate) else None

    @staticmethod
    def is_file_or_dir_exists(arg):
        ''' check if is_file_or_dir_exists '''
        return os.path.exists(arg)

    @staticmethod
    def read_file_by_line(path_and_file_name, encoding='utf-8'):
        ''' read_file_by_line '''
        result = []
        with open(path_and_file_name, 'r', encoding=encoding) as file:
            for line in file:
                result.append(line)
        return result

    @staticmethod
    def write_file_by_line(path_and_file_name, encoding='utf-8'):
        ''' write_file_by_line '''
        with open(path_and_file_name, 'a', encoding=encoding) as file:
            for line in file:
                file.write(line + '\n')

    @staticmethod
    # todo
    def read_big_file_last_line(path_and_file_name, encoding='utf-8'):
        ''' read_big_file_last_line '''
        with open(path_and_file_name, 'rb', encoding=encoding) as file:
            # first_line = f.readline()  #读第一行
            off = -50  # 设置偏移量
            while True:
                file.seek(off, 2)
                file.readlines()
                lines = file.readlines()
                if len(lines) >= 2:
                    last_line = lines[-1]  # 取最后一行
                    break
                off *= 2
            # print(last_line.decode())
            return last_line.decode()

    @staticmethod
    def read_small_file_last_line(path_and_file_name, encoding='utf-8'):
        ''' read_small_file_last_line '''
        with open(path_and_file_name, 'r', encoding=encoding) as file:
            lines = file.readlines()
            length = len(lines)
            return lines[-1] if length > 0 else None

    @staticmethod
    def get_case_list(root):
        ''' get_case_list '''
        result = []
        for root_dir, dirs, files in os.walk(root):
            for file_name in files:
                if file_name.endswith(cv.ConstValue.PYTHON_SUFFIX):
                    result.append(root_dir + os.sep + file_name)
        return result

    @staticmethod
    def get_case_list_exclude_folders(root, exclude_folders):
        ''' get_case_list_exclude_folders '''
        pass
