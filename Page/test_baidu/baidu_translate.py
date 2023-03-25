# -*- coding:utf-8 -*-
# @Time  :2023/3/24 2:38
# @AUTHOR:希耶谢
import allure

from Data_Load.page_data import create_data
from KeyWord.Browser import BrowserAct


@create_data(r"D:\Pycharm\selenium+pytest框架\Data\test_baidu.xlsx", "baidu_translate")
class Translate_page(BrowserAct):
    class Button:
        pass

    class Input:
        pass

    @allure.step("关闭展示页面")
    def close(self):
        self.ele_presence_wait(*Translate_page.Button.close).click()

    @allure.step("输入原文进行翻译")
    def translate(self, text):
        self.ele_presence_wait(*self.Input.translate_text).send_keys(text)  # 翻译原文输入
        self.ele_presence_wait(*self.Button.translate_button).click()  # 点击翻译按钮
    @allure.step('获取翻译后的内容')
    def out_text(self):
        return self.ele_presence_wait(*self.Input.translate_output).text


