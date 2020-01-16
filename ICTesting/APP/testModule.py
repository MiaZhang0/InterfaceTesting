import requests

class TestModuleClass():
    def __init__(self):
        self.host = 'http://192.168.0.234:8099'
    #发送手机验证码
    def testSendCode(self,phone):
        url = self.host + '/appSendCode'
        datas = {'phone':phone}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #短信登录
    def testLogin(self,phone,code):
        url = self.host + '/appLogin'
        datas = {'phone':phone,'code':code}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #选择，切换小区
    def testSelectArea(self,phone,areaId):
        url = self.host + '/selectArea'
        datas = {'phone':phone,'areaId':areaId}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #轮播列表
    def testBannerList(self):
        url = self.host + '/mobile/home/bannerList'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #公告列表
    def testNoticeList(self,types):
        url = self.host + '/mobile/home/bulletinList'
        datas = {'types':types}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #资讯列表
    def testNewsList(self,pageNo,pageSize,typeId):
        url = self.host + '/mobile/home/newsList'
        datas = {'pageNo':pageNo,'pageSize':pageSize,'typeId':typeId}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #社区信息
    def testCommunityInfo(self):
        url = self.host + '/mobile/home/communityInfo'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #小区信息
    def testAreaInfo(self):
        url = self.host + '/mobile/home/areaInfo'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #公告详情
    def testNoticeInfo(self,bulletinId):
        url = self.host + '/mobile/home/bulletinInfo'
        datas = {'bulletinId':bulletinId}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #资讯详情
    def testNewsInfo(self,newsId):
        url = self.host + '/mobile/home/newsInfo'
        datas = {'newsId':newsId}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #点赞或者取消点赞
    def testThumbUp(self,newsId,type):
        url = self.host + '/mobile/news/thumbUp'
        datas = {'newsId':newsId,'type':type}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #收藏或者取消收藏
    def testNewsCollect(self,newsId,type):
        url = self.host + '/mobile/news/collect'
        datas = {'newsId':newsId,'type':type}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #个人信息
    def testPersonalInfo(self):
        url = self.host + '/mobile/personal/personalInfo'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #足迹，收藏，点赞列表
    def testPersonalList(self,pageNo,pageSize,type):
        url = self.host + '/mobile/personal/list'
        datas = {'pageNo':pageNo,'pageSize':pageSize,'type':type}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #修改个人信息
    def testPersonalEdit(self,nickname,gender,headlamge,username,password,idCard,phone):
        url = self.host + '/mobile/personal/edit'
        datas = {'nickname':nickname,'gender':gender,'headlamge':headlamge,'username':username,'password':password,'idCard':idCard,'phone':phone}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message