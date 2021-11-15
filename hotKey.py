import win32con
from ctypes import *
from ctypes.wintypes import *
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

main_key = 192

# 这里的 QMThread 为自定义的 QThread
class HotKey(QThread):
    """全局热键监听"""
    ShowWindow = pyqtSignal(int)

    def __init__(self):
        super(HotKey, self).__init__()

        self.main_key = 192

    def run(self):
        """ 监听 windows 快捷键使用 """

        user32 = windll.user32

        while True:
            if not user32.RegisterHotKey(None, 1, win32con.MOD_ALT, self.main_key):  # alt+~
                print('Unable to register id')
                # print('Unable to register id', self.key_num, self.key_num % 2)

            try:
                msg = MSG()

                if user32.GetMessageA(byref(msg), None, 0, 0) != 0:
                    print('2222222', msg.message, win32con.WM_HOTKEY)
                    if msg.message == win32con.WM_HOTKEY:
                        if msg.wParam == win32con.MOD_ALT:
                            self.ShowWindow.emit(msg.lParam)

            finally:
                print('finish')