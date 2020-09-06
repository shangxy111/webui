# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/6/25 16:35
from selenium import webdriver
class Options:

    #配置浏览器选项（测试Chrome和firefox）
    def options_conf(self, browse_type):
        options = getattr(webdriver, browse_type+'Options')()
        #窗体最大化
        options.add_argument('start-maximized')
        #去掉开发者模式
        options.add_experimental_option('useAutomationExtension', False)
        #去掉黄条
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        #去掉密码弹窗
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)

        # 无头模式： 启动浏览器进程，但是不会显示出来
        #options.add_argument('--headless')
        # 去掉 EGL-ERROR信息提示
        options.add_argument('--disable-gpu')

        return options


