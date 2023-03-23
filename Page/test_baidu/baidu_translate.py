# -*- coding:utf-8 -*-
# @Time  :2023/3/24 2:38
# @AUTHOR:希耶谢

from Data_Load.page_data import create_data
from KeyWord.Browser import BrowserAct


@create_data(r"D:\Pycharm\Selenium+unittest框架\data\test.xlsx", "baidu_translate")
class Translate_page():
    class Button:
        pass

    class Input:
        pass

    def __init__(self, driver):
        self.d = BrowserAct(driver)

    # 输入原文进行翻译
    def translate(self, text):
        self.d.find_ele(*self.Input.translate_text).send_keys(text)
        self.d.find_ele(*self.Button.translate_button).click()

    # 获取翻译后的内容
    def out_text(self):
        return self.d.find_ele(*self.Input.translate_output).text
