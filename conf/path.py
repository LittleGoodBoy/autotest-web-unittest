import os

'''
    默认定义文件夹的绝对路径的时候,末尾加上路径分隔符,后续拼接文件时直接加上文件名称
    
    
    print(os.path.abspath(__file__)) # 当前文件的绝对路径
    os.path.sep # 获取当前操作系统的路径分隔符
'''

# 定义项目的根目录绝对路径
BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志相关
# 1、定义服务日志文件名称
LOGNAME = "server.log"
# 2、定义日志文件存储目录的绝对路径
LOGFOLDER = BASEPATH + os.sep + 'log' + os.path.sep
# 3、定义服务日志存储绝对路径
LOGPATH = LOGFOLDER + LOGNAME

# 报告相关
# 1、报告名称
REPORTNAME = 'report.html'
# 2、报告目录
REPORTFOLDER = BASEPATH + os.path.sep + 'report' + os.path.sep
# 3、报告路径
REPORTPATH = REPORTFOLDER + REPORTNAME
# 4、错误截图,图片路径
PICTUREPATH = REPORTFOLDER + 'picture' + os.path.sep

# 用例存储目录
CASEPATH = BASEPATH + os.path.sep + 'testCase' + os.path.sep


