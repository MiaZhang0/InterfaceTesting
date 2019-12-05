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
    #登录
    def testLoginModule(self,username,pwd):
        url = self.host + '/api/v1/login/login'
        datas = {'username':username,'password':pwd}
        r = requests.post(url,data=datas)
        message = r.text
        #只有登录成功才会返回token值
        if '登录成功' in message:
            token = r.json()['data']['userinfo']['token']
            return message,token
        else:
            return message
     #退出登录
    def testLogoutModule(self):
        url = self.host + '/api/v1/login/logout'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        # print(header)
        r = requests.post(url,headers=header)
        message = r.text
        # print(message)
        return message
    #身份验证-发送短信
    def testSendMobile(self,mobile):
        url = self.host + '/api/v1/login/sendMobile'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        # print(header)
        datas = {'mobile':mobile}
        r = requests.post(url, data=datas,headers=header)
        message = r.text
        # print(message)
        return message
    #通过手机号码验证
    def testVerifyPhone(self,mobile,captcha):
        url = self.host + '/api/v1/login/verify_phone'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        # print(header)
        datas = {'mobile': mobile,'captcha':captcha}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #重置密码
    def testResetPwd(self,ptoken,new_pwd):
        url = self.host + '/api/v1/login/resetPassword'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'token':ptoken,'newPwd':new_pwd}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #修改密码
    def testChangePwd(self,ptoken,old_pwd,new_pwd):
        url = self.host + '/api/v1/login/changePassword'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'token': ptoken, 'oldPwd':old_pwd,'newPwd': new_pwd}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    # 综合预警行业图标
    def testZhyjIndustryModule(self):
        url = self.host + '/api/v1/zhyj/industry'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        # print(header)
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #搜索站点、险情、监测点
    def testZhyjSearch(self,keyword):
        url = self.host + '/api/v1/zhyj/search'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'keywords':keyword}
        r = requests.post(url,data=datas,headers=header)
        message = r.text
        # print(message)
        return message
    #综合页面天气实况
    def testZhyjWeather(self,lng,lat):
        url = self.host + '/api/v1/zhyj/weather'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'lng':lng,'lat':lat}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #险情-统计
    def testDcaseStatistics(self,keywords,filter):
        url = self.host + '/api/v1/dcase/statistics'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'keywords': keywords,'filter':filter}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #添加参与人
    def testDcaseAddParticipants(self,id,user_id):
        url = self.host + '/api/v1/dcase/addParticipants'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id':id,'user_ids':user_id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #通过险情ID获取受灾情况
    def testDcaseGetCaseDisaster(self,id):
        url = self.host + '/api/v1/dcase/getCaseDisaster'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    # 上报险情受灾情况
    def testDcaseUpdateCaseDisaster(self,id,disaster):
        url = self.host + '/api/v1/dcase/UpdateCaseDisaster'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id,'disaster':disaster}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #通过灾害类型ID获取受灾类型
    def testDcaseGetCaseDisasterType(self,caseTypeld):
        url = self.host + '/api/v1/dcase/getCaseDisasterType'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'caseTypeId':caseTypeld}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #获取所有的灾害类型
    def testDcaseGetCaseType(self):
        url = self.host + '/api/v1/dcase/getCaseType'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #通过行业类型ID获取受灾类型【行业id目前是1-10】
    def testDcaseDisasterType(self,industry_id):
        url = self.host + '/api/v1/dcase/disasterType'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'industry_id':industry_id}
        r = requests.post(url, data=datas,headers=header)
        message = r.text
        # print(message)
        return message
    #删除参与人
    def testDcaseDelParticipants(self,id,user_id):
        url = self.host + '/api/v1/dcase/delParticipants'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id':id,'user_ids':user_id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #获取参与人【险情id目前1-80】
    def testDcaseGetParticipants(self,id,keywords,page,pageSize):
        url = self.host + '/api/v1/dcase/getParticipants'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id, 'keywords': keywords,'page':page,'pageSize':pageSize}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #险情-列表
    def testDcaseWarningList(self,keywords,filter,page,pageSize,status):
        url = self.host + '/api/v1/dcase/warningList'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'keywords':keywords,'filter':filter,'page':page,'pageSize':pageSize,'status':status}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #修改负责人
    def testDcaseAddChatge(self,id,user_id):
        url = self.host + '/api/v1/dcase/addCharge'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id':id,'user_id':user_id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #上报险情
    def testDcaseAdd(self,address,lat,lng,case_type,adcode,info,imgs,disaster):
        url = self.host + '/api/v1/dcase/add'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'address':address,'lat':lat,'lng':lng,'case_type':case_type,'adcode':adcode,'info':info,'imgs':imgs,'disaster':disaster}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #险情新增配置
    def testGetReportConfig(self,id):
        url = self.host + '/api/v1/dcase/getReportConfig'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id':id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #险情发送图片
    def testDcaseImgSending(self,id,imgs):
        url = self.host + '/api/v1/dcase/imgSending'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id,'imgs':imgs}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #险情发送文字
    def testDcaseTextSending(self,id,info):
        url = self.host + '/api/v1/dcase/textSending'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id':id,'info':info}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #险情处理
    def testDcaseDangerousCase(self,id,type):
        url = self.host + '/api/v1/dcase/dangerousCase'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id':id,'type':type}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #险情-详情
    def testDcaseDetails(self,id):
        url = self.host + '/api/v1/dcase/details'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #大屏险情处置发送指令
    def testDcaseXmt(self,id,uid,sendType,sendMode,sendTitle,sendContent):
        url = self.host + '/api/v1/dcase/xmt'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id,'uid':uid,'sendType':sendType,'sendMode':sendMode,'sendTitle':sendTitle,'sendContent':sendContent}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #【巡检】列表
    def testInspectingWarningList(self,keywords,filter,page,pageSize):
        url = self.host + '/api/v1/inspecting/warningList'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'keywords':keywords,'filter':filter,'page':page,'pageSize':pageSize}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #【巡检】详情-经纬度需要返给h5做点位标记
    def testInspectingDetails(self,id):
        url = self.host + '/api/v1/inspecting/details'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id':id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #添加巡检
    def testInspectingAdd(self,address,status,lat,lng,adcode,info,date,cc,images):
        url = self.host + '/api/v1/inspecting/add'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'address':address,'status':status,'lat':lat,'lng':lng,'adcode':adcode,'info':info,'date':date,'cc':cc,'images':images}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #组织架构
    def testOrganizationZuzhi(self):
        url = self.host + '/api/v1/organization/zuZhi'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #最近联系人
    def testOrganizationRecentContacts(self):
        url = self.host + '/api/v1/organization/recentContacts'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #组织架构
    def testOrganizationZuzhiJiagou(self):
        url = self.host + '/api/v1/organization/zuZhiJiaGou'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #组织架构所有用户
    def testOrganizationZuzhiDetails(self,group_id,page,pageSize):
        url = self.host + '/api/v1/organization/zuZhiJiaGouDetails'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'group_id':group_id,'page':page,'pageSize':pageSize}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #搜索所有用户
    def testOrganizationSearch(self,keywords,page,pageSize):
        url = self.host + '/api/v1/organization/search'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'keywords':keywords,'page':page,'pageSize':pageSize}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #用户详情
    def testOrganizationUserDetails(self,id):
        url = self.host + '/api/v1/organization/UserDetails'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id':id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #险情筛选条件
    def testCommonScreen(self,action):
        url = self.host + '/api/v1/common/screen'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'action':action}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #检测版本，通过头部客户端版本判断【client填天e行，或者】
    def testCommonCheckVersion(self,platform,client,sequence):
        url = self.host + '/api/v1/common/checkVersion'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'platform':platform,'client':client,'sequence':sequence}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #添加用户device_tokens
    def testCommonDeviceTokens(self,platform,deviceTokens):
        url = self.host + '/api/v1/common/deviceTokens'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token,'platform':platform}
        datas = {'deviceTokens':deviceTokens}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #批量上传0-9照片
    def testCommonBatchUpload(self,file0):
        url = self.host + '/api/v1/common/batchUpload'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'file0':file0}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    # 上传文件
    def testCommonUpload(self,file):
        url = self.host + '/api/v1/common/upload'
        token = getLoginToken()
        # payload = {'action': 'storeFile'}
        header = {'Authorization': 'Bearer ' + token,'content-type':'application/json'}
        # header = {'Authorization': 'Bearer ' + token}
        files = {'file': file}
        r = requests.post(url, headers=header,files=files)
        message = r.text
        # print(message)
        return message
    #上传用户经纬度
    def testCommonSetloc(self,lng,lat):
        url = self.host + '/api/v1/common/setloc'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'lng':lng,'lat':lat}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #未读消息数量
    def testCommonNumMsg(self):
        url = self.host + '/api/v1/common/numMsg'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #天气主要概况
    def testHomepageIndex(self,lng,lat):
        url = self.host + '/api/v1/index/index'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'lng': lng, 'lat': lat}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #首页-全部,传递数据参考各分接口
    def testHomepageIndexAll(self,lng,lat):
        url = self.host + '/api/v1/index/indexAll'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'lng': lng, 'lat': lat}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #【首页】首页-图标
    def testHomepageIndecIcon(self):
        url = self.host + '/api/v1/index/indexIcon'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #【首页】通知，如果没有通知，则不显示
    def testHomepageIndexNotify(self):
        url = self.host + '/api/v1/index/notify'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #【首页】关注站点
    def testMstationsFocusSites(self,page,pageSize):
        url = self.host + '/api/v1/mstations/focusSites'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'page':page,'pageSize':pageSize}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #监测站点头部动态切换栏
    def testMstationsTableType(self,id,industry_id,type):
        url = self.host + '/api/v1/mstations/tableType'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id':id,'industry_id':industry_id,'type':type}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #站点信息
    def testMstationsGetSiteBasics(self,id,industry_id):
        url = self.host + '/api/v1/mstations/getSiteBasics'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id':id,'industry_id':industry_id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #气象
    def testMstationsGetSiteStatistics(self,id,industry_id):
        url = self.host + '/api/v1/mstations/getSiteStatistics'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id, 'industry_id': industry_id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #监测数据
    def testMstationsGetMajor(self,id,industry_id):
        url = self.host + '/api/v1/mstations/getMajor'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id, 'industry_id': industry_id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #风场格点
    def testH5WeatherWind(self):
        url = self.host + '/api/v1/h5weather/wind'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #当前页面交互，点击显示雷电强度
    def testH5WeatherThunder(self):
        url = self.host + '/api/v1/h5weather/thunder'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #站点【与APP交互】
    # def testH5WeatherSite(self):
    #     url = self.host + '/api/v1/h5weather/site'
    #     token = getLoginToken()
    #     header = {'Authorization': 'Bearer ' + token}
    #     r = requests.post(url, headers=header)
    #     message = r.json()
    #     print(message)
    #     # return message
    #预警【与APP交互】
    def testH5WeatherWarning(self):
        url = self.host + '/api/v1/h5weather/alarm'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #当前页面交互，点击显示质量详细指数
    def testH5Weather(self):
        url = self.host  + '/api/v1/h5weather/aqi'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #险情点位-闪动【与APP交互】
    def testH5WeatherCase(self,industry_id):
        url = self.host + '/api/v1/h5weather/case'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'industry_id': industry_id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    # 监测点位【与APP交互】
    def testH5WeatherJiance(self,industry_id):
        url = self.host + '/api/v1/h5weather/jiance'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'industry_id': industry_id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #物资监测点
    def testH5WeatherMaterial(self):
        url = self.host + '/api/v1/h5weather/material'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #巡检
    def testH5WeatherInspecting(self,id):
        url = self.host + '/api/v1/h5weather/Inspecting'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #险情
    def testH5WeatherCased(self,id):
        url = self.host + '/api/v1/h5weather/cased'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #人员
    def testH5WeatherUser(self):
        url = self.host + '/api/v1/h5weather/renyuan'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #指定规划路径
    def testH5WeatherNavigation(self):
        url = self.host + '/api/v1/h5weather/navigation'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message
    #多个经纬度通过温度
    # def testWeatherTmp(self,loc):
    #     url = self.host + '/api/v1/weather/tmp'
    #     token = getLoginToken()
    #     header = {'Authorization': 'Bearer ' + token}
    #     loc = ['lng','lat','uid'] #loc是一个数组
    #     r = requests.post(url, headers=header)
    #     message = r.text
    #     # print(message)
    #     return message
    #多个经纬度通过降水；若无标识信息返回
    # def testWeatherWindPr(self,path_planning,date):
    #     url = self.host + '/api/v1/weather/windPr'
    #     token = getLoginToken()
    #     header = {'Authorization': 'Bearer ' + token}
    #     path_planning = [] #s数组
    #     date = '' #date数据类型
    #     r = requests.post(url, headers=header)
    #     message = r.text
    #     # print(message)
    #     return message
    #通过经纬度获取目的天气情况
    def testWeather(self,lat,lng):
        url = self.host + '/api/v1/weather/toWeather'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'lat':lat,'lng':lng}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #通过经纬度查询前方天气情况
    def testWeatherEarlyWarning(self,lat,lng):
        url = self.host + '/api/v1/weather/earlyWarning'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'lat': lat, 'lng': lng}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #天气主要概况【APP考勤】
    def testWeatherKQ(self,lng,lat):
        url = self.host + '/api/v1/weather/kqWeather'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'lat': lat, 'lng': lng}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #帮助中心-列表
    def testHelpList(self,page,pageSize):
        url = self.host + '/api/v1/help/list'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'page': page, 'pageSize': pageSize}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #帮助中心-详情[id范围4-15]
    def testHelpDetails(self,id):
        url = self.host + '/api/v1/help/details'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #ING险情-列表
    def testCaseList(self,keywords,filter,page,pageSize,status):
        url = self.host + '/api/v1/ing/caseList'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'keywords':keywords,'filter':filter,'page':page,'pageSize':pageSize,'status':status}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #【通知】通知列表
    def testMessageNotice(self,keywords,page,pageSize):
        url = self.host + '/api/v1/message/notice'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'keywords': keywords, 'page': page, 'pageSize': pageSize}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #【通知】类型详情
    def testMessageNoticeDetails(self,page,pageSize,id):
        url = self.host + '/api/v1/message/noticeDetails'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'page': page, 'pageSize': pageSize, 'id': id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #【new】通知-详情，自动阅读
    def testMessageDetails(self,id):
        url = self.host + '/api/v1/message/details'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #通知-删除
    def testMessageDelMsg(self,id):
        url = self.host + '/api/v1/message/delMsg'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        datas = {'id': id}
        r = requests.post(url, data=datas, headers=header)
        message = r.text
        # print(message)
        return message
    #工作台
    def testWorkbench(self):
        url = self.host + '/api/v1/workbench/activeLayer'
        token = getLoginToken()
        header = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=header)
        message = r.text
        # print(message)
        return message

# # TestModuleClass().testDcas/api/v1/dcase/addeStatistics('','{"child":[{"key":"2"},{"key":"6"}],"key":"industry"}')  ?
