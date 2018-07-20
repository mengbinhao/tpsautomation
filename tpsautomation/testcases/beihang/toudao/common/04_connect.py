import sys
import tpsautomation.operation.commonoperation as co

tpsexepath = sys.argv[1]

co_obj = co.CommonOperation()
co_obj.connect_tps(tpsexepath)

