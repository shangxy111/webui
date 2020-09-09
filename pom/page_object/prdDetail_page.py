# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/7/9 19:59
from pom.base_page.base_page import BasePage
from selenium import webdriver
from time import sleep
from pom.common.options import Options
from pom.page_object.login_page import LoginPage
from selenium.webdriver.common.by import By

class PrdDetailPage(BasePage) :

   def __init__(self, driver , id):
       self.driver = driver
       self.url = f'http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/{id}.html'

   #产品规格属性
   attributes = (By.XPATH, '//*[@class="cart-title"]/../ul/li[1]')
   #产品数量
   number = (By.XPATH, '//*[@type="number"]')
   #加入购物车
   cartButton = (By.XPATH, '//button[@title="加入购物车"]')
   #加入成功标志
   successFlg = (By.XPATH, '//p[text()="加入成功"]')


   #判断产品属性是否存在
   def is_exist_attributes(self):
       try:
           #定位产品属性
           return  self.locatorMore(self.attributes)
       except Exception as error:
           self.logger.info('产品规格属性不存在：{0}'.format(error))
           return False

   #选择属性规格
   def click_attributes(self):
        #如果产品有规格属性
        els = self.is_exist_attributes()
        #依次选择产品规格属性
        for el in els :
            sleep(1)
            # self.driver.execute_script("arguments[0].click();", el)
            el.click()


    #输入产品数量
   def input_number(self, text):
       el =self.locator(self.number)
       el.clear()
       el.send_keys(text)

       #js执行器
       # js = 'function clean(){ ' \
       #      'document.getElementById("text_box").value ="";} ' \
       #      'clean();'
       # self.driver.execute_script(js, el)

       # js2= 'function getValue() {' \
       #      'document.getElementById("text_box").value = 2;' \
       #      '}' \
       #      'getValue();'
       # self.driver.execute_script(js2, el)

    #点击加入购物车按钮
   def click_cartButton(self):
       self.locator(self.cartButton).click()

   #判断是否加入购物车成功
   def assert_ele(self):
       try:
           #定位"加入成功"提示元素(无头模式下定位不到该元素)
           return self.eleWait(self.successFlg)
       except Exception as error:
           self.logger.error(f'商品详情页发生异常：{error}')
           return False


   def test_prdDetail(self):
       #访问当前页
       self.visit()
       # 选择产品属性
       self.click_attributes()
       # 输入产品数量
       self.input_number(2)
       # 点击加入购物车
       self.click_cartButton()
       #断言
       return self.assert_ele()

#调试函数
if __name__ == '__main__':
    driver = webdriver.Chrome(options=Options().options_conf('Chrome'))
    lp = LoginPage(driver, url=LoginPage.url)
    #登录操作
    isLogin = lp.test_login('jade', 'jade620595')
    #判断是否登录成功
    if (isLogin):
        #产品详情页，加入购物车
        pd = PrdDetailPage(driver=driver, id=12)
        pd.test_prdDetail()
    driver.quit()



