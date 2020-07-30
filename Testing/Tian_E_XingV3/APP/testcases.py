import requests


# 共计?个接口

# 自动格式化：ctrl + alt + L ; shift + ctrl + F

def getLoginToken():
    message = TestModuleClass().testLoginModule('zxm', 'Kk123456', '2')
    token = message['data']['token']
    # print(token)
    return token


class TestModuleClass():
    def __init__(self):
        self.host = 'http://weather.kedalo.com:9989'

    # 登录接口1, 0:PC 1:IOS 2:android
    def testLoginModule(self, username, pwd, platform):
        url = self.host + '/login'
        datas = {'username': username, 'password': pwd, 'platform': platform}
        r = requests.post(url, data=datas)
        message = r.json()
        # print(message)
        return message

    # 个人管理接口
    # 登录记录接口2
    def testLoginRecord(self, pageNo, pageSize):
        url = self.host + '/manage/admin/security/loginRecord'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'pageNo': pageNo, 'pageSize': pageSize}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 个人信息接口3
    def testAccountInfo(self):
        url = self.host + '/manage/admin/account/info'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.get(url=url, headers=header)
        message3 = r.text
        print(message3)
        return message3

    # 修改头像接口4
    def testAccountUpload(self, filepath):
        url = self.host + '/manage/admin/account/upload'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.post(url, headers=header, files=filepath)
        message = r.text
        print(message)
        return message

    # 上传图片接口
    def testCommonUpload(self, type, file):
        url = self.host + '/manage/common/upload'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.post(url, headers=header, data=type, files=file)
        message = r.text
        print(message)
        return message

    # 修改手机号或者密码接口5
    def testSecurityEdit(self, password, phone):
        url = self.host + '/manage/admin/security/edit'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'password': password, 'phone': phone}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 个人资料编辑6
    def testAccountEdit(self, name, gender, phone, email, job):
        url = self.host + '/manage/admin/account/edit'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'gender': gender, 'phone': phone, 'email': email, 'job': job}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 移动端登录接口（此处取消一个取消登录）
    # 二维码扫描接口7
    def testVerifiQrcode(self, token):
        url = self.host + '/mobile/common/verifiQrcode'
        datas = {'token': token}
        r = requests.get(url, params=datas)
        message = r.text
        print(message)
        return message

    # 确认登录接口8
    def testCommonConfirm(self, token):
        url = self.host + '/mobile/common/confirm'
        datas = {'token': token}
        r = requests.get(url, params=datas)
        message = r.text
        print(message)
        return message

    # 发送短信接口9
    def testMobileAppSendCode(self, phone):
        url = self.host + '/mobile/appSendCode'
        datas = {'phone': phone}
        r = requests.get(url, params=datas)
        message = r.text
        print(message)
        return message

    # 短信登录接口10
    def testAppLogin(self, phone, code, platform):
        url = self.host + '/mobile/appLogin'
        datas = {'phone': phone, 'code': code, 'platform': platform}
        r = requests.get(url, params=datas)
        message = r.text
        print(message)
        return message

    # 取消登录接口63,此处的token是二维码token
    def testCommonlogout(self, token):
        url = self.host + '/mobile/common/cancel'
        datas = token
        r = requests.get(url, params=datas)
        message = r.text
        print(message)
        return message

    # 移动端个人中心更新接口11
    def testCenterUpnew(self, platform):
        url = self.host + '/mobile/center/upnew'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'platform': platform}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 移动端个人中心关联项目接口12
    def testProjectList(self, name, type, pageNo, pageSize):
        url = self.host + '/mobile/project/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'type': type, 'pageNo': pageNo, 'pageSize': pageSize}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 移动端个人中心发送短信接口13
    def testAppSendCode(self, phone):
        url = self.host + '/appSendCode'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'phone': phone}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 移动端个人中心验证短信接口14
    def testVerifiCode(self, phone, code):
        url = self.host + '/verificode'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'phone': phone, 'code': code}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 移动端个人中心修改密码接口15
    def testResetPassword(self, password, uid):
        url = self.host + '/resetPassword'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'password': password, 'uid': uid}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 获取真实时间接口16
    def testScreenRealtime(self):
        url = self.host + '/screen/realtime'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.get(url, headers=header)
        message = r.text
        print(message)
        return message

    # 获取图片接口17
    def testCommonImage(self, path, width, height):
        url = self.host + '/manage/common/image'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'path': path, 'width': width, 'height': height}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # PC管理端接口
    # 获取二维码接口18
    def testQrcode(self):
        url = self.host + '/qrcode'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.get(url, headers=header)
        message = r.text
        print(message)
        return message

    # 机构列表接口19
    def testCommonOrglist(self):
        url = self.host + '/manage/common/orgList'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.get(url, headers=header)
        message = r.text
        print(message)
        return message

    # 获取登录状态接口20
    def testLoginStatus(self):
        url = self.host + '/loginStatus'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.get(url, headers=header)
        message = r.text
        print(message)
        return message

    # 应急类型列表接口21
    def testCommonTypelist(self):
        url = self.host + '/manage/common/typeList'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.get(url, headers=header)
        message = r.text
        print(message)
        return message

    # 行业列表接口22
    def testCommonIndustrylist(self):
        url = self.host + '/manage/common/industryList'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.get(url, headers=header)
        message = r.text
        print(message)
        return message

    # 所有角色列表接口
    def testCommonRolelist(self):
        url = self.host + '/manage/common/roleList'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.get(url, headers=header)
        message = r.text
        print(message)
        return message

    # 所有人员列表接口
    def testCommonPersonlist(self):
        url = self.host + '/manage/common/personList'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.get(url, headers=header)
        message = r.text
        print(message)
        return message

    # 人员管理
    # 人员管理人员添加接口23
    def testPersonadd(self, name, gender, phone, departmentId, email, job, headImg):
        url = self.host + '/manage/person/add'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'gender': gender, 'phone': phone, 'departmentId': departmentId, 'email': email,
                 'job': job, 'headImg': headImg}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 人员管理人员修改接口24
    def testPersonedit(self, name, gender, phone, departmentId, email, job, headImg, personId):
        url = self.host + '/manage/person/edit'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'gender': gender, 'phone': phone, 'departmentId': departmentId, 'email': email,
                 'job': job, 'headImg': headImg, 'personId': personId}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 人员管理人员列表接口25
    def testPersonlist(self, name, pageNo, pageSize, departmentId):
        url = self.host + '/manage/person/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token, 'Content-Type': 'application/json'}
        datas = {'name': name, 'pageNo': pageNo, 'pageSize': pageSize, 'departmentId': departmentId}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 人员管理人员详情接口26
    def testPersoninfo(self, personId):
        url = self.host + '/manage/person/info'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'personId': personId}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 人员管理人员删除接口27,id是一个list
    def testPersondel(self, id):
        url = self.host + '/manage/person/del'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = id
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 数据同步日志类型列表接口28
    def testLogTypelist(self):
        url = self.host + '/manage/data/synWeather/logTypeList'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        r = requests.get(url, headers=header)
        message = r.text
        print(message)
        return message

    # 数据同步日志列表接口29
    def testDatalist(self, name, type, startTime, endTime, pageNo, pageSize):
        url = self.host + '/manage/data/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'type': type, 'startTime': startTime, 'endTime': endTime, 'pageNo': pageNo,
                 'pageSize': pageSize}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 应急管理应急列表接口30
    def testEmergencylist(self, pageNo, pageSize, name):
        url = self.host + '/$server$/manage/emergency/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'pageNo': pageNo, 'pageSize': pageSize, 'name': name}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 应急管理应急添加接口31
    def testEmergencyAdd(self, name, type, lat, lng, remarks, areas):
        url = self.host + '/manage/emergency/add'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'type': type, 'lat': lat, 'lng': lng, 'remarks': remarks, 'areas': areas}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 应急管理应急修改接口32
    def testEmergencyEdit(self, basicId, name, type, lat, lng, remarks, areas):
        url = self.host + '/manage/emergency/edit'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'basicId': basicId, 'name': name, 'type': type, 'lat': lat, 'lng': lng, 'remarks': remarks,
                 'areas': areas}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 应急管理应急删除接口33,ids是list
    def testEmergencydel(self, ids):
        url = self.host + '/manage/emergency/del'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = ids
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 视频监控监控列表接口34
    def testMonitorlist(self, name, pageNo, pageSize):
        url = self.host + '/manage/monitor/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'pageNo': pageNo, 'pageSize': pageSize}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 视频监控监控添加接口35
    def testMonoitoradd(self, lng, lat, monitorName, industryId, url, remarks):
        url = self.host + '/manage/monitor/add'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'lng': lng, 'lat': lat, 'monitorName': monitorName, 'industryId': industryId, 'url': url,
                 'remarks': remarks}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 视频监控监控详情接口36
    def testMonitorinfo(self, monitorId):
        url = self.host + '/manage/monitor/info'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'monitorId': monitorId}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 视频监控监控修改接口37
    def testMonitoredit(self, monitorId, monitorName, lng, lat, industryId, url, remarks):
        url = self.host + '/manage/monitor/edit'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'monitorId': monitorId, 'monitorName': monitorName, 'lng': lng, 'lat': lat, 'industryId': industryId,
                 'url': url, 'remarks': remarks}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 视频监控监控删除接口38,ids列表
    def testMonitordel(self, ids):
        url = self.host + '/manage/monitor/del'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = ids
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 组织机构机构添加接口39
    def testPersonOrgadd(self, name, parentId):
        url = self.host + '/manage/person/orgAdd'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'parentId': parentId}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 组织机构机构修改接口40
    def testPersonOrgedit(self, departmentId, parentId, name):
        url = self.host + '/manage/person/orgEdit'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'departmentId': departmentId, 'parentId': parentId, 'name': name}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 组织机构机构删除接口41,ID是列表
    def testPersonOrgdel(self, ID):
        url = self.host + '/manage/person/orgDel'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = ID
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 站点管理站点列表接口42
    def testSitelist(self, pageNo, pageSize, type, name):
        url = self.host + '/manage/data/siteList/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'pageNo': pageNo, 'pageSize': pageSize, 'type': type, 'name': name}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 站点禁用或者启用接口43
    def testSitelistEnable(self, sid, status):
        url = self.host + '/manage/data/siteList/enable'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'sid': sid, 'status': status}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 站点管理站点详情接口44
    def testSitelistInfo(self, sid):
        url = self.host + '/manage/data/siteList/info'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'sid': sid}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 站点历史数据接口45
    def testSitelistHistory(self, sid, time):
        url = self.host + '/manage/data/siteList/history'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'sid': sid, 'time': time}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 监测项目列表接口46
    def testProjectlist(self, name, type, pageNo, pageSize):
        url = self.host + '/manage/project/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'type': type, 'pageNo': pageNo, 'pageSize': pageSize}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 监测项目新增接口47
    def testProjectadd(self, projectName, areasCodes, stress, projectType, projectProfile, projectImages, loc,
                       contactsId, sites, monitorIds):
        url = self.host + '/manage/project/add'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'projectName': projectName, 'areasCodes': areasCodes, 'stress': stress, 'projectType': projectType,
                 'projectProfile': projectProfile, 'projectImages': projectImages, 'loc': loc, 'contactsId': contactsId,
                 'sites': sites, 'monitorIds': monitorIds}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 监测项目编辑接口48
    def testProjectedit(self, projectId, areasCodes, stress, projectName, projectType, projectProfile, projectImages,
                        loc, contactsId, sites, monitorIds):
        url = self.host + '/manage/project/edit'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'projectId': projectId, 'projectName': projectName, 'areasCodes': areasCodes, 'stress': stress,
                 'projectType': projectType,
                 'projectProfile': projectProfile, 'projectImages': projectImages, 'loc': loc, 'contactsId': contactsId,
                 'sites': sites, 'monitorIds': monitorIds}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 监测项目详情接口49
    def testProjectinfo(self, projectId):
        url = self.host + '/manage/project/info'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'projectId': projectId}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 监测项目删除接口50
    def testProjectdel(self, serverurl):
        url = self.host + '/manage/project/del'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'serverurl': serverurl}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 发布终端管理添加接口51
    def testMachineadd(self, expiredTime, name, serial, type, remark):
        url = self.host + '/manage/machine/add'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'expiredTime': expiredTime, 'name': name, 'serial': serial, 'type': type, 'remark': remark}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 发布终端管理修改接口52
    def testMachineEdit(self, expiredTime, name, serial, type, remark, machineId):
        url = self.host + '/manage/machine/edit'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'expiredTime': expiredTime, 'name': name, 'serial': serial, 'type': type, 'remark': remark,
                 'machineId': machineId}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 发布终端管理删除接口53,ids是列表
    def testMachinedel(self, ids):
        url = self.host + '/manage/machine/del'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = ids
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 发布终端管理列表接口54
    def testMachinelist(self, name, type, time, status, pageNo, pageSize):
        url = self.host + '/manage/machine/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'type': type, 'time': time, 'status': status, 'pageNo': pageNo, 'pageSize': pageSize}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 角色管理--角色列表接口
    def testRolelist(self, name, pageNo, pageSize):
        url = self.host + '/manage/role/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'pageNo': pageNo, 'pageSize': pageSize}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 角色管理-角色删除接口
    def testRoledel(self, ids):
        url = self.host + '/manage/role/del'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'ids': ids}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 角色管理--角色添加接口,datas是json格式传参(该接口虽然角色添加成功，但是datas返回为空，没有具体的权限)
    def testRoleadd(self, datas):
        url = self.host + '/manage/role/add'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token, 'Content-Type': 'application/json'}
        # datas = {'name':name,'menus':menus,'funs':funs,'describe':describe}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 角色管理--角色编辑
    def testRoleEdit(self, roleId, name, menus, funs, describe):
        url = self.host + '/manage/role/edit'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'roleId': roleId, 'name': name, 'menus': menus, 'funs': funs, 'describe': describe}
        r = requests.post(url, headers=header, data=datas)
        message = r.text
        print(message)
        return message

    # 地图数据接口
    # 重点监测项目列表接口55
    def testScreenProjectlist(self, type, areas):
        url = self.host + '/screen/project/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'type': type, 'areas': areas}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 重点监测项目类型列表接口56
    def testScreenProjectTypelist(self, serverurl):
        url = self.host + '/screen/project/projectTypeList'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'serverurl': serverurl}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 监测项目详情接口57
    def testScreenProjectInfo(self, projectId):
        url = self.host + 'screen/project/info'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'projectId': projectId}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 监测站点列表接口58
    def testScreenSitelist(self, type, areas):
        url = self.host + '/screen/stie/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'type': type, 'areas': areas}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 监测站点类型列表接口59
    def testScreenSiteTypelist(self, serverurl):
        url = self.host + '/screen/stie/typeList'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'serverurl': serverurl}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 基础信息列表接口60
    def testScreenBasiclist(self, type, areas):
        url = self.host + '/screen/basic/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'type': type, 'areas': areas}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 基础类型列表接口61
    def testScreenBasicTypelist(self, serverurl):
        url = self.host + '/screen/basic/typeList'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'serverurl': serverurl}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 实时数据接口62
    def testScreenRealtimedata(self, time, fieId):
        url = self.host + '/screen/realtime/pointData'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'time': time, 'fieId': fieId}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 天气接口
    # 根据经纬度查询当前天气数据
    def testWeathernow(self, lng, lat):
        url = self.host + '/weather/now'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'lng': lng, 'lat': lat}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 逐小时预报
    def testScreenlocalForecast(self, lng, lat):
        url = self.host + '/screen/localForecast'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'lng': lng, 'lat': lat}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 关联项目
    def testMobileProjectlist(self, name, type, pageNo, pageSize):
        url = self.host + '/mobile/project/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'name': name, 'type': type, 'pageNo': pageNo, 'pageSize': pageSize}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 根据经纬度获取风速风向
    def testLocalForecast_meta(self, lng, lat):
        url = self.host + '/screen/localForecast_meta'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'lng': lng, 'lat': lat}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 根据经纬度查询当前天气数据,青羊区=510106
    def testScreenNow(self, lng, lat, areaCode):
        url = self.host + '/screen/now'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'lng': lng, 'lat': lat, 'areaCode': areaCode}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message

    # 根据经纬度查询15天预报, areaCode
    def testScreenFifthdays(self, lng, lat):
        url = self.host + '/screen/fifthDays'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'lng': lng, 'lat': lat}
        r = requests.get(url, headers=header, params=datas)
        message = r.text
        print(message)
        return message
