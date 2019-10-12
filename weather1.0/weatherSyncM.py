#encoding=utf-8
import win32serviceutil
import win32service
import win32event
import  win32api
import logging
import inspect
import time
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='C:\weather_service.log',
                    filemode='a')

class WeatherSyncManager(win32serviceutil.ServiceFramework):
    _svc_name_ = "Weather Sync Agent Manager"  # 服务名
    _svc_display_name_ = "Weather Sync Agent Manager"  # 服务在windows系统中显示的名称
    _svc_description_ = "气象数据同步服务"  # 服务的描述

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.run = True

    def _getLogger(self):
        logger = logging.getLogger('[WeatherSyncManager]')

        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        handler = logging.FileHandler(os.path.join(dirpath, "service.log"))

        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger

    def SvcDoRun(self):
        logging.info('Windows 服务程序启动...')
        while self.run:
            print('monitor testing')
            time.sleep(3)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.run = False


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(WeatherSyncManager)