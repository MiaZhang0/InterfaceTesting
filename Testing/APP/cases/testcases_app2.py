import unittest
from unittest import TestCase
from APP import testModule_APP2
import time

class TestClass(TestCase):
    def setUp(self):
        self.t = testModule_APP2.TestModuleClass()
    # 登录
    def test_login_success(self):
        message = self.t.testLoginModule('15108307817', 'Kk1234')
        self.assertIn('登录成功', message[0], 'test_login_success_001测试失败。')
    def test_login_fail01(self):
        message = self.t.testLoginModule('','')
        self.assertIn('手机号码错误，请重新输⼊！',message,'test_login_fail01_002测试失败。')
    def test_login_fail02(self):
        message = self.t.testLoginModule('15108307817','1')
        self.assertIn('密码错误，请重新输⼊！', message, 'test_login_fail02_003测试失败。')

    def test_homepageWeather_success(self):
        message = self.t.testHomepageWeather('','')
        self.assertIn('success',message,'test_homepageWeather_success_004测试失败。')
    def test_homepageWeather_fail(self):
        message = self.t.testHomepageWeather(-11111111111111111111111111,-2)
        self.assertIn('Undefined index: code',message,'test_homepageWeather_fail_005测试失败。')

    def test_alarmInfo_success(self):
        message = self.t.testAlarmInfo('2','2')
        self.assertIn('success',message,'test_alarmInfo_success_006测试失败。')
    def test_alarmInfo_fail(self):
        message = self.t.testAlarmInfo('sss','')
        self.assertIn('无效的参数',message,'test_alarmInfo_fail_007测试失败。')

    def test_alarmDetail_success(self):
        message = self.t.testAlarmDetail('1')
        self.assertIn('success',message,'test_alarmDetail_success_008测试失败。')
    def test_alarmDetail_fail01(self):
        message = self.t.testAlarmDetail('')
        self.assertIn('无效的参数',message,'test_alarmDetail_fail01_009测试失败。')
    def test_alarmDetail_fail02(self):
        message = self.t.testAlarmDetail('99')
        self.assertIn('告警不存在', message, 'test_alarmDetail_fail02_010测试失败。')

    def test_warningList_success(self):
        message = self.t.testWarningList('','','','')
        self.assertIn('success',message,'test_warningList_success_011测试失败。')
    def test_warningList_fail01(self):
        message = self.t.testWarningList('aaaaa','','','')
        self.assertIn('无效的页码',message,'test_warningList_fail01_012测试失败。')
    def test_warningList_fail02(self):
        message = self.t.testWarningList('','aaaa','','')
        self.assertIn('无效的数量',message,'test_warningList_fail02_013测试失败。')
    def test_warningList_fail03(self):
        message = self.t.testWarningList('','','aaaa','')
        self.assertIn('无效的预警等级',message,'test_warningList_fail03_014测试失败。')
    def test_warningList_fail04(self):
        message = self.t.testWarningList('','','','aaaa')
        self.assertIn('Invalid argument supplied for foreach()',message,'test_warningList_fail04_014测试失败。')

    def test_warningStatistics_success(self):
        message = self.t.testWarningStatistics('')
        self.assertIn('success',message,'test_warningStatistics_success_015测试失败。')
    def test_warningStatistics_fail(self):
        message = self.t.testWarningStatistics('aaaa')
        self.assertIn('Invalid argument supplied for foreach()',message,'test_warningStatistics_fail_016测试失败。')

    def test_dcaseList_success(self):
        message = self.t.testDcaseList('','','','','')
        self.assertIn('success',message,'test_dcaseList_success_017测试失败。')
    def test_dcaseList_fail01(self):
        message = self.t.testDcaseList('aaa','','','','')
        self.assertIn('Invalid argument supplied for foreach()',message,'test_dcaseList_fail01_018测试失败。')
    def test_dcaseList_fail02(self):
        message = self.t.testDcaseList('','','aaa','','')
        self.assertIn('无效的参数', message, 'test_dcaseList_fail02_019测试失败。')
    def test_dcaseList_fail03(self):
        message = self.t.testDcaseList('','','','','aaa')
        self.assertIn('无效的状态', message, 'test_dcaseList_fail03_020测试失败。')

    def test_dcaseStatistics_success(self):
        message = self.t.testDcaseStatistics('','')
        self.assertIn('success',message,'test_dcaseStatistics_success_021测试失败。')
    def test_dcaseStatistics_fail(self):
        message = self.t.testDcaseStatistics('aaa','')
        self.assertIn('Invalid argument supplied for foreach()',message,'test_dcaseStatistics_fail_022测试失败。')

    def test_monitorList_success(self):
        message = self.t.testMonitorList('','','')
        self.assertIn('success',message,'test_monitorList_success_023测试失败。')
    def test_monitorList_fail01(self):
        message = self.t.testMonitorList('','aaa','')
        self.assertIn('无效的页码',message,'test_monitorList_fail01_024测试失败。')
    def test_monitorList_fail02(self):
        message = self.t.testMonitorList('','','aaa')
        self.assertIn('无效的数量',message,'test_monitorList_fail02_025测试失败。')

    def test_monitorStatistics_success(self):
        message = self.t.testMonitorStatistics()
        self.assertIn('success',message,'test_monitorStatistics_success_026测试失败。')

    def test_commonMsg_success(self):
        message = self.t.testCommonMsg()
        self.assertIn('success',message,'test_commonMsg_success_027测试失败。')
    def tearDown(self):
        pass
if __name__ == '__main__':
    suite = unittest.TestSuite()
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    suite.addTests(test_cases)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)