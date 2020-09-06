#导包
from time import sleep
from Log.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait

# 定义基类：提供各个PO对象来调用的公共类方法
class BasePage(object):
    #日志器
    logger = Logger().get_logger()

    # 定义构造函数：所有内容都是基于driver操作，所以要传递driver
    # 定义构造函数：每一个页面都有url，定义好url，在类中直接可以调用
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # 元素的定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 元素的定位
    def locatorMore(self, loc):
        return self.driver.find_elements(*loc)

    # 访问指定的URL
    def visit(self):
        self.driver.get(self.url)

    # 关闭浏览器
    def quit(self):
        self.sleep()
        self.driver.quit()

    #隐式等待
    def wait(self):
        self.driver.implicitly_wait(10)

    #显示等待
    def eleWait(self, loc):
        return WebDriverWait(self.driver, 5, 0.5).until(lambda el : self.locator(loc), message="元素定位失败")

    #强制等待
    def sleep(self):
        sleep(3)
