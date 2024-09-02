# -*- coding:utf-8 -*-
# @Time  :2023/3/24 2:38
# @AUTHOR:希耶谢
from selenium.webdriver import Keys

from Data_Load.page_data import create_data
from KeyWord.Browser import BrowserAct
from time import sleep
import allure


@create_data("/Users/koolearn/cuijianwei/pytest-allure-ui/Data/page_data/test_nvwa.xlsx", "nvwa_label_list")
class Lable_page(BrowserAct):
    class Button:
        pass

    class Input:
        pass

    @allure.step("新建标签列表")
    def build_new_label_list(self):
        self.mouse(*self.Button.search)
        self.ele_presence_wait(*self.Button.confirm).click()

        self.ele_visibility_wait(*self.Input.search).send_keys("用户测试标签")
        self.ele_visibility_wait(*self.Button.labelconfirm).click()

        list_info = self.ele_presence_wait(*self.Button.Assert).text.split("\n")
        print(list_info)
        with allure.step("断言结果检查"):
            assert "用户测试标签" in list_info, "断言失败信息"


