# -*- coding:utf-8 -*-
# @Time  :2023/3/24 2:38
# @AUTHOR:希耶谢

from Data_Load.page_data import create_data
from KeyWord.Browser import BrowserAct


@create_data(r"D:\Pycharm\Selenium+unittest框架\data\test.xlsx", "baidu_home")
class Home_page():
    class Button:
        pass

    class Input:
        pass

    def __init__(self, driver):
        self.d = BrowserAct(driver)

    # 进入百度首页
    def open(self):
        self.d.open(self.url)

    # 进行搜索,截图
    def search(self, text):
        self.d.find_ele(*self.Input.search).send_keys(text)
        self.d.find_ele(*self.Button.search).click()
        self.d.screenshot("{}.png".format(text))

    # 进入 更多===》选择翻译
    def in_more(self):
        self.d.find_ele(*self.Button.more).click()
