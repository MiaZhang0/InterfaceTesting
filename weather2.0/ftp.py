from ctypes import *
import os
import sys
import ftplib
import shutil
import time
import datetime
import socket
import rsync
import logging

class MyFtp():
    ftp = ftplib.FTP()

    def __init__(self, host, port=21):
        try:
            self.ftp.connect(host, port)
        except(socket.error, socket.gaierror):
            print("error: connect %s fail" % host)
            logging.error("error: connect %s fail" % host)

    def Login(self, user, passwd):
        try:
            self.ftp.login(user, passwd)
            print(self.ftp.welcome)
            logging.info(self.ftp.welcome)
        except ftplib.error_perm:
            print("error: cannot login anonymously")
            logging.error("error: cannot login anonymously")
            self.ftp.close()

    def DownLoadFile(self, LocalFile, RemoteFile):  # 下载单个文件
        file_handler = open(LocalFile, 'wb')
        # print(file_handler)
        self.ftp.retrbinary("RETR %s" % (RemoteFile), file_handler.write)#接收服务器上文件并写入本地文件
        self.ftp.retrbinary('RETR ' + RemoteFile, file_handler.write)
        file_handler.close()
        return True

    def DownLoadFileTree1(self, LocalDir, RemoteDir):  # 下载整个目录下的文件/sevp/nwgd/nwgd/
        # print("remoteDir:", RemoteDir)
        logging.info("remoteDir:%s" %RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        # print("RemoteNames", RemoteNames)
        getFile = open(r'/opt/weather/data/grb.txt',"r",encoding="utf-8")
        resp = getFile.read()
        getFile.close()
        fileName=''
        # 是否同步
        tb = False
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            fileName+=file+'\r\n'
            fitem = file.split(".")
            if file not in resp and "GRB2" == fitem[1]:
                self.DownLoadFile(Local, file)
                # print('Downloading ' + file)
                logging.info('Downloading ' + file)
                tb = True
        if (tb):
            updateFile = open(r'/opt/weather/data/grb.txt', "w", encoding="utf-8")
            updateFile.write(fileName)
            updateFile.close()
        self.ftp.cwd("..")
        return tb

    def DownLoadFileTree6(self, LocalDir, RemoteDir):  # 下载整个目录下的文件/sevp/nwgd/nwgd/
        # print("remoteDir:", RemoteDir)
        logging.info("remoteDir:"+ RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        # print("RemoteNames", RemoteNames)
        getFile = open(r'/opt/weather/data/txt1.txt', "r", encoding="utf-8")
        resp = getFile.read()
        getFile.close()
        fileName = ''
        # 是否同步
        tb = False
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            fileName += file + '\r\n'
            fitem = file.split(".")
            # print(fitem)
            if file not in resp and "TXT" == fitem[1]:
                self.DownLoadFile(Local, file)
                # print('Downloading ' + file)
                logging.info('Downloading ' + file)
                tb = True
        if (tb):
            updateFile = open(r'/opt/weather/data/txt1.txt', "w", encoding="utf-8")
            updateFile.write(fileName)
            updateFile.close()
        self.ftp.cwd("..")
        return tb

    def DownLoadFileTree2(self, LocalDir, RemoteDir):  # 下载整个目录下的文件/pprog/fdlib/
        # print("remoteDir:", RemoteDir)
        logging.info("remoteDir:"+ RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        # print("RemoteNames", RemoteNames)
        getFile = open(r'/opt/weather/data/doc1.txt', "r", encoding="utf-8")
        resp = getFile.read()
        getFile.close()
        fileName = ''
        # 是否同步
        tb = False
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            fileName += file + '\r\n'
            if file not in resp:
                self.DownLoadFile(Local, file)
                # print('Downloading ' + file)
                logging.info('Downloading ' + file)
                tb = True
        if (tb):
            updateFile = open(r'/opt/weather/data/doc1.txt', "w", encoding="utf-8")
            updateFile.write(fileName)
            updateFile.close()
        self.ftp.cwd("..")
        return tb

    def DownLoadFileTree3(self, LocalDir, RemoteDir):  # 下载整个目录下的文件/pprog/fclib/
        # print("remoteDir:", RemoteDir)
        logging.info("remoteDir:"+ RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        # print("RemoteNames", RemoteNames)
        getFile = open(r'/opt/weather/data/doc2.txt', "r", encoding="utf-8")
        resp = getFile.read()
        getFile.close()
        fileName = ''
        # 是否同步
        tb = False
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            fileName += file + '\r\n'
            if file not in resp:
                self.DownLoadFile(Local, file)
                # print('Downloading ' + file)
                logging.info('Downloading ' + file)
                tb = True
        if (tb):
            updateFile = open(r'/opt/weather/data/doc2.txt', "w", encoding="utf-8")
            updateFile.write(fileName)
            updateFile.close()
        self.ftp.cwd("..")
        return tb
    def DownLoadFileTree4(self,LocalDir,RemoteDir):
        # print("remoteDir:", RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        now_time = datetime.datetime.now()
        current_date = now_time.strftime("%Y%m%d")
        if current_date in RemoteNames:
            current_dir = RemoteDir + current_date
            # print("remoteDir:",current_dir)
            logging.info("remoteDir:"+current_dir)
        else:
            last_day = now_time - datetime.timedelta(days=1)
            current_dir = RemoteDir + last_day.strftime("%Y%m%d")
            # print("remoteDir:",current_dir)
            logging.info("remoteDir:"+current_dir)
        self.ftp.cwd(current_dir)
        RemoteFileNames = self.ftp.nlst()
        getFile = open(r'/opt/weather/data/babj.txt', "r", encoding="utf-8")
        resp = getFile.read()
        getFile.close()
        fileName = ''
        # 是否同步
        tb = False
        for file in RemoteFileNames:
            Local = os.path.join(LocalDir, file)
            fileName += file + '\r\n'
            if file not in resp:
                self.DownLoadFile(Local, file)
                # print('Downloading ' + file)
                logging.info('Downloading ' + file)
                tb = True
        if (tb):
            updateFile = open(r'/opt/weather/data/babj.txt', "w", encoding="utf-8")
            updateFile.write(fileName)
            updateFile.close()
        self.ftp.cwd("..")
        return tb

    def DownLoadFileTree5(self, LocalDir, RemoteDir):  # 下载整个目录下的文件/sevp/spcc/
        # print("remoteDir:", RemoteDir)
        logging.info("remoteDir:"+ RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        # print("RemoteNames", RemoteNames)
        getFile = open(r'/opt/weather/data/txt2.txt', "r", encoding="utf-8")
        resp = getFile.read()
        getFile.close()
        fileName = ''
        # 是否同步
        tb = False
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            fileName += file + '\r\n'
            if file not in resp:
                self.DownLoadFile(Local, file)
                # print('Downloading ' + file)
                logging.info('Downloading ' + file)
                tb = True
        if (tb):
            updateFile = open(r'/opt/weather/data/txt2.txt', "w", encoding="utf-8")
            updateFile.write(fileName)
            updateFile.close()
        self.ftp.cwd("..")
        return tb

    def Del_file(self, delDir_path):
        delDir = delDir_path
        delList = os.listdir(delDir)
        for f in delList:
            filePath = os.path.join(delDir, f)
            if os.path.isfile(filePath):
                os.remove(filePath)
                # print(filePath + " was removed!")
            elif os.path.isdir(filePath):
                shutil.rmtree(filePath, True)
                # print("Directory: " + filePath + " was removed!")

    def close(self):
        self.ftp.quit()

if __name__ == "__main__":
    while 1:
        log_filename = r"/opt/rsync/logging_ftp.log"
        log_format = "%(filename)s [%(asctime)s] [%(levelname)s] %(message)s"
        logging.basicConfig(filename=log_filename, filemode="w",format=log_format, datefmt="%Y-%m-%d %H:%M:%S %p",
                            level=logging.DEBUG)
        ftp = MyFtp('10.194.17.12')
        ftp.Login('bfymws', 'bfym0414')
        ftp.DownLoadFileTree1(r'/opt/weather/data/cache/grb', '/sevp/nwgd/nwgd/')#从目标目录下载到本地目录grb
        # ftp.DownLoadFileTree6(r'/opt/weather/data/cache/txt', '/sevp/nwgd/nwgd/')#txt1
        # ftp.DownLoadFileTree2(r'/opt/weather/data/cache/Cdoc', '/pprog/fdlib/')  # 从目标目录下载到本地目录doc1
        # ftp.DownLoadFileTree3(r'/opt/weather/data/cache/Cdoc', '/pprog/fclib/')  # fd市级产品-BFYM ；fc县级产品 - 6县2区doc2
        # ftp.DownLoadFileTree4(r'/opt/weather/data/cache/Dbabj', '/sevp/nwgd/')  # 从目标目录下载到本地目录babj
        # ftp.DownLoadFileTree5(r'/opt/weather/data/cache/txt', '/sevp/spcc/') #从目标目录下载到本地目录txt2
        ftp.close()
        print("下载文件完成!")
        res = rsync.rsync_cmd()  # 同步上传文件及文件夹
        if res is not None:
            delFile_path1= r'/opt/weather/data/cache/grb'
            ftp.Del_file(delFile_path1)
            delFile_path3 = r'/opt/weather/data/cache/txt'
            ftp.Del_file(delFile_path3)
            # delFile_path5 = r'/opt/weather/data/cache/Dbabj'
            # ftp.Del_file(delFile_path5)
            # delFile_path6 = r'/opt/weather/data/cache/Cdoc'
            # ftp.Del_file(delFile_path6)
            print("缓存文件夹已清空")
        # print("同步文件完成!")
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info("此次文件同步完成的时间是：%s"%time_now)
        print("此次文件同步完成的时间是：%s"%time_now)
        time.sleep(30)