# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/6/25 16:35
from selenium import webdriver
class Options:

    #配置浏览器选项（测试Chrome）
    def options_conf(self, browse_type):
        options = getattr(webdriver, browse_type+'Options')()
        #窗体最大化（正常模式下使用, 无头模式下有时不生效）
        #options.add_argument('start-maximized')
        #去掉开发者模式
        options.add_experimental_option('useAutomationExtension', False)
        #去掉黄条
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        #去掉密码弹窗
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)

        #liunx服务下让Chrome在root权限下跑
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # 无头模式： 启动浏览器进程，但是不会显示出来
        options.add_argument('--headless')
        # 无头模式下窗体最大化(设置窗体的分辨率，无头模式下出错通过截图来定位问题)
        options.add_argument('--window-size=1366,768')
        # 去掉 EGL-ERROR信息提示
        options.add_argument('--disable-gpu')

        return options


