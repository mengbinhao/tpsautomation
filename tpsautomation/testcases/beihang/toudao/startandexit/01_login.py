''' login case '''
import sys
import tpsautomation.operation.commonoperation as co

tps_exe_path = sys.argv[1]
user_name = 'our'
password = '123'

co_obj = co.CommonOperation()
co_obj.start_tps(tps_exe_path)
co_obj.connect_tps(tps_exe_path)
co_obj.login_tps(user_name, password)
