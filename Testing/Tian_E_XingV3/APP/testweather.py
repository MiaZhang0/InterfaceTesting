from Tian_E_XingV3.APP import testcases
import json
'''
json.loads(json_str) json字符串转换成字典
json.dumps(dict) 字典转换成json字符串
'''
import sys


class Logger(object):
    def __init__(self, logFile="Default.log"):
        self.terminal = sys.stdout
        self.log = open(logFile, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass




# 实例化对象
obj = testcases.TestModuleClass()
# message1 = obj.testLocalForecast_meta('104.017663','30.660655')
# # print(message)
#
# l1 = Logger("log1.txt")
# l1.write(message1)

message2 = obj.testScreenNow('104.017663','30.660655','510106')
l2 = Logger("log2.txt")
l2.write(message2)