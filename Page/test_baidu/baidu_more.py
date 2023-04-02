# -*- coding:utf-8 -*-
# @Time  :2023/3/24 2:38
# @AUTHOR:希耶谢
import allure

from Data_Load.page_data import create_data
from KeyWord.Browser import BrowserAct


@create_data(r"D:\Pycharm\selenium+pytest框架\Data\page_data\test_baidu.xlsx", "baidu_more")
class More_page(BrowserAct):
    class Button:
        pass

    class Input:
        pass

    @allure.step("点击 百度翻译")
    def translate(self):
        self.ele_presence_wait(*self.Button.translate).click()


