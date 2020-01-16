import unittest
from unittest import TestCase
from WEB import testModule

class TestClass(TestCase):
    def setUp(self):
        self.t = testModule.TestModuleClass()
    #发送手机验证码
    def test_sendCode_success(self):
        message = self.t.testSendCode('15108307817')
        self.assertIn('',message,'test_sendCode_success_001测试失败。')
    def test_sendCode_fail(self):
        message = self.t.testSendCode('')
        self.assertIn('',message,'test_sendCode_fail_002测试失败。')
    #控制台登录，返回token
    def test_msgLogin_success(self):
        message = self.t.testMsgLogin('','')
        self.assertIn('',message,'test_msgLogin_success_003测试失败。')
    def test_msgLogin_fail(self):
        message = self.t.testMsgLogin('','')
        self.assertIn('',message,'test_msgLogin_fail_测试失败。')
    #普通登录
    def test_login_success(self):
        message = self.t.testLogin('','')
        self.assertIn('',message,'test_login_success_测试失败。')
    def test_login_fail(self):
        message = self.t.testLogin('','')
        self.assertIn('',message,'test_login_fail_测试失败。')
    #登出
    def test_logout_success(self):
        message = self.t.testLogout()
        self.assertIn('',message,'test_logout_success_测试失败。')
    # 获取菜单权限
    def test_menuAuthority_success(self):
        message = self.t.testMenuAuthority('')
        self.assertIn('',message,'test_menuAuthority_success_测试失败。')
    def test_menuAuthority_fail(self):
        message = self.t.testMenuAuthority('')
        self.assertIn('',message,'test_menuAuthority_fail_测试失败。')
    # 居民查询条件，小区列表
    def test_areaList_success(self):
        message = self.t.testAreasList()
        self.assertIn('',message,'test_areaList_success_测试失败。')
    def test_areaList_fail(self):
        message = self.t.testAreasList()
        self.assertIn('',message,'test_areaList_fail_测试失败。')
    # 添加资讯草稿
    def test_newsDraft_success(self):
        message = self.t.testNewsDraft('','','','','','','')
        self.assertIn('',message,'test_newsDraft_success_测试失败。')
    def test_newsDraft_fail(self):
        message = self.t.testNewsDraft('', '', '', '', '', '', '')
        self.assertIn('',message,'test_newsDraft_fail_测试失败。')
    #检测是否有资讯草稿
    def test_findNewsDraft_success(self):
        message = self.t.testFindNewsDraft()
        self.assertIn('',message,'test_findNewsDraft_success_测试失败。')
    def test_findNewsDraft_fail(self):
        message = self.t.testFindNewsDraft()
        self.assertIn('',message,'test_findNewsDraft_fail_测试失败。')
    #小区单位信息
    def test_cellUnitInfo_success(self):
        message = self.t.testCellUnitInfo()
        self.assertIn('',message,'test_cellUnitInfo_success_测试失败。')
    #图片下载
    def test_imageDownload_success(self):
        message = self.t.testImageDownload('')
        self.assertIn('',message,'test_imageDownload_success_测试失败。')
    def test_imageDownload_fail(self):
        message = self.t.testImageDownload('')
        self.assertIn('',message,'test_imageDownload_fail_测试失败。')
    #上传图片
    def test_imageUpload_success(self):
        message = self.t.testImageUpload('','')
        self.assertIn('',message,'test_imageUpload_success_测试失败。')
    def test_imageUpload_fail(self):
        message = self.t.testImageUpload('','')
        self.assertIn('',message,'test_imageUpload_fail_测试失败。')
    #获取当前权限方法
    def test_authList_success(self):
        message = self.t.testAuthList('','','')
        self.assertIn('',message,'test_authList_success_测试失败。')
    def test_authList_fail(self):
        message = self.t.testAuthList('','','')
        self.assertIn('',message,'test_authList_fail_测试失败。')
    #删除小区
    def test_CellDel_success(self):
        message = self.t.testCellDel('')
        self.assertIn('',message,'test_CellDel_success_测试失败。')
    def test_CellDel_fail(self):
        message = self.t.testCellDel('')
        self.assertIn('',message,'test_CellDel_fail_测试失败。')
    #导出小区列表数据
    def test_exportData_success(self):
        message = self.t.testExportData()
        self.assertIn('',message,'test_exportData_success_测试失败。')
    #小区列表
    def test_CellList_success(self):
        message = self.t.testCellList('','','')
        self.assertIn('',message,'test_CelList_success_测试失败。')
    def test_CellList_fail(self):
        message = self.t.testCellList('','','')
        self.assertIn('',message,'test_CellList_fail_测试失败。')
    #新增小区
    def test_CellAdd_success(self):
        message = self.t.testCellAdd('','','','','','','','','','','')
        self.assertIn('',message,'test_CellAdd_success_测试失败。')
    def test_CellAdd_fail(self):
        message = self.t.testCellAdd('','','','','','','','','','','')
        self.assertIn('',message,'test_CellAdd_fail_测试失败。')
    #修改小区
    def test_CellEdit_success(self):
        message = self.t.testCellEdit('','','','','','','','','','','','')
        self.assertIn('',message,'test_CellEdit_success_测试失败。')
    def test_CellEdit_fail(self):
        message = self.t.testCellEdit('','','','','','','','','','','','')
        self.assertIn('',message,'test_CellEdit_fail_测试失败。')
    #轮播详情
    def test_bannerInfo_success(self):
        message = self.t.testBannerInfo('')
        self.assertIn('',message,'test_bannerInfo_success_测试失败。')
    def test_bannerInfo_fail(self):
        message = self.t.testBannerInfo('')
        self.assertIn('',message,'test_bannerInfo_fail_测试失败。')
    #轮播列表
    def test_bannerList_success(self):
        message = self.t.testBannerList('','','','')
        self.assertIn('',message,'test_bannerList_success_测试失败。')
    def test_bannerList_fail(self):
        message = self.t.testBannerList('','','','')
        self.assertIn('',message,'test_bannerList_fail_测试失败。')
    #添加轮播
    def test_bannerAdd_success(self):
        message = self.t.testBannerAdd('','','','')
        self.assertIn('',message,'test_bannerAdd_success_测试失败。')
    def test_bannerAdd_fail(self):
        message = self.t.testBannerAdd('','','','')
        self.assertIn('',message,'test_bannerAdd_fail_测试失败。')
    #编辑轮播
    def test_bannerEdit_success(self):
        message = self.t.testBannerEdit('','','','','')
        self.assertIn('',message,'test_bannerEdit_success_测试失败。')
    def test_bannerEdit_fail(self):
        message = self.t.testBannerEdit('','','','','')
        self.assertIn('',message,'test_bannerEdit_fail_测试失败。')
    #删除轮播
    def test_bannerDel_success(self):
        message = self.t.testBannerDel()
        self.assertIn('',message,'test_bannerDel_success_测试失败。')
    #发布轮播
    def test_bannerRelease_success(self):
        message = self.t.testBannerRelease('','')
        self.assertIn('',message,'test_bannerRelease_success_测试失败。')
    def test_bannerRelease_fail(self):
        message = self.t.testBannerRelease('','')
        self.assertIn('',message,'test_bannerRelease_fail_测试失败。')
    #新建社区
    def test_communityAdd_success(self):
        message = self.t.testCommunityAdd('','','','','','','','','','','','','')
        self.assertIn('',message,'test_communityAdd_success_测试失败。')
    def test_communityAdd_fail(self):
        message = self.t.testCommunityAdd('','','','','','','','','','','','','')
        self.assertIn('',message,'test_communityAdd_fail_测试失败。')
    #社区详情
    def test_communityInfo_success(self):
        message = self.t.testCommunityInfo('')
        self.assertIn('',message,'test_communityInfo_success_测试失败。')
    def test_communityInfo_fail(self):
        message = self.t.testCommunityInfo('')
        self.assertIn('',message,'test_communityInfo_fail_测试失败。')
    #编辑社区，请求参数地址对象，社区对象，员工对象
    def test_communityEdit_success(self):
        message = self.t.testCommunityEdit()
        self.assertIn('',message,'test_communityEdit_success_测试失败。')
    #公告列表
    def test_noticeList_success(self):
        message = self.t.testNoticeList('','','','')
        self.assertIn('',message,'test_noticeList_success_测试失败。')
    def test_noticeList_fail(self):
        message = self.t.testNoticeList('', '', '', '')
        self.assertIn('',message,'test_noticeList_fail_测试失败。')
    #新增公告
    def test_noticeAdd_success(self):
        message = self.t.testNoticeAdd('','','')
        self.assertIn('',message,'test_noticeAdd_success_测试失败。')
    def test_noticeAdd_fail(self):
        message = self.t.testNoticeAdd('','','')
        self.assertIn('',message,'test_noticeAdd_fail_测试失败。')
    #公告详情
    def test_noticeInfo_success(self):
        message = self.t.testNoticeInfo('')
        self.assertIn('',message,'test_noticeInfo_success_测试失败。')
    def test_noticeInfo_fail(self):
        message = self.t.testNoticeInfo('')
        self.assertIn('',message,'test_noticeInfo_fail_测试失败。')
    #公告修改
    def test_noticeEdit_success(self):
        message = self.t.testNoticeEdit('','','','')
        self.assertIn('',message,'test_noticeEdit_success_测试失败。')
    def test_noticeEdit_fail(self):
        message = self.t.testNoticeEdit('','','','')
        self.assertIn('',message,'test_noticeEdit_fail_测试失败。')
    #公告置顶
    def test_noticeTop_success(self):
        message = self.t.testNoticeTop('','')
        self.assertIn('',message,'test_noticeTop_success_测试失败。')
    def test_noticeTop_fail(self):
        message = self.t.testNoticeTop('','')
        self.assertIn('',message,'test_noticeTop_fail_测试失败。')
    #公告发布
    def test_noticeRelease_success(self):
        message = self.t.testNoticeRelease('','')
        self.assertIn('',message,'test_noticeRelease_success_测试失败。')
    def test_noticeRelease_fail(self):
        message = self.t.testNoticeRelease('','')
        self.assertIn('',message,'test_noticeRelease_fail_测试失败。')
    #公告删除
    def test_noticeDel_success(self):
        message = self.t.testNoticeDel()
        self.assertIn('',message,'test_noticeDel_success_测试失败。')
    #导出居民
    def test_residentExport_success(self):
        message = self.t.testResidentExport()
        self.assertIn('',message,'test_residentExport_success_测试失败。')
    #新增居民
    def test_residentAdd_success(self):
        message = self.t.testResidentAdd('','','','','','','')
        self.assertIn('',message,'test_residentAdd_success_测试失败。')
    def test_residentAdd_fail(self):
        message = self.t.testResidentAdd('','','','','','','')
        self.assertIn('',message,'test_residentAdd_fail_测试失败。')
    #删除居民
    def test_residentDel_success(self):
        message = self.t.testResidentDel('')
        self.assertIn('',message,'test_residentDel_success_测试失败。')
    def test_residentDel_fail(self):
        message = self.t.testResidentDel('')
        self.assertIn('',message,'test_residentDel_fail_测试失败。')
    #编辑居民
    def test_residentEdit_success(self):
        message = self.t.testResidentEdit('','','','','','','','')
        self.assertIn('',message,'test_residentEdit_success_测试失败。')
    def test_residentEdit_fail(self):
        message = self.t.testResidentEdit('', '', '', '', '', '', '', '')
        self.assertIn('',message,'test_residentEdit_fail_测试失败。')
    #居民列表
    def test_residentList_success(self):
        message = self.t.testResidentList('','','','','','')
        self.assertIn('',message,'test_residentList_success_测试失败。')
    def test_residentList_fail(self):
        message = self.t.testResidentList('','','','','','')
        self.assertIn('',message,'test_residentList_fail_测试失败。')
    #居民信息
    def test_residentInfo_success(self):
        message = self.t.testResidentInfo('')
        self.assertIn('',message,'test_residentInfo_success_测试失败。')
    def test_residentInfo_fail(self):
        message = self.t.testResidentInfo('')
        self.assertIn('',message,'test_residentInfo_fail_测试失败。')
    #社区或小区管理员管理
    def test_manageList_success(self):
        message = self.t.testManageList('','','')
        self.assertIn('',message,'test_manageList_success_测试失败。')
    def test_manageList_fail(self):
        message = self.t.testManageList('','','')
        self.assertIn('',message,'test_manageList_fail_测试失败。')
    #管理员详情
    def test_accountInfo_success(self):
        message = self.t.testAccountInfo('')
        self.assertIn('',message,'test_accountInfo_success_测试失败。')
    def test_accountInfo_fail(self):
        message = self.t.testAccountInfo('')
        self.assertIn('',message,'test_accountInfo_fail_测试失败。')
    #新增管理员
    def test_accountAdd_success(self):
        message = self.t.testAccountAdd('','','','','')
        self.assertIn('',message,'test_accountAdd_success_测试失败。')
    def test_accountAdd_fail(self):
        message = self.t.testAccountAdd('','','','','')
        self.assertIn('',message,'test_accountAdd_fail_测试失败。')
    #管理员编辑
    def test_accountEdit_success(self):
        message = self.t.testAccountEdit('','','','','')
        self.assertIn('',message,'test_accountEdit_success_测试失败。')
    def test_accountEdit_fail(self):
        message = self.t.testAccountEdit('','','','','')
        self.assertIn('',message,'test_accountEdit_fail_测试失败。')
    #管理员删除
    def test_accountDel_success(self):
        message = self.t.testAccountDel()
        self.assertIn('',message,'test_accountDel_success_测试失败。')
    #管理人员导出
    def test_accountExport_success(self):
        message = self.t.testAccountExport()
        self.assertIn('',message,'test_accountExport_success_测试失败。')
    #新增资讯
    def test_newsAdd_success(self):
        message = self.t.testNewsAdd('','','','','','','','','')
        self.assertIn('',message,'test_newsAdd_success_测试失败。')
    def test_newsAdd_fail(self):
        message = self.t.testNewsAdd('','','','','','','','','')
        self.assertIn('',message,'test_newsAdd_fail_测试失败。')
    #修改资讯
    def test_newsEdit_success(self):
        message = self.t.testNewsEdit('','','','','','','','','','')
        self.assertIn('',message,'test_newsEdit_success_测试失败。')
    def test_newsEdit_fail(self):
        message = self.t.testNewsEdit('','','','','','','','','','')
        self.assertIn('',message,'test_newsEdit_fail_测试失败。')
    #资讯列表
    def test_newsList_success(self):
        message = self.t.testNewsList('','','','')
        self.assertIn('',message,'test_newsList_success_测试失败。')
    def test_newsList_fail(self):
        message = self.t.testNewsList('','','','')
        self.assertIn('',message,'test_newsList_fail_测试失败。')
    #删除资讯
    def test_newsDel_success(self):
        message = self.t.testNewsDel('')
        self.assertIn('',message,'test_newsDel_success_测试失败。')
    def test_newsDel_fail(self):
        message = self.t.testNewsDel('')
        self.assertIn('',message,'test_newsDel_fail_测试失败。')
    #发布或不发布资讯
    def test_newsRelease_success(self):
        message = self.t.testNewsRelease('','')
        self.assertIn('',message,'test_newsRelease_success_测试失败。')
    def test_newsRelease_fail(self):
        message = self.t.testNewsRelease('','')
        self.assertIn('',message,'test_newsRelease_fail_测试失败。')
    #资讯详情
    def test_newsInfo_success(self):
        message = self.t.testNewsInfo('')
        self.assertIn('',message,'test_newsInfo_success_测试失败。')
    def test_newsInfo_fail(self):
        message = self.t.testNewsInfo('')
        self.assertIn('',message,'test_newsInfo_fail_测试失败。')
    #置顶或不置顶资讯
    def test_newsTop_success(self):
        message = self.t.testNewsTop('','')
        self.assertIn('',message,'test_newsTop_success_测试失败。')
    def test_newsTop_fail(self):
        message = self.t.testNewsTop('','')
        self.assertIn('',message,'test_newsTop_fail_测试失败。')
    #修改浏览量
    def test_newsUpdateCount_success(self):
        message = self.t.testNewsUpdateCount('','')
        self.assertIn('',message,'test_newsUpdateCount_success_测试失败。')
    def test_newsUpdateCount_fail(self):
        message = self.t.testNewsUpdateCount('','')
        self.assertIn('',message,'test_newsUpdateCount_fail_测试失败。')
    #小区账号列表
    def test_accountAreasList_success(self):
        message = self.t.testAccountAreasList('','','')
        self.assertIn('',message,'test_accountAreasList_success_测试失败。')
    def test_ccountAreasList_fail(self):
        message = self.t.testAccountAreasList('','','')
        self.assertIn('',message,'test_ccountAreasList_fail_测试失败。')
    #小区账号信息
    def test_accountAreasInfo_success(self):
        message = self.t.testAccountAreasInfo('')
        self.assertIn('',message,'test_accountAreasInfo_success_测试失败。')
    def test_accountAreasInfo_fail(self):
        message = self.t.testAccountAreasInfo('')
        self.assertIn('',message,'test_accountAreasInfo_fail_测试失败。')
    #新增小区账号
    def test_accountAreasAdd_success(self):
        message = self.t.testAccountAreasAdd('','','','','','')
        self.assertIn('',message,'test_accountAreasAdd_success_测试失败。')
    def test_accountAreasAdd_fail(self):
        message = self.t.testAccountAreasAdd('','','','','','')
        self.assertIn('',message,'test_accountAreasAdd_fail_测试失败。')
    #修改小区账号
    def test_accountAreasEdit_success(self):
        message = self.t.testAccountAreasEdit('','','','','','')
        self.assertIn('',message,'test_accountAreasEdit_success_测试失败。')
    def test_accountAreasEdit_fail(self):
        message = self.t.testAccountAreasEdit('', '', '', '', '', '')
        self.assertIn('',message,'test_accountAreasEdit_fail_测试失败。')
    #删除小区账号
    def test_accountAreasDel_success(self):
        message = self.t.testAccountAreasDel()
        self.assertIn('',message,'test_accountAreasDel_success_测试失败。')
    #导出小区账号
    def test_accountAreasExport_success(self):
        message = self.t.testAccountAreasExport()
        self.assertIn('',message,'test_accountAreasExport_success_测试失败。')

    # 权限列表

    # 角色添加
    def test_roleAdd_success(self):
        message = self.t.testRoleAdd('','','')
        self.assertIn('',message,'test_roleAdd_success_测试失败。')
    def test_roleAdd_fail(self):
        message = self.t.testRoleAdd('','','')
        self.assertIn('',message,'test_roleAdd_fail_测试失败。')
    # 修改角色
    def test_roleEdit_success(self):
        message = self.t.testRoleEdit('','','','')
        self.assertIn('',message,' test_roleEdit_success_测试失败。')
    def test_roleEdit_fail(self):
        message = self.t.testRoleEdit('', '', '', '')
        self.assertIn('',message,'test_roleEdit_fail_测试失败。')
    # 获取权限菜单
    def test_authMenuFun_success(self):
        message = self.t.testAuthMenuFun()
        self.assertIn('',message,'test_authMenuFun_success_测试失败。')
    # 删除角色
    def test_roleDel_success(self):
        message = self.t.testRoleDel()
        self.assertIn('',message,'test_roleDel_success_测试失败。')
    # 角色信息
    def test_roleInfo_success(self):
        message = self.t.testRoleInfo('')
        self.assertIn('',message,'test_roleInfo_success_测试失败。')
    def test_roleInfo_fail(self):
        message = self.t.testRoleInfo('')
        self.assertIn('',message,'test_roleInfo_fail_测试失败。')
    # 拷贝角色
    def test_roleCopy_success(self):
        message = self.t.testRoleCopy('','','','')
        self.assertIn('',message,'test_roleCopy_success_测试失败。')
    def test_roleCopy_fail(self):
        message = self.t.testRoleCopy('','','','')
        self.assertIn('',message,'test_roleCopy_fail_测试失败。')
    # 权限加载管理员
    def test_authUsers_success(self):
        message =self.t.testAuthUsers()
        self.assertIn('',message,'test_authUsers_success_测试失败。')
    def tearDown(self):
        pass