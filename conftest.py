# -*- coding:utf-8 -*-
# @Time  :2023/3/24 4:09
# @AUTHOR:希耶谢

import pytest
from selenium import webdriver
import allure


# fixture 浏览器前置操作
@pytest.fixture(scope="session")
def browser():
    with allure.step("浏览器前置操作：打开浏览器，窗口最大化"):
        global driver
        '''
        Chrome 无头模式设置
        opts = webdriver.ChromeOptions
        opts.add_argument("headless")
        driver = webdriver.Chrome(options=opts)
        driver.set_window_size(x,y)  #无头模式====设置窗口大小
        '''
        driver = webdriver.Chrome()
        # option = webdriver.ChromeOptions()
        # option.add_experimental_option("detach", True)
        # driver = webdriver.Chrome(options=option)
        driver.maximize_window()  # 窗口最大化
        driver.title
    yield driver
    with allure.step("浏览器后置操作：退出浏览器"):
        driver.quit()


# 钩子函数，实现异常截图
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    out = yield  # yield ==》用例执行结果result对象
    report = out.get_result()  # report ==》用例执行结果的report对象
    """
        report对象属性：when,nodeid,outcome
        when（setup, call, teardown） 用例执行阶段
        nodeid   用例名字
        outcome（passed,failed）   用例执行结果
    """

    if report.when == "call":
        # 获取用例call阶段执行结果为失败的情况
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 添加allure报告截图
            with allure.step("用例执行失败截图==="):
                # allure添加附件--》allure.attach（源文件、文件名、文件类型）
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
