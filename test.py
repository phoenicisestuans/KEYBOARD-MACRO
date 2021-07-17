import win32api
import win32con
import time as t
import sys

input = win32api.KEYBDINPUT(0x57, 'w', win32con.KEYEVENTF_SCANCODE)
t.sleep(10)
win32con.sendInput(1, input, sys.getsizeof(input))
t.sleep(10)