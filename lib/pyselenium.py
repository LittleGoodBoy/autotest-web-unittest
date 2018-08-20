from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

'''
    对selenium进行二次封装
'''
class PySelenium(object):

    '''
        初始化,实例化浏览器驱动对象
    '''
    def __init__(self, browser='ff'):
        if browser == 'ff' or browser == 'firefox': # 火狐
            driver = webdriver.Firefox()
        elif browser == 'chrome': # 谷歌
            option = webdriver.ChromeOptions()
            option.add_argument("--start-maximized")
            driver = webdriver.Chrome(chrome_options=option)
        elif browser == 'ie' | browser == 'internet explorer': # IE
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        elif browser == 'edge':
            driver = webdriver.Edge()

        try:
            self.driver = driver
        except Exception:
            # 手动抛出异常
            raise NameError(
                "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'phantomjs', 'edge' or 'chrome'." % browser)


    '''
        设置元素等待
    '''
    def elementWait(self, css, secs=5):
        # 判断表达式是否包含指定字符
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        # 提取元素定位方式和定位表达式
        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located(By.ID,value))
        elif by == 'name':
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located(By.NAME,value))
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    '''
        获取指定元素对象
            表达式：  by=>value （by为定位方式,value为定位方式的表达式,例如:按照id定位某个元素,id=>"#"）
    '''
    def getElement(self, css):
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by == 'name':
            element = self.driver.find_element_by_name(value)
        elif by == 'class':
            element = self.driver.find_element_by_class_name(value)
        elif by == 'link_text':
            element = self.driver.find_element_by_link_text(value)
        elif by == 'xpath':
            element = self.driver.find_element_by_xpath(value)
        elif by == 'css':
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    '''
        请求/打开指定链接
    '''
    def openUrl(self, url):
        self.driver.get(url)

    '''
        窗口最大化
    '''
    def maxWindows(self):
        self.driver.maximize_window()

    '''
        设置窗口指定宽高
    '''
    def setWindowsSize(self, wide, high):
        self.driver.set_window_size(width=wide,height=high)

    '''
        添加文本到input
    '''
    def addText(self, css, massage):
        self.elementWait(css)
        input = self.getElement(css)
        input.send_keys(massage)

    '''
        清空input中的文本
    '''
    def clear(self, css):
        self.elementWait(css)
        self.getElement(css).clear()

    '''
        鼠标左键单击
    '''
    def click(self, css):
        self.elementWait(css)
        self.getElement(css).click()

    '''
        鼠标右键单击
    '''
    def rightClick(self, css):
        self.elementWait(css)
        ActionChains(self.driver).context_click(self.getElement(css)).perform()

    '''
        移动鼠标到指定元素(默认在元素的中间位置)
    '''
    def moveToTargetElement(self, css):
        self.elementWait(css)
        ActionChains(self.driver).move_to_element(self.getElement(css)).perform()

    '''
        移动鼠标到指定元素,并且指定位于元素的x,y偏移量(偏移量相对于元素的左上角)
    '''
    def moveToTargetElementWithOffset(self, css, xoffset, yoffset):
        self.elementWait(css)
        ActionChains(self.driver).move_to_element_with_offset(self.getElement(css), xoffset, yoffset).perform()

    '''
        鼠标左键双击
    '''
    def doubleClick(self, css):
        self.elementWait(css)
        ActionChains(self.driver).double_click(self.getElement(css)).perform()

    '''
        拖拽元素到指定元素处
    '''
    def dragAndDropToElement(self, sourceCss, targetCss):
        self.elementWait(sourceCss)
        self.elementWait(targetCss)
        ActionChains(self.driver).drag_and_drop(self.getElement(sourceCss),self.getElement(targetCss)).perform()

    '''
        拖拽元素指定偏移(该偏移是相对于当前鼠标的坐标偏移量)
    '''
    def dragAndDropToOffset(self, sourceCss, xoffset, yoffset):
        self.elementWait(sourceCss)
        ActionChains(self.driver).drag_and_drop_by_offset(self.getElement(sourceCss), xoffset, yoffset).perform()

    '''
        鼠标左键点击链接文本
    '''
    def clickLinkText(self, text):
        self.driver.find_element_by_partial_link_text(text).click()

    '''
        关闭当前窗口
    '''
    def close(self):
        self.driver.close()

    '''
        关闭浏览器驱动
    '''
    def quit(self):
        self.driver.quit()

    '''
        提交指定表单
    '''
    def submit(self, css):
        self.elementWait(css)
        self.getElement(css).submit()

    '''
        刷新当前页面,相当于点击F5
    '''
    def F5(self):
        self.driver.refresh()

    '''
        执行指定的js代码
    '''
    def js(self, javaScript):
        self.driver.execute_script(javaScript)

    '''
        获取指定元素的某个属性值
    '''
    def getAttribute(self, css, attr):
        self.elementWait(css)
        self.getElement(css).get_attribute(attr)

    '''
        获取指定元素的文本内容,即value属性值
    '''
    def getText(self, css):
        self.elementWait(css)
        self.getElement(css).text

    '''
        判断元素是否可见
    '''
    def isDisplay(self, css):
        self.elementWait(css)
        return self.getElement(css).is_displayed()

    '''
        判断元素是否启用
    '''
    def isEnabled(self, css):
        self.elementWait(css)
        return self.getElement(css).is_enabled()

    '''
        判断元素是否选中,一般用于验证checkbox和radio
    '''
    def isSelected(self, css):
        self.elementWait(css)
        return self.getElement(css).is_selected()

    '''
        获取当前页面的title
    '''
    def getTitle(self):
        return self.driver.title

    '''
        获取当前页面的url
    '''
    def getCurrentUrl(self):
        return self.driver.current_url

    '''
        截图,保存到指定路径下文件中
    '''
    def getScreenshot(self, fullFileName):
        self.driver.get_screenshot_as_file(fullFileName)

    '''
        全局等待,Implicitly wait.All elements on the page.
    '''
    def wait(self, secs):
        self.driver.implicitly_wait(secs)

    '''
        弹框警告-确认
    '''
    def alertAccept(self):
        # self.driver.switch_to_alert().accept() 废弃的方式
        self.driver.switch_to.alert.accept()

    '''
        弹框警告-取消
    '''
    def alertDismiss(self):
        # self.driver.switch_to_alert().dismiss() 废弃的方式
        self.driver.switch_to.alert.dismiss()

    '''
        切换到指定的iframe
    '''
    def switchFrame(self, css):
        self.elementWait(css)
        self.driver.switch_to.frame(self.getElement(css))

    '''
        切换到上一级(iframe)
    '''
    def switchFrameOut(self):
        self.driver.switch_to.default_content()

    '''
        打开新页面,并切换当前句柄为新页面的句柄
        (每个页面对应一个句柄handle,可以通过self.driver.window_handles查看所有句柄)
        --当前方法可能存在问题
    '''
    def openNewWindow(self):
        original_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)


    '''
        等待元素,默认5秒,每1秒检查一次
            --如果超时则对当前页面截图,以指定的文件名称保存到图片存储目录,并返回false
    '''
    def waitEleAndSaveExceptionForTimeout(self, css, pictureName):
        try:
            self.elementWait(css)
            return True
        except Exception as e:
            from conf.path import PICTUREPATH  # 导入定义的图片存储目录路径
            pictureFullName = PICTUREPATH + pictureName + '.jpg'
            self.getScreenshot(pictureFullName)
            return False

    '''
        等待元素,10秒,每1秒检查一次
            --如果超时,返回false
    '''
    def waitEleAndExceptionForTimeout(self, css):
        try:
            self.element_wait(css, secs=10)
            return True
        except Exception as e:
            return False

    '''
        根据指定的值选中相应的下拉列表中的选项
            --如果没有指定的值则抛出异常
    '''
    def selectByValue(self, css, value):
        self.element_wait(css)
        Select(self.get_element(css)).select_by_value(value)

if __name__ == '__main__':
    pySelenium = PySelenium('chrome')
