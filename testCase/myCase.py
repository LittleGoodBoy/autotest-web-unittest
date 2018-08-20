import unittest
from page.testPage import TestPage


class MyCase(unittest.TestCase):
    '''
        类方法,在所有测试用例执行之前执行,只执行一次
    '''
    @classmethod
    def setUpClass(cls):
        # 实例化测试页面,并请求到指定页面
        cls.testPage = TestPage()
        cls.testPage.open('https://www.baidu.com')

    '''
        测试用例1
    '''
    def test_a_study(self):

        self.testPage.addSearch("selenium")
        self.testPage.clickSearch()
        # 获取当前页面的title
        currentTitle = self.testPage.getTitle()

        print(currentTitle)
        # 断言title是否为指定内容
        self.assertTrue(currentTitle is "selenium_百度搜索")

    '''
        类方法,在所有测试用例执行之后执行,只执行一次
    '''
    @classmethod
    def tearDownClass(cls):
        cls.testPage.quit() # 关闭驱动


if __name__ == '__main__':
    unittest.main() # 运行case