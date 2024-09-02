'''
对浏览器操作的一些封装、关键字封装
'''

from selenium.webdriver import ActionChains, Keys  # 键盘Keys和鼠标ActionChains操作
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


# 浏览器的操作封装
class BrowserAct():
    def __init__(self, driver):
        self.__d = driver  # 浏览器对象初始化
        self.__wait = WebDriverWait(self.__d, 10)  # 显性等待初始化
        self.__action = ActionChains(self.__d)  # 鼠标操作对象

    # 窗口最大化
    def max(self):
        return self.__d.maximize_window()

    # 全屏窗口
    def full(self):
        return self.__d.fullscreen_window()

    # 浏览器进行截屏
    def screenshot(self):
        return self.__d.get_screenshot_as_png()

    # 打开新的url + 显性等待
    def open(self, url):
        self.__d.get(url)
        self.__wait.until(ec.url_contains(url))

    # 获取当前页面url
    @property
    def current_url(self):
        return self.__d.current_url

    # 获取当前页面title
    @property
    def title(self):
        return self.__d.title

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

    # frame 等待==加载frame，是否可以switch进去(加载完成=》自动switch进去)
    def frame(self, frame):
        self.__wait.until(ec.frame_to_be_available_and_switch_to_it(frame))

    # 退出iframe
    def exit_frame(self):
        self.__switch.default_content()

    # 去到上一级iframe
    def parent_frame(self):
        self.__switch.parent_frame()

    # alert 显性等待  弹窗切换
    @property
    def to_alert(self):
        self.__wait.until(ec.alert_is_present())  # 弹窗 显性等待==自动切换进alert。return driver.switch_to.alert

    def alert_accept(self):
        self.to_alert.accept()

    def alert_dismiss(self):
        self.to_alert.dismiss()

    def alert_send_keys(self, values):
        self.to_alert.send_keys(values)

    # 获取弹窗文本内容
    @property
    def alert_text(self):
        return self.to_alert.text

    # handles,页签、句柄切换
    def handle(self, n):  # 切换下标为n的页签
        handles = self.__d.window_handles  # 获取所有句柄
        return self.__switch.window(handles[n])

    # 执行JS语句显示元素定位位置，方便确认位置
    def locator_station(self, ele):
        self.__d.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            ele,
            "border: 2px solid green;"  # 边框，green绿色
        )

    # 查找元素 + 元素存在dom树显性等待  单数
    def ele_presence_wait(self, by, value, num=None):
        value = value.format(num) if num is not None else value
        locator = (by, value)
        self.__wait.until(ec.presence_of_element_located(locator))
        ele = self.__d.find_element(by, value)
        self.locator_station(ele)  # 框出元素定位的位置
        return ele

    # 查找元素 + 元素存在dom树显性等待  复数
    def eles_presence_wait(self, by, value, num=None):
        value = value.format(num) if num is not None else value
        locator = (by, value)
        self.__wait.until(ec.presence_of_all_elements_located(locator))
        eles = self.__d.find_elements(by, value)
        return eles

    # 查找元素 + 元素存在dom树 且可见 显性等待  单数
    def ele_visibility_wait(self, by, value, num=None):
        value = value.format(num) if num is not None else value
        locator = (by, value)
        self.__wait.until(ec.visibility_of_element_located(locator))
        ele = self.__d.find_element(by, value)
        self.locator_station(ele)  # 框出元素定位的位置
        return ele

    # 查找元素 + 元素存在dom树 且可见 显性等待  复数
    def eles_visibility_wait(self, by, value, num=None):
        value = value.format(num) if num is not None else value
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

    def ele_value_normal(self, by, value):
        return self.__d.find_element(by, value)

    def ele_value_wait_by_sleep(self, by, value, ownDriver, num=None):
        value = value.format(num) if num is not None else value
        ele = ownDriver.find_element(by, value)
        return ele

    def eles_value_wait_by_sleep(self, by, value, ownDriver, num=None):
        value = value.format(num) if num is not None else value
        ele = ownDriver.find_elements(by, value)
        return ele

    # 元素截屏
    def ele_screenshot(self, by, value, filename):
        ele = self.ele_presence_wait(by, value)
        ele.screenshot(filename)

    # 鼠标左击长按  click_and_hold(ele)
    def mouse_hold(self, by, value):
        ele = self.ele_presence_wait(by, value)
        self.__action.click_and_hold(ele).perform()

    # 鼠标释放   release()
    def mouse_release(self):
        self.__action.release().perform()

    # 鼠标悬停   move_to_element(ele)
    def mouse(self, by, value):
        ele = self.ele_presence_wait(by, value)
        self.__action.move_to_element(ele).perform()

    # 鼠标双击   double_click(ele)
    def mouse_double(self, by, value):
        ele = self.ele_presence_wait(by, value)
        self.__action.double_click(ele).perform()

    # 鼠标拖动   drag_and_drop(source,target)
    def mouse_drop(self, locator1, locator2):
        source = self.ele_presence_wait(*locator1)
        target = self.ele_presence_wait(*locator2)
        self.__action.drag_and_drop(source, target).perform()

    # 左击   click(ele)
    # 右击   context_click(ele)

    '''
    Windows对象  --浏览器窗体
    location对象 --页面
    document对象--页面内元素（定位，点击，输入，元素的属性…）

    js操作  ====  driver.execute_script("js语句")
    
    document.getElementById(id属性值).click()           点击元素
    document.querySelector(css选择器).value='输入的值'    元素输入文本  
    
    document.title  页面标题
    document.getElementById("id属性值").className   class属性值
    document.querySelector('css选择器').text  元素文本值
    document.querySelector('css选择器').textContent  元素文本值
    
    返回属性值 === return
    js="return document.getElementById('id属性值').className"
    res=driver.execute_script(js)

    页面对象 滚动
    document.body.scrollHeight   页面 滚动高度
    document.body.scrollWidth    页面 滚动宽度 
    window.scrollTo(x,y)
    document.getElementById('id属性值').scrollIntoVie(false)     ture默认 元素顶部  false元素底部

    元素对象 滚动
    先定位元素  document.getElementById('id属性值')  === ele
    document.getElementById('id属性值').scrollHeight    滚动条高度     
    ele.scrollWidth 	     滚动条宽度
    ele.scrollTo(x,y)	     滑动到指定坐标位置
    ele.scrollTop=y 	     y轴 滚动
    ele.scrollLeft=x    	 x轴 

    JQuery获取元素
    return $("p:contains('包含的字符')")[0]      根据文本获取元素
    return $(css定位)[0]          css定位
    return $x(xpath定位)[0]       xpath定位

    js=r"return $x(xpath定位)[0]"
    ele=driver.execute_script(js) # 执行js获取元素
    '''
