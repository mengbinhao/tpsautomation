''' connect case '''
import sys
import tpsautomation.operation.commonoperation as co

tps_exe_path = sys.argv[1]

co_obj = co.CommonOperation()
co_obj.connect_tps(tps_exe_path)
co_obj = None
