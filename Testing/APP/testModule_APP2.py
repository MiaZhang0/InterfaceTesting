import requests

# 获取登录token
def getLoginToken():
    res = TestModuleClass().testLoginModule('15108307817', 'Kk1234')
    # print(res)
    token = res[1]
    # print(token)
    return token
#API模块类
class TestModuleClass():
    def __init__(self):
        self.host = 'https://yaan.kedalo.com'
    # 登录
    def testLoginModule(self, username, pwd):
        url = self.host + '/api/v1/login/login'
        datas = {'username': username, 'password': pwd}
        r = requests.post(url, data=datas)
        message = r.text
        # 只有登录成功才会返回token值
        if '登录成功' in message:
            token = r.json()['data']['userinfo']['token']
            return message, token
        else:
            return message
    #首页-天气
    def testHomepageWeather(self,lng,lat):
        url = self.host + '/api/v1/index/indexAllNew'
        datas = {'lng':lng,'lat':lat}
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, data=datas,headers=header)
        message = r.text
        # print(message)
        return message
    #告警列表
    def testAlarmInfo(self,page,pageSize):
        url = self.host + '/api/v1/Alarm/giveAnAlarmInfo'
        datas = {'page':page,'pageSize':pageSize}
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #告警详情
    def testAlarmDetail(self,id):
        url = self.host + '/api/v1/Alarm/giveAnAlarm'
        datas = {'id':id}
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #预警列表
    def testWarningList(self,page,pageSize,lvl,filter):
        url = self.host + '/api/v1/Alarm/warningList'
        datas = {'page':page,'pageSize':pageSize,'lvl':lvl,'filter':filter}
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #预警统计
    def testWarningStatistics(self,filter):
        url = self.host + '/api/v1/Alarm/warningStatisticsNew'
        datas = {'filter':filter}
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #险情列表
    def testDcaseList(self,filter,keywords,page,pageSize,status):
        url = self.host + '/api/v1/Dcase/warningList'
        datas = {'filter':filter,'keywords':keywords,'page':page,'pageSize':pageSize,'status':status}
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #险情统计
    def testDcaseStatistics(self,filter,keywords):
        url = self.host + '/api/v1/Dcase/statisticsNew'
        datas = {'filter':filter,'keywords':keywords}
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #项目列表
    def testMonitorList(self,keywords,page,pageSize):
        url = self.host + '/api/v1/Monitor/monitorListNew'
        datas = {'keywords':keywords,'page':page,'pageSize':pageSize}
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #项目统计
    def testMonitorStatistics(self):
        url = self.host + '/api/v1/Monitor/statistics'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url,headers=header)
        message = r.text
        # print(message)
        return message
    #未读消息
    def testCommonMsg(self):
        url = self.host + '/api/v1/common/numMsg'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        print(message)
        return message