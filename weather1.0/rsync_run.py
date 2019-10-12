import os
import platform
import time

WIN_RSYNC = r'G:\Kedalo\DebugWeather\cwRsync\bin\rsync.exe -avz'
LINUX_RSYNC = '/usr/bin/rsync'
#HOST = '172.16.1.135'
HOST = '118.123.236.132'
MOD_NAME = "weather_data"


def i_system():
    return platform.system()

def choose_rsync():
    # rsync - z - -password - file = D:\kedalo\weather\rsync.password
    # D:\weather\kedalo
    # kedalo @ 172.16.1.135::weather_data

    # E:\FTPlocalpath\test     / opt / weather / data / rsync.password
    # kedalo @ 118.123.236.132::test
    if i_system() == "Windows":
        rsync = WIN_RSYNC
    elif i_system() == "Linux":
        rsync = LINUX_RSYNC
    else:
        rsync = "Maybe something is wrong."

    return rsync

def rsync_cmd():
    remote_path = r"--password-file=/cygdrive/d/weather/rsync.password"
    #remote_path = r"/etc/rsyncd/rsyncd.secrets"
    local_path = r"/cygdrive/e/FTPlocalpath/test/*"
    username = "kedalo"
    target = []
    rsync = choose_rsync()
   # cmds = '%s %s %s %s@%s::%s' %(rsync,local_path,remote_path,username,HOST,MOD_NAME)
    data="/opt/weather/data"
    cmds = '%s %s %s %s@%s::%s' % (rsync,remote_path,local_path,username, HOST, MOD_NAME)
    # os.system('cmd')
    # print(cmds)
    dd = os.popen(cmds)
    # print(dd)
    for d in dd:
        print(d)
        target.append(d.strip().split(' '))
    # print(target)
    return target
    # if target is not None:


    # for i in target:
    #     d4 = int(i[-4].replace(',', ''))
    #     t = str(i[-3] + ' ' + i[-2])
    #     t1 = time.strptime(t, '%Y/%m/%d %H:%M:%S')
    #     t3 = int(time.mktime(t1))
    #     print(i[-1], t3, d4)

def main():
    rsync_cmd()



if __name__ == '__main__':
    main()