from ctypes import *
import os
import sys
import ftplib
import shutil
import time
import datetime
import rsync_run
import socket

class MyFtp():
    # dict_file_pre = {}
    ftp = ftplib.FTP()
    # list_file_date = []
    # ftp = ftplib.FTP_TLS()

    def __init__(self, host, port=21):
        try:
            self.ftp.connect(host, port)
        except(socket.error,socket.gaierror):
            print("error: connect %s fail" %host )

    def Login(self, user, passwd):
        try:
            self.ftp.login(user, passwd)
            print(self.ftp.welcome)
        except ftplib.error_perm:
            print("error: cannot login anonymously")
            ftp.close()
    def DownLoadFile(self, LocalFile, RemoteFile):  # 下载单个文件
        # fitem = RemoteFile.split("_")
        # fkey = fitem[0] + "_" + fitem[1] + "_" + fitem[2]+ "_" + fitem[3] + "_" + fitem[4]
        #     # ftime = fitem[5]
        # ftime = datetime.datetime.strptime(fitem[5], "%Y%m%d%H%M%S")
        # #print(ftime)
        # if fkey in self.dict_file_pre and self.dict_file_pre[fkey] >= ftime:
        #     return True
        file_handler = open(LocalFile, 'wb')
        # print(file_handler)
        self.ftp.retrbinary("RETR %s" % (RemoteFile), file_handler.write)#接收服务器上文件并写入本地文件
        self.ftp.retrbinary('RETR ' + RemoteFile, file_handler.write)
        file_handler.close()
        # self.dict_file_pre[fkey] = ftime
        # print(self.dict_file_pre)
        # return True

    def DownLoadFileTree(self, LocalDir, RemoteDir):  # 下载整个目录下的文件
        # print("remoteDir:", RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        # print("RemoteNames", RemoteNames)
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            # print(self.ftp.nlst(file))
            # print(file)
            # print(file.find(".") == -1)
            if file.find(".") == -1:
                self.DownLoadFileTree(Local, file)
                # print(self.DownLoadFileTree(Local, file))
            else:
                self.DownLoadFile(Local, file)
        self.ftp.cwd("..")
        return

    def Del_file(self,delDir_path):
        delDir = delDir_path
        delList = os.listdir(delDir)
        for f in delList:
            filePath = os.path.join(delDir,f)
            if os.path.isfile(filePath):
                os.remove(filePath)
                print(filePath + "was removed!")
            elif os.path.isdir(filePath):
                shutil.rmtree(filePath,True)
                print("Directory: " + filePath + "was removed!")

    def close(self):
        self.ftp.quit()

if __name__ == "__main__":
    ftp = MyFtp('192.168.239.1')
    ftp.Login('ftp_test', 'Ftp1234')
    ftp.DownLoadFileTree(r'E:\FTPlocalpath\test', '/weather/')  # 从目标目录下载到本地目录d盘
    ftp.DownLoadFileTree(r'E:\FTPlocalpath\test','/sevp/nwgd/')
    ftp.DownLoadFileTree(r'E:\FTPlocalpath\test','/bccd/sevp/')
    ftp.close()

    res = rsync_run.rsync_cmd()  #同步上传文件及文件夹
    # print(res)
    print("下载文件完成!同步中，请等待···，10s后删除缓存文件")
    time.sleep(10)
    if res is not None:
        delFile_path = r"E:\FTPlocalpath\test"
        ftp.Del_file(delFile_path)
        print("缓存文件夹已清空")
