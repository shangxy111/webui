# 定义登录页面对象
from pom.base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

# 创建login页面对象
class LoginPage(BasePage):
    '''
        LoginPage的核心业务是登录流程的实现：
            1. 登录关联的元素（Element）获取
            2. 基于元素实现的操作方式
            3. 实现核心的业务流程：登录
    '''
    # 获取登录页的url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    # 获取页面元素
    user = (By.NAME, 'accounts')  # 账号输入框
    pwd = (By.NAME, 'pwd')  # 密码输入框
    # 登录按钮
    login = (By.XPATH, '//button[text()="登录"]')
    # 登录状态的元素校验是否登录成功？
    logOut = (By.XPATH, '//a[text()="退出"]')
    # 元素的操作行为
    # 账号的输入
    def input_user(self, txt):
        self.locator(self.user).send_keys(txt)

    # 密码的输入
    def input_pwd(self, txt):
        self.locator(self.pwd).send_keys(txt)

    # 登录按钮的点击
    def click_login(self):
        self.locator(self.login).click()

    # 断言函数：设置成功返回true，失败返回false
    def assert_ele(self):
        try:
            #定位登录成功特定元素
            return self.eleWait(self.logOut)
        except Exception as error:
            self.logger.error(f'登录发生异常：{error}')
            return False

    # 调试函数
    def test_login(self, user, pwd):
        self.visit()
        self.wait()
        self.input_user(user)
        self.input_pwd(pwd)
        self.click_login()
        return  self.assert_ele()


if __name__ == '__main__':
    # 调试方法
    driver = webdriver.Chrome()
    lp = LoginPage(driver=driver, url=LoginPage.url)
    lp.test_login('jade', 'jade620595')
    driver.quit()
