import unittest
from unittest import TestCase
from APP import testModule_APP
import time

class TestClass(TestCase):
    def setUp(self):
        self.t = testModule_APP.TestModuleClass()
    #登录
    def test_login_success(self):
        message = self.t.testLoginModule('15108307817', 'Kk12345')
        self.assertIn('登录成功',message[0],'test_login_success_001测试失败。')
    def test_login_fail01(self):
        message = self.t.testLoginModule('','')
        self.assertIn('手机号码错误，请重新输⼊！',message,'test_login_fail01_002测试失败。')
    def test_login_fail02(self):
        message = self.t.testLoginModule('15108307817','1')
        self.assertIn('密码错误，请重新输⼊！', message, 'test_login_fail02_003测试失败。')
    # 退出登录
    def test_logout_success(self):
        message = self.t.testLogoutModule()
        self.assertIn('success',message,'test_logout_success_004测试失败。')
    # 综合预警行业图标
    def test_zhyjIndustry_success(self):
        message = self.t.testZhyjIndustryModule()
        self.assertIn('success',message,'test_zhyjIndustry_success_005测试失败。')
    # 搜索站点、险情、监测点
    def test_zhyjSearch_success(self):
        message = self.t.testZhyjSearch('水')
        self.assertIn('success',message,'test_zhyjSearch_success_006测试失败。')
    def test_zhyjSearch_fail(self):
        message = self.t.testZhyjSearch('')
        self.assertIn('无效的参数',message,'test_zhyjSearch_fail_007测试失败。')
    # 综合页面天气实况
    def test_zhyjWeather_success(self):
        message = self.t.testZhyjWeather(103.0,30.3)
        self.assertIn('success',message,'test_zhyjWeather_success_008测试失败。')
    def test_zhyjWeather_fail01(self):
        message = self.t.testZhyjWeather('','')
        self.assertIn('无效纬度',message,'test_zhyjWeather_fail01_009测试失败。')
    def test_zhyjWeather_fail02(self):
        message = self.t.testZhyjWeather('','30.3')
        self.assertIn('无效经度',message,'test_zhyjWeather_fail02_010测试失败。')
    # 险情-统计
    def test_dcaseStatistics_success(self):
        message = self.t.testDcaseStatistics('','')
        self.assertIn('success',message,'test_dcaseStatistics_success_011测试失败。')
    # 添加参与人
    def test_dcaseAddParticipants_fail01(self):
        message = self.t.testDcaseAddParticipants('1',[1,2])
        self.assertIn('修改参与人失败',message,'test_dcaseAddParticipants_fail01_012测试失败。')
    def test_dcaseAddParticipants_fail02(self):
        message = self.t.testDcaseAddParticipants('','')
        self.assertIn('无效的参数', message, 'test_dcaseAddParticipants_fail02_013测试失败。')
    def test_dcaseAddParticipants_success(self):
        message = self.t.testDcaseAddParticipants('1','37,38')
        self.assertIn('添加人成功',message,'test_dcaseAddParticipants_success_014测试失败。')
    # 通过险情ID获取受灾情况
    def test_dcaseGetCaseDisaster_success(self):
        message = self.t.testDcaseGetCaseDisaster(1)
        self.assertIn('success',message,'test_dcaseGetCaseDisaster_success_015测试失败。')
    def test_dcaseGetCaseDisaster_fail(self):
        message = self.t.testDcaseGetCaseDisaster('')
        self.assertIn('无效的险情', message, 'test_dcaseGetCaseDisaster_fail_016测试失败。')
    # 上报险情受灾情况
    def test_dcaseUpdateCaseDisaster_success(self):
        message = self.t.testDcaseUpdateCaseDisaster('1','2')
        self.assertIn('更新险情受损成功',message,'test_dcaseUpdateCaseDisaster_success_017测试失败。')
    def test_dcaseUpdateCaseDisaster_fail(self):
        message = self.t.testDcaseUpdateCaseDisaster('','')
        self.assertIn('无效的参数',message,'test_dcaseUpdateCaseDisaster_fail_018测试失败。')
    #通过灾害类型ID获取受灾类型【id 范围1-42】
    def test_dcaseGetCaseDisasterType_success(self):
        message = self.t.testDcaseGetCaseDisasterType('1')
        self.assertIn('success',message,'test_dcaseGetCaseDisasterType_success_019测试失败')
    def test_dcaseGetCaseDisasterType_fail(self):
        message = self.t.testDcaseGetCaseDisasterType('')
        self.assertIn('无效的灾害类型',message,'test_dcaseGetCaseDisasterType_fail_020测试失败。')
    # 获取所有的灾害类型
    def test_dcaseGetCaseType_success(self):
        message = self.t.testDcaseGetCaseType()
        self.assertIn('success',message,'test_dcaseGetCaseType_success_021测试失败。')
    # 通过行业类型ID获取受灾类型
    def test_dcaseDisasterType_success(self):
        message = self.t.testDcaseDisasterType('1')
        self.assertIn('success',message,'test_dcaseDisasterType_success_022测试失败。')
    def test_dcaseDisasterType_fail(self):
        message = self.t.testDcaseDisasterType('')
        self.assertIn('无效的类型',message,'test_dcaseDisasterType_fail_023测试失败。')
    # 删除参与人
    def test_dcaseDelParticipants_success(self):
        message = self.t.testDcaseDelParticipants('1','31')
        self.assertIn('success',message,'test_dcaseDelParticipants_success_024测试失败。')
    def test_dcaseDelParticipants_fail(self):
        message = self.t.testDcaseDelParticipants('','')
        self.assertIn('无效的参数',message,'test_dcaseDelParticipants_fail_025测试失败。')
    #获取参与人
    def test_dcaseGetParticipants_success(self):
        message = self.t.testDcaseGetParticipants('76','','','')
        self.assertIn('success',message,'test_dcaseGetParticipants_success_026测试失败。')
    def test_dcaseGetParticipants_fail(self):
        message = self.t.testDcaseGetParticipants('','','','')
        self.assertIn('无效的状态',message,'test_dcaseGetParticipants_fail_027测试失败。')
    #险情-列表
    def test_dcaseWarningList_success(self):
        message = self.t.testDcaseWarningList('','','','','')
        self.assertIn('success',message,'test_dcaseWarningList_success_028测试失败。')
    #修改负责人
    def test_dcaseAddChatge_success(self):
        message = self.t.testDcaseAddChatge('72','35')
        self.assertIn('修改负责人成功',message,'test_dcaseAddChatge_success_029测试失败。')
    def test_dcaseAddChatge_fail(self):
        message = self.t.testDcaseAddChatge('','')
        self.assertIn('无效的参数',message,'test_dcaseAddChatge_fail_030测试失败。')
    #添加险情
    def test_dcaseAdd_success(self):
        message = self.t.testDcaseAdd('三九大桥雨城区',29.58,103.0,4,'511800','testtesttest000','/uploads/20190925/6ac4875daf833164282a5311f2fcbd91.jpeg','2')
        self.assertIn('上报险情成功',message,'test_dcaseAdd_success_031测试失败。')
    def test_dcaseAdd_fail01(self):
        message = self.t.testDcaseAdd('','','','','','','','')
        self.assertIn('无效的地址', message, 'test_dcaseAdd_fail01_032测试失败。')
    def test_dcaseAdd_fail02(self):
        message = self.t.testDcaseAdd('三九大桥雨城区','','','','','','','')
        self.assertIn('无效纬度', message, 'test_dcaseAdd_fail02_033测试失败。')
    def test_dcaseAdd_fail03(self):
        message = self.t.testDcaseAdd('三九大桥雨城区',29.58,'','','','','','')
        self.assertIn('无效经度', message, 'test_dcaseAdd_fail03_034测试失败。')
    def test_dcaseAdd_fail04(self):
        message = self.t.testDcaseAdd('三九大桥雨城区', 29.58, 103.0, '', '', '', '', '')
        self.assertIn('无效的灾害类型', message, 'test_dcaseAdd_fail04_035测试失败。')
    def test_dcaseAdd_fail05(self):
        message = self.t.testDcaseAdd('三九大桥雨城区', 29.58, 103.0, 5, '', 'est', '', '')
        self.assertIn('无效的参数', message, 'test_dcaseAdd_fail05_036测试失败。')
    def test_dcaseAdd_fail06(self):
        message = self.t.testDcaseAdd('三九大桥雨城区', 29.58, 103.0, 5, '511800', '', '', '')
        self.assertIn('无效的内容', message, 'test_dcaseAdd_fail06_037测试失败。')
    # 险情新增配置
    def test_getReportConfig_success(self):
        message = self.t.testGetReportConfig('')
        self.assertIn('success',message,'test_getReportConfig_success_038测试失败。')
    #险情发送图片
    def test_dcaseImgSending_success(self):
        message = self.t.testDcaseImgSending(82,'/uploads/20190925/6ac4875daf833164282a5311f2fcbd91.jpeg,/uploads/20190924/a3a43377d2a7d95bf0da6b3038513a25.jpg')
        self.assertIn('操作成功',message,'test_dcaseImgSending_success_039测试失败。')
    def test_dcaseImgSending_fail(self):
        message = self.t.testDcaseImgSending('','')
        self.assertIn('无效的参数',message,'test_dcaseImgSending_fail_040测试失败。')
    # 险情发送文字
    def test_dcaseTextSending_success(self):
        message = self.t.testDcaseTextSending(82,'hahahahhahahaha')
        self.assertIn('操作成功',message,'test_dcaseTextSending_success_041测试失败。')
    def test_dcaseTextSending_fail(self):
        message = self.t.testDcaseTextSending('','')
        self.assertIn('无效的参数',message,'test_dcaseTextSending_success_041测试失败。')
    #险情处理[处理状态：0,1,2,3]
    def test_dcaseDangerousCase_success(self):
        message = self.t.testDcaseDangerousCase(81,2)
        self.assertIn('操作成功',message,'test_dcaseDangerousCase_success_042测试失败。')
    def test_dcaseDangerousCase_fail(self):
        message = self.t.testDcaseDangerousCase('','')
        self.assertIn('无效的参数',message,'test_dcaseDangerousCase_fail_043测试失败。')
    #险情-详情
    def test_dcaseDetails_success(self):
        message = self.t.testDcaseDetails(82)
        self.assertIn('success',message,'test_dcaseDetails_success_044测试失败。')
    def test_dcaseDetails_fail(self):
        message = self.t.testDcaseDetails('')
        self.assertIn('无效的参数',message,'test_dcaseDetails_fail_045测试失败。')
    # 大屏险情处置发送指令
    def test_dcaseXmt_success(self):
        message = self.t.testDcaseXmt(82,7,1,'1',1234567890,123457890)
        self.assertIn('',message,'test_dcaseXmt_success_046测试失败。')
    def test_dcaseXmt_fail01(self):
        message = self.t.testDcaseXmt('','','','','','')
        self.assertIn('无效的险情',message,'test_dcaseXmt_fail01_047测试失败。')
    def test_dcaseXmt_fail02(self):
        message = self.t.testDcaseXmt(82,'','','','','')
        self.assertIn('无效的接受人',message,'test_dcaseXmt_fail02_048测试失败。')
    def test_dcaseXmt_fail03(self):
        message = self.t.testDcaseXmt(82,7,'','','','')
        self.assertIn('请选择发送类型',message,'test_dcaseXmt_fail03_049测试失败。')
    def test_dcaseXmt_fail04(self):
        message = self.t.testDcaseXmt(82,7,1,'','','')
        self.assertIn('标题格式错误',message,'test_dcaseXmt_fail04_050测试失败。')
    def test_dcaseXmt_fail05(self):
        message = self.t.testDcaseXmt(82, 7, 1,'' , '1234567890', '')
        self.assertIn('内容格式错误', message, 'test_dcaseXmt_fail05_051测试失败。')
    def test_dcaseXmt_fail06(self):
        message = self.t.testDcaseXmt(82, 7, 1,'' , '1234567890', '456789')
        self.assertIn('无效推送方式', message, 'test_dcaseXmt_fail06_052测试失败。')
    #【巡检】列表
    def test_inspectingWarningList_success(self):
        message = self.t.testInspectingWarningList('','','','')
        self.assertIn('success',message,'test_inspectingWarningList_success_053测试失败。')
    # 【巡检】详情-经纬度需要返给h5做点位标记
    def test_inspectingDetails_success(self):
        message = self.t.testInspectingDetails('19')
        self.assertIn('success',message,'test_inspectingDetails_success_054测试失败。')
    def test_inspectingDetails_fail(self):
        message = self.t.testInspectingDetails('')
        self.assertIn('无效的参数', message, 'test_inspectingDetails_fail_055测试失败。')
    #添加巡检
    def test_inspectingAdd_success(self):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        message = self.t.testInspectingAdd('雅安站姚桥镇北环东路',1,30.028493,103.056953,'511800','11111111111',date,'','')
        self.assertIn('上传巡检成功',message,'test_inspectingAdd_success_056测试失败。')
    def test_inspectingAdd_fail01(self):
        message = self.t.testInspectingAdd('雅安站姚桥镇北环东路', 1, 30.028493, 103.056953, '511800', '11111111111', '','','')
        self.assertIn('无效的时间', message, 'test_inspectingAdd_fail01_057测试失败。')
    def test_inspectingAdd_fail02(self):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        message = self.t.testInspectingAdd('',1,'',103.056953, '511800', '11111111111',date,'','')
        self.assertIn('无效纬度',message,'test_inspectingAdd_fail02_058测试失败。')
    def test_inspectingAdd_fail03(self):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        message = self.t.testInspectingAdd('', 1, 30.028493, '', '511800', '11111111111', date,'','')
        self.assertIn('无效经度', message, 'test_inspectingAdd_fail03_059测试失败。')
    def test_inspectingAdd_fail04(self):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        message = self.t.testInspectingAdd('', 1, 30.028493, 103.056953, '', '11111111111', date,'','')
        self.assertIn('无效的参数', message, 'test_inspectingAdd_fail04_060测试失败。')
    def test_inspectingAdd_fail05(self):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        message = self.t.testInspectingAdd('', 1, 30.028493, 103.056953, '511800', '', date,'','')
        self.assertIn('info不能为空', message, 'test_inspectingAdd_fail05_061测试失败。')
    def test_inspectingAdd_fail06(self):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        message = self.t.testInspectingAdd('', '', 30.028493, 103.056953, '511800', 'PPP', date,'','')
        self.assertIn('无效的状态', message, 'test_inspectingAdd_fail06_062测试失败。')
    # 组织架构
    def test_organizationZuzhi_success(self):
        message = self.t.testOrganizationZuzhi()
        self.assertIn('success',message,'test_organizationZuzhi_success_063测试失败。')
    # 最近联系人
    def test_organizationRecentContacts_success(self):
        message = self.t.testOrganizationRecentContacts()
        self.assertIn('success',message,'test_organizationRecentContacts_success_064测试失败。')
    # 组织架构
    def test_organizationZuzhiJiagou_success(self):
        message = self.t.testOrganizationZuzhiJiagou()
        self.assertIn('success',message,'test_organizationZuzhiJiagou_success_065测试失败。')
    # 组织架构所有用户
    def test_organizationZuzhiDetails_success(self):
        message = self.t.testOrganizationZuzhiDetails('2','','')
        self.assertIn('success',message,'test_organizationZuzhiDetails_success_066测试失败。')
    def test_organizationZuzhiDetails_fail(self):
        message = self.t.testOrganizationZuzhiDetails('','','')
        self.assertIn('无效参数',message,'test_organizationZuzhiDetails_fail_067测试失败。')
    # 搜索所有用户
    def test_organizationSearch_success(self):
        message = self.t.testOrganizationSearch('陈','','')
        self.assertIn('success',message,'test_organizationSearch_success_068测试失败。')
    def test_organizationSearch_fail(self):
        message = self.t.testOrganizationSearch('','','')
        self.assertIn('格式错误',message,'test_organizationSearch_fail_069测试失败。')
    # 用户详情
    def test_organizationUserDetails_success(self):
        message = self.t.testOrganizationUserDetails('7')
        self.assertIn('success',message,'test_organizationUserDetails_success_070测试失败。')
    def test_organizationUserDetails_fail(self):
        message = self.t.testOrganizationUserDetails('')
        self.assertIn('无效ID',message,'test_organizationUserDetails_fail_071测试失败。')
    # 险情筛选条件，筛选类型【case：险情；inspecting：巡检；alarm：预警】
    def test_commonScreen_success(self):
        message = self.t.testCommonScreen('case')
        self.assertIn('',message,'test_commonScreen_success_072测试失败。')
    def test_commonScreen_fail(self):
        message = self.t.testCommonScreen('')
        self.assertIn('无效的行业',message,'test_commonScreen_fail_073测试失败。')
    # 检测版本，通过头部客户端版本判断
    def test_commonCheckVersion_success(self):
        message = self.t.testCommonCheckVersion('','','')
        self.assertIn('success',message,'test_commonCheckVersion_success_074测试失败。')
    # def test_commonCheckVersion_fail(self):
    #     message = self.t.testCommonCheckVersion('','','')
    #     self.assertIn('',message,'test_commonCheckVersion_fail_074测试失败。')
    # 添加用户device_tokens
    def test_commonDeviceTokens_success(self):
        message = self.t.testCommonDeviceTokens('Android','Akwhy5G4cGVMW9NoGMRfoXbexHuYv0j16fXT8cM2ktmw')
        self.assertIn('success',message,'test_commonDeviceTokens_success_075测试失败。')
    def test_commonDeviceTokens_fail(self):
        message = self.t.testCommonDeviceTokens('','')
        self.assertIn('无效的token或platform',message,'test_commonDeviceTokens_fail_076测试失败。')
    # 批量上传0-9照片
    # def test_commonBatchUpload_success(self):
    #     path = r'G:\Kedalo\Testing\APP\1.png'
    #     with open(path,'r') as f:
    #         file0 = f.read()
    #         message = self.t.testCommonBatchUpload(file0)
    #         self.assertIn('',message,'test_commonBatchUpload_success_077测试失败。')
    def test_commonBatchUpload_fail(self):
        message = self.t.testCommonBatchUpload('')
        self.assertIn('未上传文件或超出服务器上传限制',message,'test_commonBatchUpload_fail_078测试失败。')
    # 上传文件
    # def test_commonUpload_success(self):
    #     message = self.t.testCommonUpload('')
    #     self.assertIn('',message,'test_commonUpload_success_079测试失败。')
    def test_commonUpload_fail(self):
        message = self.t.testCommonUpload('')
        self.assertIn('未上传文件或超出服务器上传限制', message, 'test_commonUpload_fail_080测试失败。')
    # 上传用户经纬度
    def test_commonSetloc_success(self):
        message = self.t.testCommonSetloc(103.0,29.58)
        self.assertIn('success',message,'test_commonSetloc_success_081测试失败。')
    def test_commonSetloc_fail(self):
        message = self.t.testCommonSetloc('','')
        self.assertIn('无效经度或纬度',message,'test_commonSetloc_fail_082测试失败。')
    # 未读消息数量
    def test_commonNumMsg_success(self):
        message = self.t.testCommonNumMsg()
        self.assertIn('success',message,'test_commonNumMsg_success_083测试失败。')
    # 天气主要概况
    def test_homepageIndex_success(self):
        message = self.t.testHomepageIndex(103.0,29.58)
        self.assertIn('success',message,'test_homepageIndex_success_084测试失败。')
    def test_homepageIndex_fail(self):
        message = self.t.testHomepageIndex('', '')
        self.assertIn('无效纬度', message, 'test_homepageIndex_fail_085测试失败。')
    # 首页-全部,传递数据参考各分接口
    def test_homepageIndexAll_success(self):
        message = self.t.testHomepageIndexAll(103.0,29.58)
        self.assertIn('success',message,'test_homepageIndexAll_success_086测试失败。')
    def test_homepageIndexAll_fail(self):
        message = self.t.testHomepageIndexAll('','')
        self.assertIn('无效经度或纬度',message,'test_homepageIndexAll_fail_087测试失败。')
    # 【首页】首页-图标
    def test_homepageIndecIcon_success(self):
        message = self.t.testHomepageIndecIcon()
        self.assertIn('success',message,'test_homepageIndecIcon_success_088测试失败。')
    # 【首页】通知，如果没有通知，则不显示
    def test_homepageIndexNotify_success(self):
        message = self.t.testHomepageIndexNotify()
        self.assertIn('success',message,'test_homepageIndexNotify_success_089测试失败。')
     # 【首页】关注站点
    def test_mstationsFocusSites_success(self):
        message = self.t.testMstationsFocusSites('','')
        self.assertIn('success',message,'test_mstationsFocusSites_success_090测试失败。')
    # 监测站点头部动态切换栏
    def test_mstationsTableType_success(self):
        message = self.t.testMstationsTableType('10',2,'')
        self.assertIn('success',message,'test_mstationsTableType_success_091测试失败。')
    def test_mstationsTableType_fail(self):
        message = self.t.testMstationsTableType('','','')
        self.assertIn('无效的参数',message,'test_mstationsTableType_fail_092测试失败。')
    # 站点信息
    def test_mstationsGetSiteBasics_success(self):
        message = self.t.testMstationsGetSiteBasics('10',2)
        self.assertIn('success',message,'test_mstationsGetSiteBasics_success_093测试失败。')
    def test_mstationsGetSiteBasics_fail(self):
        message = self.t.testMstationsGetSiteBasics('','')
        self.assertIn('无效的参数',message,'test_mstationsGetSiteBasics_fail_094测试失败。')
    # 气象
    def test_mstationsGetSiteStatistics_success(self):
        message = self.t.testMstationsGetSiteStatistics('10',2)
        self.assertIn('success',message,'test_mstationsGetSiteStatistics_success_095测试失败。')
    def test_mstationsGetSiteStatistics_fail(self):
        message = self.t.testMstationsGetSiteStatistics('','')
        self.assertIn('无效的参数',message,'test_mstationsGetSiteStatistics_fail_096测试失败。')
    # 监测数据
    def test_mstationsGetMajor_success(self):
        message = self.t.testMstationsGetMajor('10',2)
        self.assertIn('success',message,'test_mstationsGetMajor_success_097测试失败。')
    def test_mstationsGetMajor_fail(self):
        message = self.t.testMstationsGetMajor('', '')
        self.assertIn('无效的参数', message, 'test_mstationsGetMajor_fail_098测试失败。')
    # 风场格点
    def test_H5WeatherWind_success(self):
        message = self.t.testH5WeatherWind()
        self.assertIn('success',message,'test_H5WeatherWind_success_099测试失败。')
    # 当前页面交互，点击显示雷电强度
    def test_H5WeatherThunder_success(self):
        message = self.t.testH5WeatherThunder()
        self.assertIn('success',message,'test_H5WeatherThunder_success_100测试失败。')
    # 站点【与APP交互】
    # def test_H5WeatherSite_success(self):
    #     message = self.t.testH5WeatherSite()
    #     self.assertIn('',message,'test_H5WeatherSite_success_101测试失败。')
    # 预警【与APP交互】
    def test_H5WeatherWarning_success(self):
        message = self.t.testH5WeatherWarning()
        self.assertIn('success',message,'test_H5WeatherWarning_success_102测试失败。')
    # 当前页面交互，点击显示质量详细指数
    def test_H5Weather_success(self):
        message = self.t.testH5Weather()
        self.assertIn('success',message,'test_H5Weather_success_103测试失败。')
    # 险情点位-闪动【与APP交互】
    def test_H5WeatherCase_success(self):
        message = self.t.testH5WeatherCase(2)
        self.assertIn('success',message,'test_H5WeatherCase_success_104测试失败。')
    # 监测点位【与APP交互】
    def test_H5WeatherJiance_success(self):
        message = self.t.testH5WeatherJiance('')
        self.assertIn('success',message,'test_H5WeatherJiance_success_106测试失败。')
    # 物资监测点
    def test_H5WeatherMaterial_success(self):
        message = self.t.testH5WeatherMaterial()
        self.assertIn('success',message,'test_H5WeatherMaterial_success_108测试失败。')
    # 巡检
    def test_H5WeatherInspecting_success(self):
        message = self.t.testH5WeatherInspecting(10)
        self.assertIn('success',message,'test_H5WeatherInspecting_success_109测试失败。')
    def test_H5WeatherInspecting_fail(self):
        message = self.t.testH5WeatherInspecting('')
        self.assertIn('error',message,'test_H5WeatherInspecting_fail_110测试失败。')
    # 险情
    def test_H5WeatherCased_success(self):
        message = self.t.testH5WeatherCased(86)
        self.assertIn('success',message,'test_H5WeatherCased_success_111测试失败。')
    def test_H5WeatherCased_fail(self):
        message = self.t.testH5WeatherCased('')
        self.assertIn('error',message,'test_H5WeatherCased_fail_112测试失败。')
    # 人员
    def test_H5WeatherUser_success(self):
        message = self.t.testH5WeatherUser()
        self.assertIn('success',message,'test_H5WeatherUser_success_113测试失败。')
    # 指定规划路径
    def test_H5WeatherNavigation_success(self):
        message = self.t.testH5WeatherNavigation()
        self.assertIn('success',message,'test_H5WeatherNavigation_success_114测试失败。')
    # 通过经纬度获取目的天气情况
    def test_weather_success(self):
        message = self.t.testWeather(29.58,103.0)
        self.assertIn('success',message,'test_weather_success_115测试失败。')
    def test_weather_fail(self):
        message = self.t.testWeather('','')
        self.assertIn('无效的参数',message,'test_weather_fail_116测试失败。')
    # 通过经纬度查询前方天气情况
    def test_weatherEarlyWarning_success(self):
        message = self.t.testWeatherEarlyWarning(29.58,103.0)
        self.assertIn('success',message,'test_weatherEarlyWarning_success_117测试失败。')
    def test_weatherEarlyWarning_fail(self):
        message = self.t.testWeatherEarlyWarning('','')
        self.assertIn('无效纬度',message,'test_weatherEarlyWarning_fail_118测试失败。')
    # 天气主要概况【APP考勤】
    def test_weatherKQ_success(self):
        message = self.t.testWeatherKQ(103.0,29.58)
        self.assertIn('success',message,'test_weatherKQ_success_119测试失败。')
    def test_weatherKQ_fail(self):
        message = self.t.testWeatherKQ('','')
        self.assertIn('无效纬度',message,'test_weatherKQ_fail_120测试失败。')
    # 帮助中心-列表
    def test_helpList_success(self):
        message = self.t.testHelpList('','')
        self.assertIn('success',message,'test_helpList_success_121测试失败。')
    # 帮助中心-详情
    def test_helpDetails_success(self):
        message = self.t.testHelpDetails(11)
        self.assertIn('success',message,'test_helpDetails_success_122测试失败。')
    def test_helpDetails_fail(self):
        message = self.t.testHelpDetails('')
        self.assertIn('无效的ID',message,'test_helpDetails_fail_123测试失败。')
    # ING险情-列表
    def test_caseList_success(self):
        message = self.t.testCaseList('','','','','')
        self.assertIn('success',message,'test_caseList_success_124测试失败。')
     # 【通知】通知列表
    def test_messageNotice_success(self):
        message = self.t.testMessageNotice('','','')
        self.assertIn('success',message,'test_messageNotice_success_125测试失败。')
    # 【通知】类型详情
    def test_messageNoticeDetails_success(self):
        message = self.t.testMessageNoticeDetails('','',1)
        self.assertIn('success',message,'test_messageNoticeDetails_success_126测试失败。')
    def test_messageNoticeDetails_fail(self):
        message = self.t.testMessageNoticeDetails('', '', '')
        self.assertIn('无效参数', message, 'test_messageNoticeDetails_fail_127测试失败。')
    # 【new】通知-详情，自动阅读
    def test_messageDetails_success(self):
        message = self.t.testMessageDetails(2)
        self.assertIn('success',message,'test_messageDetails_success_128测试失败。')
    def test_messageDetails_fail(self):
        message = self.t.testMessageDetails('')
        self.assertIn('无效的参数',message,'test_messageDetails_fail_129测试失败。')
    # 通知-删除
    def test_messageDelMsg_success(self):
        message = self.t.testMessageDelMsg(2)
        self.assertIn('success',message,'test_messageDelMsg_success_130测试失败。')
    def test_messageDelMsg_fail(self):
        message = self.t.testMessageDelMsg('')
        self.assertIn('无效的参数',message,'test_messageDelMsg_fail_131测试失败。')
    # 工作台
    def test_workbench_success(self):
        message = self.t.testWorkbench()
        self.assertIn('success',message,'test_workbench_success_132测试失败。')
    def tearDown(self):
        pass
if __name__ == '__main__':
    suite = unittest.TestSuite()
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    suite.addTests(test_cases)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
