#导包
import os
import unittest
from selenium import webdriver
from time import sleep
from pom.page_object.login_page import LoginPage
from pom.common.options import Options
from pom.page_object.prdDetail_page import PrdDetailPage
from pom.page_object.register_page import RegisterPage
from ddt import ddt, file_data, unpack, data

#测试用例
from pom.page_object.search_page import SearchPage
from pom.page_object.shopcart_page import ShopCartPage
from BeautifulReport import BeautifulReport
from pom.common.logger import Logger
import time

@ddt
class CasesUnit(unittest.TestCase):

    def setUp(self) -> None:
        # 创建Chrome浏览器对象,每一个用例只实例化一次
        self.driver = webdriver.Chrome(options=Options().options_conf('Chrome'))
        # 设置隐式等待时间
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        #强制等待
        sleep(3)
        #释放进程
        self.driver.quit()

    '''
        UnitTest中先运行setup，再执行case，再执行tearDown
        如果PO对象有关联，就通过driver进行关联
        1. driver在loginPage，执行了登录的操作，记录下登录状态
        2. 将这个driver传到第二个页面，执行登录后才能执行的操作
    '''
    # 用例流程一：登录
    @data(['jade008', '123456'])
    @unpack
    @BeautifulReport.add_test_img('test_1_error')
    def test_1(self, username, pwd):
        # 页面对象在实例化的时候都需要传递一个driver，不同的driver会执行不同的操作
        lp = LoginPage(self.driver, LoginPage.url)
        loginFlg = lp.test_login(username, pwd)
        #登录断言
        self.assertTrue(loginFlg, msg='登录失败')

    #用例测试二：注册
    # @data(['jade008', '123456'])
    # @unpack
    # @BeautifulReport.add_test_img('test_2') #失败截图
    # def test_2(self, username, pwd):
    #     #创建注册页面实例化对象
    #     rp = RegisterPage(self.driver, RegisterPage.url)
    #     registerFlg = rp.test_register(username, pwd)
    #     #注册断言
    #     self.assertTrue(registerFlg, msg='注册失败')

    #用例流程二:登录(用户不存在去注册)-商品搜索-商品详情(加入购物车)-购物车结算
    @file_data('../common/data.yaml')
    @unpack
    @BeautifulReport.add_test_img('test_3_error')
    def test_3(self, **kwargs):
        # 用户登录
        lp = LoginPage(self.driver, LoginPage.url)
        login = lp.test_login(kwargs['username'], kwargs['pwd'])
        # 用户存在，直接登录
        if login:
            pass
        # 用户不存在，需要注册
        else:
            # 先进行注册
            rp = RegisterPage(self.driver, RegisterPage.url)
            rp.test_register(kwargs['username'], kwargs['pwd'])
        # 商品搜索
        sp = SearchPage(self.driver, SearchPage.url)
        # 3-断言：搜索
        searchFlg = sp.test_search(kwargs['productName'])
        self.assertTrue(searchFlg)

        # 商品详情
        pp = PrdDetailPage(self.driver, sp.getProductId())
        # 产品详情添加商品、加入购物车
        addFlg = pp.test_prdDetail()
        self.assertTrue(addFlg)

        # 购物车页面
        scp = ShopCartPage(self.driver, ShopCartPage.url)
        # 购物车页面进行修改删除商品
        calcFlg = scp.test_shopCart(kwargs['productNum'])
        # 5-断言：购物车商品结算跳转
        self.assertTrue(calcFlg, msg='购物车流程失败')

    # BeautifulReport失败截图默认在save_img方法中
    def save_img(self, testMethod):
        # #当前模块所在的目录
        # root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
        # #存放图片的目录
        # img_path = os.path.join(root_dir, 'img').replace('\\', '/')
        #如果想让失败截图保存成自己想要的格式，修改BeautifulReport.add_test_img源码
        img_path = os.path.abspath('{}'.format(BeautifulReport.img_path))
        #图片目录不存在，创建
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        #打印日志
        Logger().get_logger().info('{0}/{1}.png'.format(img_path, testMethod))
        #失败截图
        self.driver.get_screenshot_as_file('{0}/{1}.png'.format(img_path, testMethod))

    # 失败截图保存
    def save_error(self):
         #获取系统当前时间
         now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
         # 当前模块所在的目录
         root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
         # 存放图片的目录
         img_path = os.path.join(root_dir, 'img').replace('\\', '/')
         # 图片目录不存在，创建
         if not os.path.exists(img_path):
             os.mkdir(img_path)
         #保存失败截图
         self.driver.save_screenshot('{0}/{1}.png'.format(img_path, now+'_error.png'))