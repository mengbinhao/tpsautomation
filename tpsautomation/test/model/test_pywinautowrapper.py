import pytest
import os
import datetime
import pywinauto
import time
import tpsautomation.model.pywinautowrapper as c
import tpsautomation.utils.fileutils as fu
import tpsautomation.utils.dateandtimeutils as dt

pw = c.PywinautoWrapper('uia')
TPS_EXE = r'C:\IndelPlan\IndelPlanV2.0.exe'

@pytest.mark.skip
def test_connect():
    pw.connect('notepad.exe')
    #pw.connect('23536', {})
    pw.connect(r'C:\Windows\System32\notepad.exe')
    

    with pytest.raises(pywinauto.findwindows.ElementNotFoundError) as excinfo:
        pw.connect('readme.txt', 1)
    assert excinfo.type.__name__ == 'ElementNotFoundError'

    with pytest.raises(pywinauto.application.ProcessNotFoundError) as excinfo:
        pw.connect('not exist')
    assert excinfo.type.__name__ == 'ProcessNotFoundError'

@pytest.mark.skip
def test_close_tps():
    with pytest.raises(pywinauto.application.AppNotConnected) as excinfo:
        pw.close_tps()
    assert excinfo.type.__name__ == 'AppNotConnected'

    ''' have to connect App first '''
    pw.connect(TPS_EXE)
    pw.close_tps()

@pytest.mark.skip
def test_close_tps_by_button():
    with pytest.raises(pywinauto.application.AppNotConnected) as excinfo:
        pw.close_tps_by_button()
    assert excinfo.type.__name__ == 'AppNotConnected'
    
    ''' have to connect App first '''
    pw.connect(TPS_EXE)
    #pw._app['Login Desktop'].print_control_identifiers()
    pw.close_tps_by_button()

@pytest.mark.skip
def test_kill_application():
    ''' have to connect App first '''
    with pytest.raises(pywinauto.application.AppNotConnected) as excinfo:
        pw.kill_application()
    assert excinfo.type.__name__ == 'AppNotConnected'

    pw.connect(TPS_EXE)
    pw.kill_application()

# below todo
@pytest.mark.skip
def test_max_window():
    ''' have to connect App first '''
    with pytest.raises(TypeError) as excinfo:
        pw.max_window()
    assert excinfo.type.__name__ == 'TypeError'

    with pytest.raises(pywinauto.application.AppNotConnected) as excinfo:
        pw.max_window('AppNotConnected')
    assert excinfo.type.__name__ == 'AppNotConnected'

def test_menu_click():
    pass

def test_input():
    pass

def test_click():
    pass
    
def test_double_click():
    pass 
def test_right_click():
    pass