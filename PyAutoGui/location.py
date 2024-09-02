import os
import time
import pyautogui
'''
网上随便找的，实时输出鼠标当前坐标
'''
try:
    while True:
        print("Press Ctrl-C to end")
        screenWidth, screenHeight = pyautogui.size()  # 获取屏幕的尺寸
        print(screenWidth, screenHeight)
        x, y = pyautogui.position()  # 获取当前鼠标的位置
        # Python rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。
        # 如果指定的长度小于字符串的长度则返回原字符串。
        posStr = "Position:" + str(x).rjust(4) + ',' + str(y).rjust(4)
        print(posStr)
        time.sleep(1)
        os.system('cls')  # 清除屏幕
except KeyboardInterrupt:
    print('end....')
