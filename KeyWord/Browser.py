# -*- coding:utf-8 -*-
# @Time  :2023/3/23 23:34
# @AUTHOR:希耶谢

'''
对浏览器操作的一些封装、关键字封装
'''

from selenium.webdriver import ActionChains, Keys  # 键盘和鼠标操作
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# 浏览器的操作封装
class BrowserAct():
    def __init__(self, driver):
        self.__d = driver  # 浏览器对象初始化
        self.__wait = WebDriverWait(self.__d, 10)  # 显性等待初始化
        self.__action = ActionChains(self.__d)  # 鼠标操作对象

    # 窗口最大化
    def max(self):
        return self.__d.maximize_window()

    # 浏览器进行截屏
    def screenshot(self, file_name):
        self.__d.get_screenshot_as_file(file_name)

    # 打开新的url + 显性等待
    def open(self, url):
        self.__d.get(url)
        self.__wait.until(ec.url_contains(url))

    # 获取当前页面url
    def current_url(self):
        return self.__d.current_url

    # 前进
    def forward(self):
        self.__d.forward()

    # 后退
    def back(self):
        self.__d.back()

    # 刷新
    def refresh(self):
        self.__d.refresh()

    # 切换switch_to
    @property
    def __switch(self):
        return self.__d.switch_to

    # iframe 切换
    def frame(self, frame):
        self.__switch.frame(frame)

    # 退出iframe
    def exit_frame(self):
        self.__switch.default_content()

    # 去到上一级iframe
    def parent_frame(self):
        self.__switch.parent_frame()

    # alert 显性等待  弹窗切换
    @property
    def to_alert(self):
        self.__wait.until(ec.alert_is_present())  # 弹窗 显性等待
        return self.__switch.alert

    def alert_accept(self):
        self.to_alert.accept()

    def alert_dismiss(self):
        self.to_alert.dismiss()

    def alert_send_keys(self, values):
        self.to_alert.send_keys(values)

    # handles,页签、句柄切换
    def handle(self, n):  # 切换下标为n的页签
        handles = self.__d.window_handles
        return self.__switch.window(handles[n])

    # 执行JS语句显示元素定位位置，方便确认位置
    def locator_station(self, ele):
        self.__d.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            ele,
            "border: 2px solid green;"  # 边框，green绿色
        )

    # 查找元素 + 元素存在dom树显性等待  单数
    def ele_presence_wait(self, by, value):
        locator = (by, value)
        self.__wait.until(ec.presence_of_element_located(locator))
        ele = self.__d.find_element(by, value)
        self.locator_station(ele)  # 框出元素定位的位置
        return ele

    # 查找元素 + 元素存在dom树显性等待  复数
    def eles_presence_wait(self, by, value):
        locator = (by, value)
        self.__wait.until(ec.presence_of_all_elements_located(locator))
        eles = self.__d.find_elements(by, value)
        return eles

    # 查找元素 + 元素存在dom树 且可见 显性等待  单数
    def ele_visibility_wait(self, by, value):
        locator = (by, value)
        self.__wait.until(ec.visibility_of_element_located(locator))
        ele = self.__d.find_element(by, value)
        self.locator_station(ele)  # 框出元素定位的位置
        return ele

    # 查找元素 + 元素存在dom树 且可见 显性等待  复数
    def eles_visibility_wait(self, by, value):
        locator = (by, value)
        self.__wait.until(ec.visibility_of_any_elements_located(locator))
        eles = self.__d.find_element(by, value)
        self.locator_station(eles)  # 框出元素定位的位置
        return eles

    # 元素text包含指定字符串判断 显性等待
    def ele_text_wait(self, by, value, text):
        locator = (by, value)
        result = self.__wait.until(ec.text_to_be_present_in_element(locator, text))
        return result

    # 元素value包含指定字符串判断 显性等待
    def ele_value_wait(self, by, value, text):
        locator = (by, value)
        result = self.__wait.until(ec.text_to_be_present_in_element_value(locator, text))
        return result

    # 元素截屏
    def ele_screenshot(self, by, value, filename):
        ele = self.ele_presence_wait(by, value)
        ele.screenshot(filename)

    # 鼠标长按
    def mouse_hold(self, by, value):
        ele = self.ele_presence_wait(by, value)
        self.__action.click_and_hold(ele).perform()

    # 鼠标释放
    def mouse_release(self):
        self.__action.release().perform()

    # 鼠标悬停
    def mouse(self, by, value):
        ele = self.ele_presence_wait(by, value)
        self.__action.move_to_element(ele).perform()

    # 鼠标双击
    def mouse_double(self, by, value):
        ele = self.ele_presence_wait(by, value)
        self.__action.double_click(ele).perform()
