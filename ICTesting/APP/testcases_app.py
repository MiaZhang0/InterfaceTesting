import unittest
from unittest import TestCase
from APP import testModule_App

class TestClass(TestCase):
    def setUp(self):
        self.t = testModule_App.TestModuleClass()
    #发送手机验证码
    def test_sendCode_success(self):
        message = self.t.testSendCode('')
        self.assertIn('',message,'test_sendCode_success_测试失败。')
    def test_sendCode_fail(self):
        message = self.t.testSendCode('')
        self.assertIn('',message,'test_sendCode_fail_测试失败。')
    #短信登录
    def test_login_success(self):
        message = self.t.testLogin('','')
        self.assertIn('',message,'test_login_success_测试失败。')
    def test_login_fail(self):
        message = self.t.testLogin('','')
        self.assertIn('',message,'test_login_fail_测试失败。')
    #选择，切换小区
    def test_selectArea_success(self):
        message = self.t.testSelectArea('','')
        self.assertIn('',message,'test_selectArea_success_测试失败。')
    def test_selectArea_fail(self):
        message = self.t.testSelectArea('', '')
        self.assertIn('',message,'test_selectArea_fail_测试失败。')
    #轮播列表
    def test_bannerList_success(self):
        message = self.t.testBannerList()
        self.assertIn('',message,'test_bannerList_success_测试失败。')
    #公告列表
    def test_noticeList_success(self):
        message = self.t.testNoticeList('')
        self.assertIn('',message,'test_noticeList_success_测试失败。')
    def test_noticeList_fail(self):
        message = self.t.testNoticeList('')
        self.assertIn('',message,'test_noticeList_fail_测试失败。')