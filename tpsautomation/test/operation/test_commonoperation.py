import tpsautomation.operation.commonoperation as co


def test_sleep():
    co1 = co.CommonOperation()
    co1.sleep()
    co1.sleep({})
    co1.sleep(666)
    co1.sleep(-1)
