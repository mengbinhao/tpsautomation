''' exit case '''
import sys
import tpsautomation.operation.commonoperation as co

tps_exe_path = sys.argv[1]

co_obj = co.CommonOperation()
co_obj.logout_tps(tps_exe_path)
co_obj.close_tps_by_x()
