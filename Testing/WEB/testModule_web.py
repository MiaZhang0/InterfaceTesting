import requests

class TestWebModuleClass():
    def __init__(self):
        self.host = 'http://118.123.236.28:8089'
    #信息统计,本月事故灾难分布|自然灾害分布|公共安全分布
    def testInfoAccidentNum(self,cityCode,type):
        url = self.host + '/info/queryAccidentNum'
        datas = {'cityCode':cityCode,'type':type}
        r = requests.post(url,data=datas)
        message = r.text
        # print(message)
        return message
    #	信息统计,查询子灾害类型列表
    def testInfoAccidentType(self,type):
        url = self.host + '/info/queryAccidentType'
        datas = {'type':type}
        r = requests.post(url,data=datas)
        message = r.text
        #print(message)
        return message
    #	信息统计,本月预警数、本月灾害数
    def testInfoDisasterNum(self,cityCode,type):
        url = self.host + '/info/queryDisasterNum'
        datas = {'cityCode':cityCode,'type':type}
        r = requests.post(url,data=datas)
        message = r.text
        #print(message)
        return message
    #	信息统计,本年度公共安全事件
    def testInfoEventsForYear(self,cityCode):
        url = self.host + '/info/queryEventsForYear'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        #print(message)
        return message
    #信息统计,查询灾害类型对应的行业ID
    def testInfoIndustryId(self,type):
        url = self.host + '/info/queryIndustryId'
        datas = {'type':type}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #信息统计,灾害损失统计
    def testInfoLossNum(self,cityCode,type):
        url = self.host + '/info/queryLossNum'
        datas = {'cityCode':cityCode,'type':type}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #信息统计,灾害类型、受损类型年数据统计
    def testInfoLossNumYear(self,cityCode,id,type):
        url = self.host + '/info/queryLossNumByTyeAndIdForYear'
        datas = {'cityCode':cityCode,'id':id,'type':type}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #信息统计,本年度灾害类型对应的受损类型列表
    def testInfoLossType(self,cityCode,type):
        url = self.host + '/info/queryLossType'
        datas = {'cityCode': cityCode, 'type': type}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #	信息统计,地图数据
    def testInfoMapData(self,cityCode,type):
        url = self.host + '/info/queryMapData'
        datas = {'cityCode': cityCode, 'type': type}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #	信息统计,本月自然灾害分布
    def testInfoNaturalNum(self,cityCode,id):
        url = self.host + '/info/queryNaturalNum'
        datas = {'cityCode': cityCode, 'id': id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #信息统计,灾害三年同比统计数据
    def testInfoWdtyn(self,cityCode,id):
        url = self.host + '/info/queryWdtyn'
        datas = {'cityCode':cityCode,'id':id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #信息统计,事故灾难类型年数据统计
    def testInfoAccidentTypeNumYear(self,cityCode,id):
        url = self.host + '/info/queyAccidentTypeNumForYear'
        datas = {'cityCode': cityCode, 'id': id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #值班信息
    def testDutyData(self):
        url = self.host + '/duty/queryDutyData'
        r = requests.post(url)
        message = r.text
        print(message)
        return message
    #	历史降水量
    def testBuildingPrRank(self,cityCode):
        url = self.host + '/building/queryBuildingPrRank'
        datas = {'cityCode':cityCode}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #历史气温
    def testBuildingTmpRank(self,cityCode):
        url = self.host + '/building/queryBuildingTmpRank'
        datas = {'cityCode': cityCode}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #	常驻视频
    def testBuildingFocusSpDevs(self,cityCode):
        url = self.host + '/building/queryFocusSpDevs'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #	建筑项目点列表
    def testBuildingProjects(self,cityCode):
        url = self.host + '/building/queryProjects'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #某一建筑项目设备上传数据
    def testBuildingProjectsData(self,id):
        url = self.host + '/building/queryProjectsDataByDev'
        datas = {'id':id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #某一建筑点信息
    def testBuildingProjectsInfo(self,id):
        url = self.host + '/building/queryProjectsInfo'
        datas = {'id': id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #某一建筑项目天气
    def testBuildingProjectsWeather(self,id):
        url = self.host + '/building/queryProjectsWeather'
        datas = {'id': id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #视频监控
    def testBuildingSpDevs(self,cityCode):
        url = self.host + '/building/querySpDevs'
        datas = {'cityCode': cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #项目点视频列表
    def testBuildingSpDevsList(self,id):
        url = self.host + '/building/querySpDevsByProjectId'
        datas = {'id':id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #安全提示,详情
    def testBuildingWarnDetail(self,cityCode,id):
        url = self.host + '/building/queryWarnDetail'
        datas = {'cityCode': cityCode,'id':id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #安全提示
    def testBuildingWarns(self,cityCode):
        url = self.host + '/building/queryWarns'
        datas = {'cityCode': cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #开始云台控制
    def testBuildingStartControlISP(self,devMac,direction):
        url = self.host + '/building/startControlSP'
        datas = {'devMac':devMac,'direction':direction}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #停止云台控制
    def testBuildingStopControlISP(self,devMac,direction):
        url = self.host + '/building/stopControlSP'
        datas = {'devMac': devMac, 'direction': direction}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #卫星云图
    def testWeatherCloudPics(self):
        url = self.host + '/weather/queryCloudPics'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #气象，历史降水排名统计
    def testWeatherHistoryPr(self,cityCode):
        url = self.host + '/weather/queryHistoryPr'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #气象，历史气温排名统计
    def testWeatherHistoryTmp(self,cityCode):
        url = self.host + '/weather/queryHistoryTmp'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #气象，天气雷达
    def testWeatherRadarPics(self):
        url = self.host + '/weather/queryRadarPics'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #险情点天气状况
    def testWeatherCase(self,lat,lng):
        url = self.host + '/weather/queryWeatherByCase'
        datas = {'lat':lat,'lng':lng}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #	天气预报
    def testWeatherCityCode(self,cityCode):
        url = self.host + '/weather/queryWeatherByCityCode'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #安装点制定天气状态
    def testWeatherSites(self,lat,lng):
        url = self.host + '/weather/queryWeatherBySite'
        datas = {'lat':lat,'lng':lng}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #站点降水、气温、风数据
    def testWeatherStations(self,lat,lng):
        url = self.host + '/weather/queryWeatherByStation'
        datas = {'lat': lat, 'lng': lng}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #查询次级行政区域未来三天天气预报
    def testWeatherThreeDay(self,cityCode):
        url = self.host + '/weather/queryWeatherByThreeDay'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #查询行政区域未来三天详细预报数据
    def testWeatherDataThreeDay(self,cityCode):
        url = self.host + '/weather/queryWeatherDataByThreeDay'
        datas = {'cityCode': cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #气象，降水量预报
    def testWeatherPrForecast(self,cityCode):
        url =  self.host + '/weather/queryWeatherPrForecast'
        datas = {'cityCode': cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #气象，预警详情信息
    def testWeatherWarnDetails(self,id):
        url = self.host + '/weather/queryWeatherWarnDetails'
        datas = {'id':id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #气象，最新预警
    def testWeatherWarns(self,cityCode):
        url = self.host + '/weather/queryWeatherWarns'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #获取所有的视频列表
    def testMstationAllSpList(self):
        url = self.host + '/mstation/queryAllSpList'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #行政区域内所有监测点列表
    def testMstations(self,cityCode,typs):
        url = self.host + '/mstation/queryMStations'
        datas = {'cityCode':cityCode,'typs':typs}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #行业监测站点统计
    def testMstationCount(self,cityCode):
        url = self.host + '/mstation/queryMStationsCount'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #监测站/项目信息
    def testMstationInfo(self,id):
        url = self.host + '/mstation/queryMStationsInfo'
        datas = {'id':id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #获取气象监测点信息
    def testMstationWeatherInfo(self,id):
        url = self.host + '/mstation/queryWeatherMStationsInfo'
        datas = {'id': id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #传行政区域编码，获取区域及次级区域告警统计
    def testStatisticsAreaWarnCount(self,cityCode,timeType):
        url  = self.host + '/statistics/queryAreaWarnCount'
        datas = {'cityCode':cityCode,'timeType':timeType}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #险情统计
    def testStatisticsCaseCount(self,cityCode):
        url = self.host + '/statistics/queryCaseCount'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #险情总汇
    def testStatisticsCaseTypeCount(self,cityCode):
        url = self.host + '/statistics/queryCaseTypeCount'
        datas = {'cityCode': cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #行业告警统计
    def testStatisticsCategoryWarnCount(self,cityCode):
        url = self.host + '/statistics/queryCategoryWarnCount'
        datas = {'cityCode': cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #预警、险情、重点监测、站点
    def testStatisticsEveryCount(self,cityCode):
        url = self.host + '/statistics/queryEveryCount'
        datas = {'cityCode': cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #	正在预计-等级统计
    def testStatisticsGradeCount(self,cityCode,timeType):
        url = self.host + '/statistics/queryGradeCount'
        datas = {'cityCode':cityCode,'timeType':timeType}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #监测站点数量统计
    def testStatisticsMstationCount(self,cityCode):
        url = self.host + '/statistics/queryMStationsCount'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #	正在预计-类型统计
    def testStatisticsTypeCount(self,cityCode):
        url = self.host + '/statistics/queryTypeCount'
        datas = {'cityCode': cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #天气预警统计
    def testStatisticsWarningCount(self,cityCode):
        url = self.host + '/statistics/queryWarningCount'
        datas = {'cityCode': cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #	行业列表
    def testIndustrys(self):
        url  = self.host + '/industrys/queryIndustrys'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #获取下级行政区域
    def testAreaGet(self,cityCode):
        url = self.host + '/area/getAreaByParent'
        datas = {'cityCode': cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #首页，重点监测视频
    def testVideoGetADevs(self):
        url = self.host + '/video/getAttentionDevs'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #根据经纬度、距离查询附近视频
    def testVideoGetSpDev(self,distance,lat,lng):
        url = self.host + '/video/getSpDevByDistance'
        datas = {'distance':distance,'lat':lat,'lng':lng}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #区县查询列表
    def testVideoGetCodeSpDev(self,code):
        url = self.host + '/video/getSpDevByParentCode'
        datas = {'code':code}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #险情处理状态
    def testDcaseHandle(self,id):
        url = self.host + '/dcase/dcaseHandle'
        datas = {'id':id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #	险情简报
    def testCaseReport(self,id):
        url = self.host + '/dcase/queryCaseReportById'
        datas = {'id': id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #险情统计页面，重大险情
    def testDcases(self,cityCode,type):
        url = self.host + '/dcase/queryCasesByCriteria'
        datas = {'cityCode':cityCode,'type':type}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #险情页面当前险情列表
    def testCasesList(self,cityCode):
        url = self.host + '/dcase/queryCasesList'
        datas = {'cityCode': cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #地图物资、负责人、避难场所、设备标点
    def testDcaseData(self,id):
        url = self.host + '/dcase/queryDataByCases'
        datas = {'id':id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #查看险情详情
    def testDcaseDetails(self,id):
        url = self.host + '/dcase/queryDcaseDetails'
        datas = {'id': id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #查看险情处理流程
    def testDcaseHandleProcess(self,id):
        url = self.host + '/dcase/queryDcaseHandleProcess'
        datas = {'id': id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #	险情影响
    def testDcseDisasterCount(self,id):
        url = self.host + '/dcase/queryDisasterCountByCaseId'
        datas = {'id':id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #历史险情
    def testDcaseHistoryCases(self,industryId,lat,lng):
        url = self.host + '/dcase/queryHistoryCases'
        datas = {'industryId':industryId,'lat':lat,'lng':lng}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #查看物资 | 负责人 | 避难场所 | 设备详情信息
    def testDcaseInfo(self,id,typeId):
        url = self.host + '/dcase/queryInfoById'
        datas = {'id':id,'typeId':typeId}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #险情点视频监控列表
    def testDcaseSP(self,lat,lng):
        url = self.host + '/dcase/querySPByCases'
        datas = {'lat':lat,'lng':lng}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #首页阈值预警模拟数据
    def testWarningThresholdAlarm(self):
        url = self.host + '/warning/queryThresholdAlarm'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #	预警详情
    def testWarningDetails(self,id):
        url = self.host + '/warning/queryWarningDetails'
        datas = {'id',id}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #最新预警列表
    def testWarnings(self,cityCode):
        url = self.host + '/warning/queryWarnings'
        datas = {'cityCode':cityCode}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #
# TestWebModuleClass().testInfoAccidentNum('','')