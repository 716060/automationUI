import pyautogui

# 获取屏幕（宽，高）
# Width, Height = pyautogui.size()

# 获得鼠标实时的（x，y）坐标
# X, Y = pyautogui.position()

# 移动鼠标到指定的坐标.duration参数==控制移动速度
# pyautogui.moveTo(x,y)

# 单击鼠标
# pyautogui.click()

# 移动到指定坐标-》点击
# pyautogui.click(x,y)

# 双击鼠标
# pyautogui.doubleClick()


# 输入文本（实际只识别英文字符）。interval参数==控制输入间隔
# pyautogui.write('Hello world!')

# 按中某个键
# pyautogui.press('esc')  === 按esc键
# pyautogui.press(['left', 'left', 'left', 'left'])  === 按四次左键


# 长按某个键
# with pyautogui.hold('shift')  ====  长按shift


# 组合键
# pyautogui.hotkey('ctrl', 'c')  ==== ctrl + c 复制组合键

# 生成一个弹窗并暂停程序。点击OK按钮 继续
# pyautogui.alert('暂停弹窗')
