from pynput.keyboard import Controller, Key
import time

# 创建键盘控制器
keyboard = Controller()


# 确认
def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)


# 打开搜索框
def open_search():
    keyboard.press(Key.ctrl)
    keyboard.press('f')
    keyboard.release('f')
    keyboard.release(Key.ctrl)
    time.sleep(1)


# 粘贴
def paste():
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    time.sleep(1)


# 打字
def typewrite(txt):
    keyboard.type(txt)
