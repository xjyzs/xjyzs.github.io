import pyautogui
import keyboard
import time
import ctypes,sys,os
clicking = False

def toggle_clicking():
    global clicking
    clicking = not clicking
    os.system(f'msg %username% /time:1 Status:{clicking}')

keyboard.on_press_key("p", lambda _:toggle_clicking())


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return None
if is_admin():
    while True:
        if clicking:
            pyautogui.click()
            time.sleep(0.1)
        else:
            time.sleep(0.5)
else:
    ctypes.windll.shell32.ShellExecuteW(None,u'runas',sys.executable,__file__,None,1)
