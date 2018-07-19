import pytest
import datetime
import pyautogui
import tpsautomation.model.pyautoguiwrapper as c
import tpsautomation.utils.fileutils as fu
import tpsautomation.utils.dateandtimeutils as dt
import tpsautomation.common.tpsconfig as conf

pw = c.PyautoGUIWrapper()

def test_check_screen_resolution():
    
    # generate file log
    pw.check_screen_resolution()

    path = r'C:\Users\T5810\Desktop\tpsautomation\logs\myapp.log'
    notexist_path = r'C:\Users\T5810\Desktop\tpsautomation\logs\myappaaaaaaa.log'
    assert fu.FileUtils.read_small_file_last_line(path)[:19] == dt.DateAndTimeUtils.get_date_and_time_as_str()

    with pytest.raises(FileNotFoundError) as excinfo:
        fu.FileUtils.read_small_file_last_line(notexist_path)[:19] == dt.DateAndTimeUtils.get_date_and_time_as_str()
    assert excinfo.type.__name__ == 'FileNotFoundError'

def test_move_mouse():
    width, height = pw.get_current_screen_resolution()
    pw.move_mouse(width // 2, height //2)
    # pw.move_mouse(200, 200, {})

def test_move_mouse_rel():
    pw.move_mouse_rel(-200, -200)

def test_get_mouse_position():
    weight, height = pw.get_current_mouse_position()
    assert weight == 760
    assert height == 340

def test_is_mouse_position_in_screen():
    assert pw.is_mouse_position_in_screen() is True

@pytest.mark.skip
def test_click():
    pw.click_mouse()
    pw.dbclick_mouse()
    pw.drag_mouse()
    # pw.draw_rect()

@pytest.mark.skip
def test_type_related():
    pw.click_mouse()
    pw.type_write('jack')
    pw.press_special_keyboard('enter')
    pw.hot_key('ctrl', 'a')

def test_capture_screenshot():
    conf.configWrapper().init_config()
    path = r'test_capture_screenshot'
    pw.capture_screenshot(path)

    with pytest.raises(TypeError) as excinfo:
        pw.capture_screenshot()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(ValueError) as excinfo:
        pw.capture_screenshot('')
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        pw.capture_screenshot({})
    assert excinfo.type.__name__ == 'ValueError'

    with pytest.raises(ValueError) as excinfo:
        pw.capture_screenshot('./images/')
    assert excinfo.type.__name__ == 'ValueError'   
    
    with pytest.raises(ValueError) as excinfo:
        pw.capture_screenshot('./images\\')
    assert excinfo.type.__name__ == 'ValueError'      

def test_safe_exit():
    with pytest.raises(pyautogui.FailSafeException) as excinfo:
        pw.safe_exit()
    assert excinfo.type.__name__ == 'FailSafeException'

    