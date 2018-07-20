import sys
import tpsautomation.operation.commonoperation as co

tpsexepath = sys.argv[1]

co_obj = co.CommonOperation()
co_obj.connect_tps(tpsexepath)

#co_obj.start_tps(tpsexepath)
#co_obj.connect_tps(tpsexepath)
#co_obj.login_tps(tpsexepath, user_name, password)

