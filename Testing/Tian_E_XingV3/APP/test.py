from Tian_E_XingV3.APP import testcases
import json
'''
json.loads(json_str) json字符串转换成字典
json.dumps(dict) 字典转换成json字符串
'''

# 获取token
# testcases.getLoginToken()
# 实例化对象
obj = testcases.TestModuleClass()
# 登录记录接口，用户root
# obj.testLoginRecord('','')
# obj.testLoginRecord(1,10)
# 个人信息接口
# obj.testAccountInfo()
# 修改头像接口,报系统异常{"code":"3001","msg":"系统异常","data":null}
# obj.testAccountUpload(r'E:\workspace\InterfaceTesting\Testing\Tian_E_XingV3\APP\data\youcai.jpg')
# 人员管理-人员添加接口
# obj.testPersonadd('zxm7','0','15108307815','60','','','')
# 人员管理-人员列表接口
# obj.testPersonlist('',1,16,7)
# 人员管理-人员详情接口
# obj.testPersoninfo(24)
# 机构列表接口
obj.testCommonOrglist()
# 所有角色列表接口
# obj.testCommonRolelist()
# 所有人员列表接口
obj.testCommonPersonlist()

# 个人信息编辑接口，其中修改头像是另一个接口
# obj.testAccountEdit('zxm','','','','')
# 修改头像接口4
# filename = 'test.jpg'
# f = {'file':(filename,open(r'C:\Users\Administrator\Desktop\test.jpg','rb'),'image/png')}
# obj.testAccountUpload(f)
# 上传图片接口
# f = open(r'C:\Users\Administrator\Desktop\test.jpg','rb')
# obj.testCommonUpload(0,f)

# 角色管理
# 角色添加接口
'''
{
    "describe": "",
    "funs": [
        0
    ],
    "menus": [
        0
    ],
    "name": ""
}
'''
# dict = {
#     "describe": "",
#     "funs": [
#         1,2
#     ],
#     "menus": [
#         1
#     ],
#     "name": "test01"
# }
# datas = json.dumps(dict)
# # print(type(datas))
# obj.testRoleadd(datas)

# 个人信息接口
# obj.testAccountInfo()

# 站点列表
# obj.testSitelist('1','10','1','')
# 站点详情
# obj.testSitelistInfo('G3006')
# 监测项目列表
# obj.testProjectlist('','','1','10')
# 重点监测项目列表
# obj.testScreenProjectlist('','')
# obj.testWeathernow(104.07,30.67)
# 成都市逐小时预报
# obj.testScreenlocalForecast(104.07,30.67)
# 雅安市逐小时预报
# obj.testScreenlocalForecast(103.00,29.98)
#
# obj.testMobileProjectlist('','','1','16')