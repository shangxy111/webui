# _*_ coding:utf-8 _*-
# 作者：shangxy
# @Time : 2020/7/8 21:43

#搜索页面
from selenium import webdriver
from selenium.webdriver.common.by import By
from pom.base_page.base_page import BasePage

#创建搜索页面对象
class SearchPage(BasePage):

    # 获取搜索页的url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/search/index.html'
    # 获取页面元素
    prd = (By.ID, 'search-input')  # 产品搜索框
    # 产品链接
    prdlink = (By.XPATH, '//div[@class="items"]/a')
    # 搜索按钮
    search = (By.ID, 'ai-topsearch')
    # 元素的操作行为
    # 产品的输入
    def input_product(self, prdName):
        self.locator(self.prd).send_keys(prdName)

    # 搜索按钮的点击
    def click_search(self):
        self.locator(self.search).click()

    # 断言函数：设置成功返回true，失败返回false
    def assert_ele(self, prdName):
        try:
            #定位登录成功特定元素
            prdName = (By.XPATH, f'//p[contains(text(), "{prdName}")]')
            return self.locator(prdName)
        except Exception as error:
            self.logger.error(f'搜索发生异常：{error}')
            return False

    #获取产品ID
    def getProductId(self):
        #获取第一个产品的链接
        link = self.locator(self.prdlink)
        #分解链接地址:http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/{id}.html
        list = link.get_attribute('href').split('/')
        id = list[-1].split('.')[0]
        return id

    # 调试函数
    def test_search(self, prdName):
        #打开搜索页
        self.visit()
        #输入产品名称
        self.input_product(prdName)
        #点击搜索按钮
        self.click_search()
        #返回断言
        return self.assert_ele(prdName)


if __name__ == '__main__':
    # 调试方法
    driver = webdriver.Chrome()
    sp = SearchPage(driver=driver, url=SearchPage.url)
    sp.test_search('手机')
    sp.getProductId()
    driver.quit()