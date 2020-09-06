# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/7/8 21:45
from pom.base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

#创建注册页面对象
class RegisterPage(BasePage):
    # 获取注册页的url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/reginfo.html'
    # 获取页面元素
    account = (By.XPATH, '//*[@placeholder="请使用字母、数字、下划线 2~18 个字符"]') #用户名
    pwd = (By.XPATH, '//*[@placeholder="设置登录密码"]') #密码
    #勾选阅读并同意《服务协议》
    agree= (By.XPATH, '//*[@name="is_agree_agreement"][1]/..')
    #注册按钮
    register= (By.XPATH, '//form[@action="http://39.98.138.157/shopxo/index.php?s=/index/user/reg.html"]/div[4]/button')

    # 元素的操作行为
    # 输入用户名
    def input_account(self, txt):
        self.locator(self.account).send_keys(txt)

    # 设置密码
    def input_pwd(self, txt):
        self.locator(self.pwd).send_keys(txt)

    #勾选并同意服务协议
    def check_agree(self):
        self.locator(self.agree).click()

    # 注册第一步按钮
    def click_register(self):
        self.locator(self.register).click()

    # 断言函数：设置成功返回true，失败返回false
    def assert_ele(self, account):
        try:
            # 注册的用户名元素
            usename = (By.XPATH, f'//em[contains(text(), "{account}")]')
            # 定位注册成功特定元素
            return self.eleWait(usename)
        except Exception as error:
            self.logger.error(f'注册发生异常：{error}')
            return False

    # 调试函数
    def test_register(self, account, pwd):
        #访问当前页
        self.visit()
        #设置隐式等待
        self.wait()
        #输入账号
        self.input_account(account)
        #设置密码
        self.input_pwd(pwd)
        #同意服务
        self.check_agree()
        #点击注册按钮
        self.click_register()
        #返回断言结果
        return self.assert_ele(account)

#调试函数
if __name__ == '__main__':
    # 调试方法
    driver = webdriver.Chrome()
    rp = RegisterPage(driver=driver, url=RegisterPage.url)
    rp.test_register('jade003', '123456')
    driver.quit()
