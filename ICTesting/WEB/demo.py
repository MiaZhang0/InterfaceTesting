import requests

class TestModuleClass():
    def __init__(self):
        self.host = 'http://192.168.0.234:8099'

    def testLogin(self, username, password):
        url = self.host + '/login'
        datas = {'username': username, 'password': password}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
    def testMsg(self):
        url = self.host + '/manage/activitiesMsg/list'
        
TestModuleClass().testLogin('zhangxiaomei1','123456')
