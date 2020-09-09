# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/7/8 21:43
#导包
from selenium import webdriver
from selenium.webdriver.common.by import By
from pom.common.options import Options
from pom.base_page.base_page import BasePage
from pom.page_object.login_page import LoginPage


class ShopCartPage(BasePage):

    # 获取搜索页的url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/cart/index.html'
    #产品名称
    prdName = (By.XPATH, '//a[@class="goods-title"]')
    #checkbox
    checkBox = (By.XPATH, '//input[@type="checkbox"]/../span')
    #产品数量
    number = (By.XPATH, '//input[@type="number"]')
    #产品删除操作
    delPrd = (By.XPATH, '//a[text()="删除"]')
    #删除确认
    delConfirm = (By.XPATH, '// span[text() = "确定"]')
    #删除成功标志
    delSuccessFlg = (By.XPATH, '//p[text()="删除成功"]')
    #结算按钮
    calc= (By.XPATH, '//button[text()="结算"]')
    #提交订单
    orderSubmit = (By.XPATH, '//button[text()="提交订单"]')

    #检查购物车中商品
    def check_product(self, productName):
        # 校验商品是否存在
        check_prd = (By.XPATH, 'p[contains(text(), "%s")]'.format(productName))
        #查看商品是否存在
        try:
            return self.locator(check_prd)
        except Exception as error:
            self.logger.log(f'购物车中没有该商品{error}')
            return False

    # 勾选产品
    def click_checkbox(self):
        # checkBox
        checkboxs = self.locatorMore(self.checkBox)
        checkboxs[self.index].click()

    # 修改产品数量
    def input_number(self, txt):
        #获取数量元素
        numbers = self.locatorMore(self.number)
        numbers[self.index].clear()
        numbers[self.index].send_keys(txt)

        # # js执行器
        # js = "arguments[0].value = 2"
        # # 用js的方法页面看上去修改
        # self.driver.execute_script(js, numbers[self.index])

    # 点击删除
    def click_delPrd(self):
        #获取删除元素
        delPrd = self.locatorMore(self.delPrd)
        # 删除元素
        delPrd[self.index].click()

    #购物车中商品种类数
    def getCartNum(self):
        try :
            el = self.locatorMore(self.prdName)
            return len(el)
        except Exception as error:
            self.logger.info('购物车产品为空')
            return 0

    #删除确认
    def click_delConfirm(self):
        self.locator(self.delConfirm).click()

    #点击结算按钮
    def click_calc(self):
        self.locator(self.calc).click()

    # 断言函数：设置成功返回true，失败返回false
    def assert_ele(self, txt):
        try:
            # 定位元素
            return  self.locator(txt)
        except Exception as error:
            self.logger.error(f'购物车页面发生异常：{error}')
            return False

    # 调试函数
    def test_shopCart(self, txt):
        #访问当前页
        self.visit()
        #获取购物车数量
        len =  self.getCartNum()
        if len == 0 :
            self.logger.info('购物车为空，不可进行操作，请先添加商品')
            return False
        else :
            self.logger.info('购物车存在产品，可以结算或者进行删除操作')
            #购物车产品不止一种，删除第一种产品
            if (len > 1):
                self.index = 0
                #可以进行删除操作
                self.click_delPrd()
                #进行删除确认操作
                self.click_delConfirm()
                #购物车数量减少
                len = len - 1
                #删除成功标志
                self.assert_ele(self.delSuccessFlg)
                self.sleep()
            # 勾选购物车中产品、修改产品数量，进行结算
            for index in range(len):
                self.index = index
                # 勾选购物车中商品
                self.click_checkbox()
                # 修改购物车中产品数量
                self.input_number(txt)
            #产品结算
            self.click_calc()
        #结算之后页面是否跳转，提交订单
        return self.assert_ele(self.orderSubmit)

#调试
if __name__ == '__main__':
    # 调试方法
    driver = webdriver.Chrome(options=Options().options_conf('Chrome'))
    lp = LoginPage(driver, url=LoginPage.url)
    isLogin = lp.test_login('jade', 'jade620595')
    if (isLogin):
        sp = ShopCartPage(driver, url=ShopCartPage.url)
        sp.test_shopCart(2)
    driver.quit()