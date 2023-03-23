# -*- coding:utf-8 -*-
# @Time  :2023/3/24 2:38
# @AUTHOR:希耶谢

from Data_Load.page_data import create_data
from KeyWord.Browser import BrowserAct


@create_data(r"D:\Pycharm\Selenium+unittest框架\data\test.xlsx", "baidu_more")
class More_page():
    class Button:
        pass

    class Input:
        pass

    def __init__(self, driver):
        self.d = BrowserAct(driver)

    # 选择 百度翻译
    def translate(self):
        self.d.find_ele(*self.Button.translate).click()
