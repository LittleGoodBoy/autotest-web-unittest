import logging
from logging import handlers
from conf import path

'''
    日志工具类    
'''
class LogUtil(object):

    def __init__(self,fileName,level='info',backCount=5,when='S'):
        logger = logging.getLogger()
        logger.setLevel(self.getLevel(level)) # 设置全局日志级别

        # 两种日志处理方式
        consoleLog = logging.StreamHandler()
        fileLog = handlers.TimedRotatingFileHandler(
                        filename = fileName,
                        when=when,
                        interval=1,
                        backupCount=backCount,
                        encoding='utf-8'
                    )
        # 定义日志输出格式
        logFormatter = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s : %(message)s')

        # 分别设置两个日志处理对象的输出格式
        consoleLog.setFormatter(logFormatter)
        fileLog.setFormatter(logFormatter)

        logger.addHandler(consoleLog)
        logger.addHandler(fileLog)

        # 将实例化之后的日志对象绑定到当前类的实例化对象的logger属性上
        self.logger = logger

    def getLevel(self,levelStr):
        # 定义字符串对应的日志级别关系字典
        level = {
            'debug':logging.DEBUG,
            'info':logging.INFO,
            'warn':logging.WARN,
            'error':logging.ERROR
        }
        return level.get(levelStr.lower())

# 对外提供实例化之后的logger对象,日志文件名称从定义的常量配置文件中获取
myLog = LogUtil(path.LOGPATH).logger

if __name__ == '__main__':
    myLog.info("哈哈")