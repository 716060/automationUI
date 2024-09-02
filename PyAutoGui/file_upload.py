import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

'''
pyautogui
文件上传---测试
使用pyautogui第三方库，在OS层面进行文件上传操作
'''
driver = webdriver.Chrome()
driver.get(r"https://layui.dev/docs/2.8/upload/#examplesl")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# 单图片上传按钮
driver.find_element(By.CSS_SELECTOR, 'button#ID-upload-demo-btn').click()

# location先定位上传文件弹出窗的文件输入位置
pyautogui.moveTo(388, 73)
# 点击路径输入框
pyautogui.click()
# 按下backspace，删除原有的路径
pyautogui.press('backspace')

sleep(1)

# 键盘输入上传文件夹的路径
# 文件夹路径不能有中文（实际是按字母键，来输入内容）
pyautogui.write(r"C:\Users\hasee\Desktop\Leo")

sleep(1)

# 回车==》拼音输入法模式下，要按两次回车才生效
pyautogui.press('enter')
pyautogui.press('enter')

sleep(1)

# 移动鼠标===选择要上传的图片坐标
pyautogui.moveTo(664, 286)
# 点击
pyautogui.click()

# 移动鼠标===【打开】按钮
pyautogui.moveTo(716, 668)
# 点击  ==== 开始上传
pyautogui.click()

# 上传成功
wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="layui-layer2"]')))
driver.save_screenshot("success.png")
