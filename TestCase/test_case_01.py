# -*- coding:utf-8 -*-
# @Time  :2023/3/24 4:50
# @AUTHOR:希耶谢
from time import sleep

import pytest
from Page.test_baidu.baidu_home import Home_page
from Page.test_baidu.baidu_more import More_page
from Page.test_baidu.baidu_translate import Translate_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.parametrize('text,text1', [("数学", "数学"), ("语文", "语文"), ("英语", "英语"), ("化学", "化学")])
def test_01(browser, text, text1):  # browser是conftest中fixture传过来的浏览器对象===一些前置 后置处理
    wait = WebDriverWait(browser, 10)
    home = Home_page(browser)

    # 01 打开百度首页
    home.open_home()
    assert home.current_url() == home.url, "百度首页url断言失败！"

    # 02 输入内容 进行搜索
    home.search(text)

    # 03 回退到首页
    home.back()

    # 04 首页点击 更多
    home.in_more()

    # 05 切换到 更多 页签
    more = More_page(browser)
    wait.until(ec.url_matches(more.url))

    # 06 更多 页面点击 翻译
    more.translate()

    # 07 切换到 翻译 页签
    translate = Translate_page(browser)
    more.handle(1)

    # 08 关闭展示页、输入内容 进行翻译
    translate.close()
    translate.translate(text1)
