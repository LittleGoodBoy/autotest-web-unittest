import unittest
import os,sys

BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASEPATH)

from lib.pictureUtil import PictureUtil
from lib.HTMLTestRunner import HTMLTestRunner
from conf import path


class Main(object):
    def runAllCase(self):
        # 1、先清空之前的所有截图
        PictureUtil().clear_picture()
        # 2、实例化一个测试套件
        suit = unittest.TestSuite()
        # 3、获取指定路径下的所有测试用例文件
        allCase = unittest.defaultTestLoader.discover(path.CASEPATH,pattern="*.py")
        # 4、遍历测试用例文件添加到测试套件中
        for case in allCase:
            suit.addTest(case)
        # 5、以二进制写的方式打开指定路径下的测试报告文件,没有则自动创建
        reportFile = open(path.REPORTPATH,'wb')
        # 6、实例化一个测试报告执行对象
        runner = HTMLTestRunner(reportFile, verbosity=1, title=u'测试报告', description=u'用例执行情况：')
        # 7、执行对象执行测试套件中的所有测试用例
        runner.run(suit)
        # 8、刷新文件流将测试结果写入到文件,并关闭文件对象
        reportFile.flush()
        reportFile.close()

if __name__ == '__main__':
    Main().runAllCase()