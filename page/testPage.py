
from page.basePage import BasePage

class TestPage(BasePage):

    '''
        搜索框,输入值
    '''
    def addSearch(self, searchMsg):
        self.pySelenium.addText("css=>#kw",searchMsg)

    '''
        点击查询按钮
    '''
    def clickSearch(self):
        self.pySelenium.click("css=>#su")

    def getTitle(self):
        return self.pySelenium.getTitle()