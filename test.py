# -*- coding:utf-8 -*-
# @Time  :2023/3/20 7:32
# @AUTHOR:希耶谢
"""import selenium
# import ddt 不需要
import xlrd
import openpyxl
import jsonpath
# import allure
import pytest"""
import os

import pytest

'''
Data         =====》数据存放[page分离元素，测试用例数据]
Data_Loader  =====》自定义数据处理
KeyWord      =====》关键字封装[浏览器相关封装，数据库操作封装]
Page         =====》PO页面
TestCase     =====》用例存放
'''


# if __name__ == '__main__':
#     pytest.main(['-vs','./TestCase/test_case_01.py'])


def run():
    pytest.main(['-vs', '--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')


if __name__ == '__main__':
    run()
