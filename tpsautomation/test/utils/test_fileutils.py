import pytest
import tpsautomation.utils.fileutils as fu
import re


def test_split_all():
    assert len(fu.FileUtils.split_all(r'c:\foo\bar\baz.txt')) == 4
    assert len(fu.FileUtils.split_all(r'a/b/c')) == 3
    assert len(fu.FileUtils.split_all(r'/a/b/c')) == 4
    assert len(fu.FileUtils.split_all(r'c:')) == 1
    assert len(fu.FileUtils.split_all(r'/')) == 1
    assert len(fu.FileUtils.split_all(r'c:\\')) == 1
    assert len(fu.FileUtils.split_all(r'c:\\a')) == 2
    assert len(fu.FileUtils.split_all(r'c:\\a\\')) == 3
    assert len(fu.FileUtils.split_all(r'c:\\a\\b')) == 3
    assert len(fu.FileUtils.split_all(r'a\\b')) == 2

def test_list_files():
    path = r'C:\Users\T5810\Desktop\tpsautomation'
    fu.FileUtils.list_files(path)

def test_get_file_abolute_path_if_exists():
    path = r'C:\Users\T5810\Desktop\tpsautomation'
    file_name = r'TODO.md'
    not_exist_file_name = r'TODO_notexist.md'
    assert fu.FileUtils.get_file_abolute_path_if_exists(not_exist_file_name, path) is None
    assert fu.FileUtils.get_file_abolute_path_if_exists(file_name, path) == r'C:\Users\T5810\Desktop\tpsautomation\TODO.md'

def test_if_file_or_dir_exists():
    assert fu.FileUtils.is_file_or_dir_exists(r'C:\Users\T5810\Desktop\tpsautomation\TODO.md') is True
    assert fu.FileUtils.is_file_or_dir_exists(r'C:\Users\T5810\Desktop\tpsautomation\bin') is True
    assert fu.FileUtils.is_file_or_dir_exists(r'C:\Users\T5810\Desktop\tpsautomation\bin_noexist') is not True
    assert fu.FileUtils.is_file_or_dir_exists(r'C:\Users\T5810\Desktop\tpsautomation\TODO_noexist.md') is not True

def test_read_file_by_line():
    assert len(fu.FileUtils.read_file_by_line(r'C:\Users\T5810\Desktop\tpsautomation\pytest.ini')) > 0

@pytest.mark.xfail
def test_write_file_by_line():
    assert len(fu.FileUtils.read_file_by_line(r'C:\Users\T5810\Desktop\tpsautomation\pytest_noexist.ini')) == 0

@pytest.mark.skip
def test_write_file_by_line():
    pass

@pytest.mark.skip
def test_read_file_last_line():
    assert fu.FileUtils.read_small_file_last_line(r'C:\Users\T5810\Desktop\tpsautomation\logs\myapp.log').find(r'pyautoguiwrapper.py') != -1
    
    with pytest.raises(FileNotFoundError) as excinfo:
        fu.FileUtils.read_small_file_last_line(r'C:\Users\T5810\Desktop\tpsautomation\logs\myapp_notexists.log')
    assert excinfo.type.__name__ == 'FileNotFoundError'

@pytest.mark.skip
def test_get_case_list():
    ret = fu.FileUtils.get_case_list(r'C:\Users\T5810\Desktop\tpsautomation\tpsautomation\testcases\beihang\toudao')
    assert len(ret) == 4
    
    with pytest.raises(TypeError) as excinfo:
        fu.FileUtils.get_case_list()
    assert excinfo.type.__name__ == 'TypeError'

def test_get_case_list_exclude_folder():
    pass
    

