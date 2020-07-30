from ftplib import FTP
import pymysql


def upload(f, remote_path, local_path):
    fp = open(local_path, 'rb')
    buf_size = 1024
    # 如果参数pasv为真，打开被动模式传输（pasv mode）,否则关闭被动传输模式
    f.set_pasv(0)
    f.storbinary('STOR {}'.format(remote_path), fp, buf_size)
    fp.close()


def download(f, remote_path, local_path):
    fp = open(local_path, 'wb')
    buf_size = 1024
    # 如果参数pasv为真，打开被动模式传输（pasv mode）,否则关闭被动传输模式
    f.set_pasv(0)
    f.retrbinary('RETR {}'.format(remote_path), fp.write, buf_size)
    fp.close()


def db_con():
    # version = 'v3.0.1.513'
    # content = '''天e行防灾减灾大数据平台移动端内测版V3.0.1.513
    # 更新说明：
    # 1. 更新项目详情数据
    # 2. 更新逐小时预报数据
    # 3. 优化页面图标和修复缺陷
    # '''
    # url = 'http://app.kedalo.com:8000/kdl20000a02_V3.0.1.513.apk'

    db = pymysql.connect('weather.kedalo.com', 'root', 'EoOer1vpxwQM3WeK', 'yaan')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print("Database version : %s " % data)

    # sql语句，修改
    sql = '''update kedalo_sys_version set lvl = 'v3.0.1.629',
    content = '天e行防灾减灾大数据平台移动端内测版V3.0.1.629
    更新说明：
1.完善根据行政区划筛选监测项目功能
2.修复缺陷及优化界面',
    url = 'http://app.kedalo.com:8000/kdl20000a02.apk'
    where version_id = 2
    '''
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print('执行成功')
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭连接
    db.close()


if __name__ == '__main__':
    try:
        ftp = FTP()
        # 打开调试级别2，显示详细信息
        # ftp.set_debuglevel(2)
        # 服务器IP和端口
        ftp.connect('app.kedalo.com', 21)
        ftp.login('ftpuser', '11nadXbkQx9Zet2A')
        # 切换目录，上传文件的目的地目录
        ftp.cwd('/')
        remote_path = 'kdl20000a02.apk'
        # print(remote_path)
        local_path = r'E:\testpack\kdl20000a02.apk'
        upload(ftp, remote_path, local_path)
        ftp.close()
        print('文件上传完成')
    except Exception as err:
        print('文件上传失败', err)
    db_con()