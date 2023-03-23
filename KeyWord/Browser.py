# -*- coding:utf-8 -*-
# @Time  :2023/3/23 23:34
# @AUTHOR:希耶谢

'''
对浏览器操作的一些封装、关键字封装
'''

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys  # 键盘和鼠标操作
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# 浏览器的初始化
class Browser():
    # opt用来设置无头模式
    @staticmethod
    def Chrome(opt=None):
        if opt:
            return webdriver.Chrome(options=opt)
        else:
            return webdriver.Chrome()

    @staticmethod
    def Firefox(opt=None):
        if opt:
            return webdriver.Firefox(options=opt)
        else:
            return webdriver.Firefox()

    @staticmethod
    def Edge(opt=None):
        if opt:
            return webdriver.Edge(options=opt)
        else:
            return webdriver.Edge()

    @staticmethod
    def Safari(opt=None):
        if opt:
            return webdriver.Safari(options=opt)
        else:
            return webdriver.Safari()

    @staticmethod
    def Ie(opt=None):
        if opt:
            return webdriver.Ie(options=opt)
        else:
            return webdriver.Ie()


# 浏览器的操作封装
class BrowserAct():
    def __init__(self, driver):
        self.driver = driver  # 浏览器对象初始化
        self.wait = WebDriverWait(self.driver, 10)  # 显性等待初始化
        self.action = ActionChains(self.driver)  # 鼠标操作对象

    # 窗口最大化
    def max(self):
        return self.driver.maximize_window()

    # 浏览器进行截屏
    def screenshot(self, file_name):
        self.driver.get_screenshot_as_file(file_name)

    # 打开新的url + 显性等待
    def open(self, url):
        self.driver.get(url)
        self.wait.until(ec.url_contains(url))

    # 获取当前页面url
    def current_url(self):
        return self.driver.current_url

    # 前进
    def forward(self):
        return self.driver.forward()

    # 后退
    def back(self):
        return self.driver.back()

    # 刷新
    def refresh(self):
        return self.driver.refresh()

    # 切换switch_to
    @property
    def __switch(self):
        return self.driver.switch_to

    # iframe
    def frame(self, frame):
        self.driver.__switch.frame(frame)

    # 退出iframe
    def exit_frame(self):
        self.driver.__switch.default_content()

    # 去到上一级iframe
    def parent_frame(self):
        self.driver.__switch.parent_frame()

    # alert 弹窗切换
    @property
    def alert(self):
        return self.driver.__switch.alert

    def alert_accept(self):
        return self.driver.__switch.alert.accept()

    def alert_dismiss(self):
        return self.driver.__switch.alert.dismiss()

    def alert_send_keys(self, values):
        return self.driver.__switch.alert.send_keys(values)

    # handles,页签、句柄切换
    def handle(self, n):  # 切换下标为n的页签
        handles = self.driver.window_handles
        return self.driver.switch_to.window(handles[n])

    # 执行JS语句显示元素定位位置，方便确认位置
    def locator_station(self, ele):
        self.driver.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            ele,
            "border: 2px solid green;"  # 边框，green绿色
        )

    # 查找元素 + 元素存在dom树显性等待  单数
    def ele_presence_wait(self, by, value):
        locator = (by, value)
        ele = self.wait.until(EC.presence_of_element_located(locator))
        self.locator_station(ele)  # 框出元素定位的位置
        return ele

    # 查找元素 + 元素存在dom树显性等待  复数
    def eles_presence_wait(self, by, value):
        locator = (by, value)
        eles = self.wait.until(EC.presence_of_all_elements_located(locator))
        return eles

    # 查找元素 + 元素存在dom树 且可见 显性等待  单数
    def ele_visibility_wait(self, by, value):
        locator = (by, value)
        self.wait.until(EC.visibility_of_element_located(locator))
        ele = self.driver.find_element(by, value)
        self.locator_station(ele)  # 框出元素定位的位置
        return ele

    # 查找元素 + 元素存在dom树 且可见 显性等待  复数
    def eles_visibility_wait(self, by, value):
        locator = (by, value)
        self.wait.until(EC.visibility_of_any_elements_located(locator))
        eles = self.driver.find_element(by, value)
        self.locator_station(eles)  # 框出元素定位的位置
        return eles

    # 元素text包含指定字符串判断 显性等待
    def ele_text_wait(self, by, value, text):
        ele = (by, value)
        result = self.wait.until(ec.text_to_be_present_in_element(ele, text))
        return result

    # 元素value包含指定字符串判断 显性等待
    def ele_value_wait(self, by, value, text):
        ele = (by, value)
        result = self.wait.until(ec.text_to_be_present_in_element_value(ele, text))
        return result

    # 元素截屏
    def ele_screenshot(self, by, value, filename):
        ele = self.find_ele(by, value)
        ele.screenshot(filename)

    # 鼠标长按
    def mouse_hold(self, by, value):
        btn = self.find_ele(by, value)
        self.action.click_and_hold(btn).perform()

    # 鼠标释放
    def mouse_release(self):
        self.action.release().perform()

    # 鼠标悬停
    def mouse(self, by, value):
        self.action.move_to_element(self.find_ele(by, value)).perform()

    # 鼠标双击
    def mouse_double(self, by, value):
        self.action.double_click(self.find_ele(by, value)).perform()
