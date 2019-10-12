from APP import testModule_APP
import time

t = testModule_APP.TestModuleClass()
#添加参与人
# t.testDcaseAddParticipants('','')
# t.testDcaseAddParticipants('103','34,35')
# t.testDcaseAddParticipants('103',[39,40])
#通过险情ID获取受灾情况
# t.testDcaseGetCaseDisaster(1)
# # t.testDcaseGetCaseDisaster('')
# 上报险情受灾情况
# t.testDcaseUpdateCaseDisaster('','')
# t.testDcaseUpdateCaseDisaster('1','2')
#通过灾害类型ID获取受灾类型
# t.testDcaseGetCaseDisasterType('')
# t.testDcaseGetCaseDisasterType('1')
#获取所有的灾害类型
# t.testDcaseGetCaseType()
#通过行业类型ID获取受灾类型【行业id目前是1-10,从0开始】
# t.testDcaseDisasterType('')
#删除参与人
# t.testDcaseDelParticipants('103',42)
# t.testDcaseDelParticipants('103','42')
# t.testDcaseDelParticipants('103',[42])
# t.testDcaseDelParticipants('1','1')
# t.testDcaseDelParticipants('','')
# t.testDcaseDelParticipants('103','31,32')
# t.testDcaseDelParticipants('103',[31,33])
#获取参与人【险情id目前1-80】
# t.testDcaseGetParticipants('','',1,20)
#险情-列表
# t.testDcaseWarningList('','','','','')
#修改负责人
# t.testDcaseAddChatge('72','35')
#上报险情
# 无效的地址、无效纬度、无效经度、无效的灾害类型、无效的参数，无效的内容
# t.testDcaseAdd('三九大桥雨城区',29.58,103.0,4,'511800','testtesttest','/uploads/20190925/6ac4875daf833164282a5311f2fcbd91.jpeg','')
# t.testDcaseAdd('三九大桥雨城区',29.58,103.0,6,'511800','','','')
#险情新增配置
# t.testGetReportConfig('')

# t.testDcaseImgSending(72,'/uploads/20190925/6ac4875daf833164282a5311f2fcbd91.jpeg,/uploads/20190924/a3a43377d2a7d95bf0da6b3038513a25.jpg')
# t.testDcaseImgSending('','')

# t.testDcaseTextSending(82,'hahahahhahahaha')
# t.testDcaseTextSending('','')

# t.testDcaseDangerousCase('','')

# t.testDcaseDetails('')

# t.testDcaseXmt(82,7,1,'1','123eeee','755)eeee')
# 无效的险情,无效的接受人,请选择发送类型,标题格式错误,内容格式错误,无效推送方式
# t.testDcaseXmt(82,7,1,'1',1234,1234)

# t.testInspectingWarningList('','','','')

# t.testInspectingDetails('')
# t.testInspectingDetails('19')
# date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# t.testInspectingAdd('雅安站姚桥镇北环东路',1,30.028493,103.056953,'511800','11111111111','','','')
#无效纬度,无效经度,无效的时间,info不能为空,无效的状态,无效的参数
# t.testInspectingAdd('',1,30.028493,103.056953,'511800','trt',date,'','')
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# t.testOrganizationZuzhi()
# t.testOrganizationRecentContacts()
# t.testOrganizationZuzhiJiagou()
# t.testOrganizationSearch('2','','')
# t.testOrganizationUserDetails('')
# t.testCommonScreen('')
# t.testCommonCheckVersion('iOS','','29')
# t.testCommonDeviceTokens('Android','Akwhy5G4cGVMW9NoGMRfoXbexHuYv0j16fXT8cM2ktmw')
# t.testCommonDeviceTokens('','')

# 批量上传照片，上传文件
# path = r'G:\Kedalo\Testing\APP\1.png'
# with open(path,'rb') as f1:
#     file0 = f1.read()
#     t.testCommonBatchUpload(file0)
# t.testCommonUpload('')
# t.testCommonSetloc('','')
# t.testCommonSetloc(103.0,29.58)
# t.testCommonNumMsg()
# t.testHomepageIndex(103.0,29.58)
# t.testHomepageIndex('','')
# t.testHomepageIndexAll('','')
# t.testHomepageIndexAll(103.0,29.58)
# t.testHomepageIndecIcon()
# t.testHomepageIndexNotify()
# t.testMstationsFocusSites('','')
# t.testMstationsTableType('10',2,'')
# t.testMstationsTableType('10',2,'weather')
# t.testMstationsTableType('','','')
# t.testMstationsGetSiteBasics('','')
# t.testMstationsGetSiteBasics('10',2)

# t.testMstationsGetSiteStatistics('','')
# t.testMstationsGetSiteStatistics('10',2)
# t.testMstationsGetMajor('','')
# t.testMstationsGetMajor('10',2)

# t.testH5WeatherWind()
# t.testH5WeatherThunder()
# t.testH5WeatherSite()
# t.testH5WeatherWarning()
# t.testH5Weather()
# t.testH5WeatherCase('')
# t.testH5WeatherJiance('')
# t.testH5WeatherMaterial()
# t.testH5WeatherInspecting(10)
# t.testH5WeatherInspecting('')
# t.testH5WeatherCased(86)
# t.testH5WeatherCased('')
# t.testH5WeatherUser()
# t.testH5WeatherNavigation()
# t.testWeather('','')
# t.testWeather(29.58,103.0)
# t.testWeatherEarlyWarning(29.58,103.0)
# t.testWeatherEarlyWarning('','')
# t.testWeatherKQ(103.0,29.58)
# t.testWeatherKQ('','')
# t.testHelpList('','')
# t.testHelpDetails('')
# t.testHelpDetails(11)
# t.testCaseList('','','','','')
# t.testMessageNotice('','','')
# t.testMessageNoticeDetails('','',1)
# t.testMessageNoticeDetails('','','')
# t.testMessageDetails(1)
# t.testMessageDetails('')
# t.testMessageDelMsg('')
t.testMessageDelMsg(3)
# t.testWorkbench()
