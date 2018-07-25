''' delete user case '''
import tpsautomation.operation.useroperation as uo

new_user_id = 1
new_user_name = 'zatest'

# according exists user, delete user zatest(Technician)
uo_obj = uo.UserOperation()
uo_obj.delete_user()
