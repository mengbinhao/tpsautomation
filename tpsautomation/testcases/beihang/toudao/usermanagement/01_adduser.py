''' add user case '''
import tpsautomation.operation.useroperation as uo
import tpsautomation.model.user as User

new_user_id = 1
new_user_name = 'zatest'
password = '123'
user_type = 1

u = User.User(new_user_id, new_user_name, password, user_type)
uo_obj = uo.UserOperation()
uo_obj.add_user(u)
