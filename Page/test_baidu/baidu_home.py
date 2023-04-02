# -*- coding:utf-8 -*-
# @Time  :2023/3/24 2:38
# @AUTHOR:希耶谢

from Data_Load.page_data import create_data
from KeyWord.Browser import BrowserAct
import allure


@create_data(r"D:\Pycharm\selenium+pytest框架\Data\page_data\test_baidu.xlsx", "baidu_home")
class Home_page(BrowserAct):
    class Button:
        pass

    class Input:
        pass

    @allure.step("进入百度首页")
    def open_home(self):
        self.open(self.url)

    @allure.step("进行百度搜索,截图")
    def search(self, text):
        self.ele_presence_wait(*self.Input.search).send_keys(text)  # 搜索框定位 并输入文本
        self.ele_presence_wait(*self.Button.search).click()  # 点击搜索按钮
        allure.attach(self.screenshot(), "{}:搜索页面截屏".format(text), allure.attachment_type.PNG)

    @allure.step("点击进入 更多")
    def in_more(self):
        self.ele_presence_wait(*self.Button.more).click()  # 更多===》点击
