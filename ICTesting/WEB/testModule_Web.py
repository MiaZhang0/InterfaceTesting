import requests

class TestModuleClass():
    def __init__(self):
        self.host = 'http://192.168.0.234:8099'
    #发送手机验证码
    def testSendCode(self,phone):
        url = self.host + '/sendCode'
        datas = {'phone':phone}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #控制台登录，返回token
    def testMsgLogin(self,phone,code):
        url = self.host + '/msgLogin'
        datas = {'phone':phone,'code':code}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #普通登录
    def testLogin(self,username,password):
        url = self.host + '/login'
        datas = {'username':username,'password':password}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #登出
    def testLogout(self):
        url = self.host + '/manage/common/loginOut'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #获取菜单权限
    def testMenuAuthority(self,menuld):
        url = self.host + '/manage/common/auth'
        datas = {'menuld':menuld}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #居民查询条件，小区列表
    def testAreasList(self):
        url = self.host + '/manage/common/areasList'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #添加资讯草稿
    def testNewsDraft(self,title,image,cognateId,link,source,top,content):
        url = self.host + '/manage/common/newsDraft'
        datas = {'title':title,'image':image,'cognateId':cognateId,'link':link,'source':source,'top':top,'content':content}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #检测是否有资讯草稿
    def testFindNewsDraft(self):
        url = self.host + '/manage/common/FindNewsDraft'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #小区单位信息
    def testCellUnitInfo(self):
        url = self.host + '/manage/bulletin/release/manage/areas/info'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #图片下载
    def testImageDownload(self,path):
        url = self.host + '/manage/common/image'
        datas = {'path':path}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #上传图片
    def testImageUpload(self,file,type):
        url = self.host + '/manage/common/upload'
        datas = {'file':file,'type':type}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #获取当前权限方法data=[functionId,action,name,createTime,menuId,permission]
    def testAuthList(self,code,msg,list):
        url = self.host + '/manage/common/authList'
        datas = {'code':code,'msg':msg,'data':list}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #删除小区
    def testCellDel(self,ids):
        url = self.host + '/manage/areas/del'
        header = {'Content-type':'application/json'}
        datas = {'ids':ids}
        r = requests.get(url,params=datas,headers=header)
        message = r.text
        print(message)
        return message
    #导出小区列表数据
    def testExportData(self):
        url = self.host + '/manage/areas/export'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #小区列表
    def testCellList(self,pageNo,pageSize,name):
        url = self.host + '/manage/areas/list'
        datas = {'pageNo':pageNo,'pageSize':pageSize,'name':name}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #新增小区
    def testCellAdd(self,city,area,street,lat,lng,name,contact,company,province,address,images):
        url = self.host + '/manage/areas/add'
        datas = {'city':city,'area':area,'street':street,'lat':lat,'lng':lng,'name':name,'contact':contact,'company':company,'province':province,'address':address,'images':images}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #修改小区
    def testCellEdit(self,areasId,name,contact,company,images,province,city,area,street,lat,lng,address):
        url = self.host + '/manage/areas/edit'
        datas = {'areasId':areasId,'name':name,'contact':contact,'company':company,'images':images,'province':province,'city':city,'area':area,'street':street,'lat':lat,'lng':lng,'address':address}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #轮播详情
    def testBannerInfo(self,bannerId):
        url = self.host + '/manage/banner/info'
        datas = {'bannerId':bannerId}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #轮播列表
    def testBannerList(self,pageNo,pageSize,title,status):
        url = self.host + '/manage/banner/list'
        datas = {'pageNo':pageNo,'pageSize':pageSize,'titile':title,'status':status}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #添加轮播
    def testBannerAdd(self,title,image,type,link):
        url = self.host + '/manage/banner/add'
        datas = {'title':title,'image':image,'type':type,'link':link}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #编辑轮播
    def testBannerEdit(self,bannerId,image,type,link,title):
        url = self.host + '/manage/banner/edit'
        datas = {'bannerId':bannerId,'image':image,'type':type,'link':link,'title':title}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #删除轮播
    def testBannerDel(self):
        url = self.host + '/manage/banner/del'
        header = {'Content-type':'application/json'}
        r = requests.post(url,headers=header)
        message = r.text
        print(message)
        return message
    #发布轮播
    def testBannerRelease(self,status,bannerId):
        url = self.host + '/manage/banner/release'
        datas = {'status':status,'bannerId':bannerId}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #新建社区
    def testCommunityAdd(self,address,area,city,lat,lng,province,street,contact1,images,name,streetDirector,contact2,job,):
        url = self.host + '/manage/community/add'
        datas = {'address':address,'area':area,'city':city,'lat':lat,'lng':lng,'province':province,'street':street,'contact':contact1,'images':images,'name':name,'streetDirector':streetDirector,'contact':contact2,'job':job}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #社区详情
    def testCommunityInfo(self,communityId):
        url = self.host + '/manage/community/info'
        datas = {'communityId':communityId}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #编辑社区，请求参数地址对象，社区对象，员工对象
    def testCommunityEdit(self):
        url = self.host + '/manage/community/edit'
        datas = {}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #公告列表
    def testNoticeList(self,content,status,pageNo,pageSize):
        url = self.host + ''
        datas = {'content':content,'status':status,'pageNo':pageNo,'pageSize':pageSize}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #新增公告
    def testNoticeAdd(self,type,content,top):
        url = self.host + '/manage/bulletin/add'
        datas = {'type':type,'content':content,'top':top}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #公告详情
    def testNoticeInfo(self,bulletinId):
        url = self.host + '/manage/bulletin/info'
        datas = {'bulletinId':bulletinId}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #公告修改
    def testNoticeEdit(self,bulletinId,type,content,top):
        url = self.host + '/manage/bulletin/edit'
        datas = {'bulletinId':bulletinId,'type':type,'content':content,'top':top}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #公告置顶
    def testNoticeTop(self,top,bulletinId):
        url = self.host + '/manage/bulletin/top'
        datas = {'top':top,'bulletinId':bulletinId}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #公告发布
    def testNoticeRelease(self,status,bulletinId):
        url = self.host + '/manage/bulletin/release'
        datas = {'status':status,'bulletinId':bulletinId}
        r = requests.get(url, params=datas)
        message = r.text
        print(message)
        return message
    #公告删除
    def testNoticeDel(self):
        url = self.host + '/manage/bulletin/del'
        r = requests.post(url)
        message = r.text
        print(message)
        return message
    #导出居民
    def testResidentExport(self):
        url = self.host + '/manage/resident/export'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #新增居民
    def testResidentAdd(self,name,idCard,contact,floor,modular,number,gender):
        url = self.host + '/manage/resident/add'
        datas = {'name':name,'idCard':idCard,'contact':contact,'floor':floor,'modular':modular,'number':number,'gender':gender}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #删除居民
    def testResidentDel(self,ids):
        url = self.host + '/manage/resident/del'
        datas = {'ids':ids}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #编辑居民
    def testResidentEdit(self,householdId,name,gender,idCard,contact,floor,modular,number):
        url = self.host + '/manage/resident/edit'
        datas = {'householdId':householdId,'name':name,'gender':gender,'idCard':idCard,'contact':contact,'floor':floor,'modular':modular,'number':number}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #居民列表
    def testResidentList(self,pageNo,pageSize,name,areasId,floor,modular):
        url = self.host + '/manage/resident/list'
        datas = {'pageNo':pageNo,'pageSize':pageSize,'name':name,'areasId':areasId,'floor':floor,'modular':modular}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #居民信息
    def testResidentInfo(self,householdId):
        url = self.host + '/manage/resident/info'
        datas = {'householdId':householdId}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #社区或小区管理员管理
    def testManageList(self,name,pageNo,pageSize):
        url = self.host + '/manage/bulletin/release/manage/account/list'
        datas = {'name':name,'pageNo':pageNo,'pageSize':pageSize}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #管理员详情
    def testAccountInfo(self,userId):
        url = self.host + '/manage/account/info'
        datas = {'userId':userId}
        r = requests.get(url, params=datas)
        message = r.text
        print(message)
        return message
    #新增管理员
    def testAccountAdd(self,name,username,password,roleId,phone):
        url = self.host + '/manage/account/add'
        datas = {'name':name,'username':username,'password':password,'roleId':roleId,'phone':phone}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #管理员编辑
    def testAccountEdit(self,name,phone,userId,roleId,password):
        url = self.host + '/manage/account/edit'
        datas = {'name':name,'phone':phone,'userId':userId,'roleId':roleId,'password':password}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #管理员删除
    def testAccountDel(self):
        url = self.host + '/manage/account/del'
        r = requests.post(url)
        message = r.text
        print(message)
        return message
    #管理人员导出
    def testAccountExport(self):
        url = self.host + '/manage/account/export'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #新增资讯
    def testNewsAdd(self,title,image,cognateId,link,top,pub_time,source,content,status):
        url = self.host + '/manage/news/add'
        datas = {'title':title,'image':image,'cognateId':cognateId,'link':link,'top':top,'pub_time':pub_time,'source':source,'content':content,'status':status}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #修改资讯
    def testNewsEdit(self,title,image,cognateId,link,top,pub_time,source,content,status,newsId):
        url = self.host + '/manage/news/edit'
        datas = {'title':title,'image':image,'cognateId':cognateId,'link':link,'top':top,'pub_time':pub_time,'source':source,'content':content,'status':status,'newsId':newsId}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #资讯列表
    def testNewsList(self,pageNo,pageSize,title,status):
        url = self.host + '/manage/news/list'
        datas = {'pageNo':pageNo,'pageSize':pageSize,'title':title,'status':status}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #删除资讯
    def testNewsDel(self,ids):
        url = self.host + '/manage/news/del'
        datas = {'ids':ids}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #发布或不发布资讯
    def testNewsRelease(self,status,newsId):
        url = self.host + '/manage/news/release'
        datas = {'status':status,'newsId':newsId}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #资讯详情
    def testNewsInfo(self,newsId):
        url = self.host + '/manage/news/info'
        datas = {'newsId':newsId}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #置顶或不置顶资讯
    def testNewsTop(self,top,newsId):
        url = self.host + '/manage/news/top'
        datas = {'top':top,'newsId':newsId}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #修改浏览量
    def testNewsUpdateCount(self,newsId,count):
        url = self.host + '/manage/news/updateCount'
        datas = {'newsId':newsId,'count':count}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #小区账号列表,name对象（pageNo,pageSize）
    def testAccountAreasList(self,name,pageNo,pageSize):
        url = self.host + '/manage/accountAreas/list'
        datas = {'name':name,'pageNo':pageNo,'pageSize':pageSize}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #小区账号信息
    def testAccountAreasInfo(self,userId):
        url = self.host + '/manage/accountAreas/info'
        datas = {'userId':userId}
        r = requests.get(url, params=datas)
        message = r.text
        print(message)
        return message
    #新增小区账号,name对象
    def testAccountAreasAdd(self,name,username,password,roleId,phone,areasId):
        url = self.host + '/manage/accountAreas/add'
        datas = {'name':name,'username':username,'password':password,'roleId':roleId,'phone':phone,'areasId':areasId}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #修改小区账号，name对象
    def testAccountAreasEdit(self,name,password,roleId,phone,areasId,userId):
        url = self.host + '/manage/accountAreas/edit'
        datas = {'name':name,'password':password,'roleId':roleId,'phone':phone,'areasId':areasId,'userId':userId}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #删除小区账号
    def testAccountAreasDel(self):
        url = self.host + '/manage/accountAreas/del'
        r = requests.post(url)
        message = r.text
        print(message)
        return message
    #导出小区账号
    def testAccountAreasExport(self):
        url = self.host + '/manage/accountAreas/export'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #权限列表

    #角色添加,参数：list[id,list[id,list[id]]]
    def testRoleAdd(self,name,users,desc):
        url = self.host + '/manage/role/add'
        datas = {}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #修改角色,参数：list[id,list[id,list[id]]]
    def testRoleEdit(self,roleId,name,desc,userId):
        url = self.host + '/manage/role/edit'
        datas = {}
        r = requests.post(url, data=datas)
        message = r.text
        print(message)
        return message
    #获取权限菜单
    def testAuthMenuFun(self):
        url = self.host + '/manage/common/authMenuFun'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
    #删除角色，int型的数组【1,2,3】
    def testRoleDel(self):
        url = self.host + '/manage/role/del'
        datas = {}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #角色信息
    def testRoleInfo(self,roleId):
        url = self.host + '/manage/role/info'
        datas = {'roleId':roleId}
        r = requests.get(url,params=datas)
        message = r.text
        print(message)
        return message
    #拷贝角色
    def testRoleCopy(self,name,desc,type,copyId):
        url = self.host + '/manage/role/copy'
        datas = {'name':name,'desc':desc,'type':type,'copyId':copyId}
        r = requests.post(url,data=datas)
        message = r.text
        print(message)
        return message
    #权限加载管理员
    def testAuthUsers(self):
        url = self.host + '/manage/common/authUsers'
        r = requests.get(url)
        message = r.text
        print(message)
        return message
