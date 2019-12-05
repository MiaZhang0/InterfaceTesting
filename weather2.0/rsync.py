import os
import platform
import socket

WIN_RSYNC = r'D:\kedale\rsync\bin\rsync.exe -avz'
LINUX_RSYNC = '/usr/bin/rsync'
#获取云服务器IP
def getHost(DN):
    try:
        result = socket.getaddrinfo(DN, None)
        ip = result[0][4][0]
    except IOError:
        print("error: connect %s fail" %DN)
    else:
        print("connect %s success" %DN)
        return ip
HOST = getHost('weather.kedalo.com')
# print(HOST)
MOD_NAME = "weather_data"

def i_system():
    return platform.system()

def choose_rsync():

    if i_system() == "Windows":
        rsync = WIN_RSYNC
    elif i_system() == "Linux":
        rsync = LINUX_RSYNC
    else:
        rsync = "Maybe something is wrong."

    return rsync

def rsync_cmd():
    remote_path = r"--password-file=/opt/rsync/config/rsync.passwd"
    #remote_path = r"/etc/rsyncd/rsyncd.secrets"
    local_path = r"/opt/weather/data/cache/*"
    username = "kedalo"
    target = []
    rsync = choose_rsync()
    params = '-av'
    port = '--port 30873'
   # cmds = '%s %s %s %s@%s::%s' %(rsync,local_path,remote_path,username,HOST,MOD_NAME)
    cmds = '%s %s %s %s %s %s@%s::%s' % (rsync, params, port, remote_path, local_path, username, HOST, MOD_NAME)
    print(cmds)
    dd = os.popen(cmds)
    for d in dd:
         print(d)
    return target