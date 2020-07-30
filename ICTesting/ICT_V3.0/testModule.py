import requests

def getLoginToken():
    message = TestModuleClass().testLoginModule('zxm', 'Kk123456', '2')
    token = message['data']['token']
    print(token)
    return token

class TestModuleClass():
    def __init__(self):
        self.host = 'https://photo.kedalo.com:8887'
    # 登录接口1, 0:PC 1:IOS 2:android
    def testLoginModule(self, username, pwd, platform):
        url = self.host + '/login'
        datas = {'username': username, 'password': pwd, 'platform': platform}
        r = requests.post(url, data=datas)
        message = r.json()
        # print(message)
        return message
    # 监控列表
    def testMobileMonitorList(self,pageNo,pageSize):
        url = self.host + '/mobile/monitor/list'
        token = getLoginToken()
        header = {'Cookie': 'SESSION=' + token}
        datas = {'pageNo': pageNo, 'pageSize': pageSize}
        r = requests.get(url, headers=header, params=datas)
        message = r.json()
        print(message)
        return message
obj = TestModuleClass()
obj.testMobileMonitorList('1','20')