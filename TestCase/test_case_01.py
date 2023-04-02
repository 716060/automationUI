# -*- coding:utf-8 -*-
# @Time  :2023/3/24 4:50
# @AUTHOR:希耶谢
import allure
import pytest
from Page.test_baidu.baidu_home import Home_page
from Page.test_baidu.baidu_more import More_page
from Page.test_baidu.baidu_translate import Translate_page
from Data_Load.case_data import load_yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from KeyWord import Sql_base


@allure.title("打开百度首页，从【更多】进入【百度翻译】进行翻译")
@allure.story("典型场景")
@allure.severity("critical")
@pytest.mark.parametrize('data', load_yaml(r"D:\Pycharm\selenium+pytest框架\Data\testcase_data\test_case_01.yaml"))
def test_01(browser, data):  # browser是conftest中fixture传过来的浏览器对象===一些前置 后置处理
    """
        01 打开百度首页
        02 输入内容 进行搜索
        03 回退到百度首页
        04 首页点击 更多
        05 切换到 更多 页签
        06 更多 页面点击 翻译
        07 切换到 翻译 页签
        08 关闭展示页、输入内容 进行翻译
    """
    home = Home_page(browser)
    home.open_home()
    home.search(data["text"])
    with allure.step("回退到百度首页"):
        home.back()
    home.in_more()
    more = More_page(browser)
    more.translate()
    translate = Translate_page(browser)
    more.handle(1)

    translate.close()
    translate.translate(data["text1"])

    with allure.step("结果断言检查："):
        assert home.url == r"https://www.baidu.com/", "断言失败信息"


'''
    with allure.step("数据库断言检查"):
        sql = Sql_base('host', 'port', 'user', 'password', 'database')
        # sql.execute("sql语句").fetchall()  # 获取全部SQL结果
        sql_data = sql.execute("sql语句").fetchone()  # 获取一条SQL结果
        assert sql_data == "要断言的数据", "断言失败信息"
'''
