# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/7/11 1:28
import os
import shutil
import unittest
from BeautifulReport import BeautifulReport


class UnitReport:
    def output_report(self):
        #当前模块所在的目录
        root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
        #存放报告的目录
        report_dir = os.path.join(root_dir, 'beatifulReport')
        # 报告名称
        report_filename = 'report'
        #如果存放报告目录存在
        if os.path.exists(report_dir):
            # 清空报告目录及其目录下的子文件
            shutil.rmtree(report_dir)
        #重新创建报告目录
        os.mkdir(report_dir)

        # 创建测试套件
        suits = unittest.defaultTestLoader.discover(start_dir=root_dir, pattern="cases_unit.py")
        # 创建BeautifulReport类对象，并添加测试套件
        report = BeautifulReport(suits)
        # 输出测试报告
        report.report('测试报告', report_filename, report_dir=report_dir)

if __name__ == '__main__':
    #添加测试套件生成报告
    UnitReport().output_report()