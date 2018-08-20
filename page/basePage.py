
from lib.pyselenium import PySelenium

'''
    所有页面的基类,封装了一下常用并且通用的方法,并且实例化了浏览器驱动对象
'''
class BasePage(object):
    def __init__(self):
        self.pySelenium = PySelenium('chrome')

    def open(self, url):
        self.pySelenium.openUrl(url)

    def close(self):
        self.pySelenium.close()

    def quit(self):
        self.pySelenium.quit()

    def swicth_windows(self):
        self.pySelenium.openNewWindow()