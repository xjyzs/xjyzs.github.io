import time,ctypes,sys,os
try:
    import pyautogui
    import keyboard
except:
    os.system(f'msg %username% /time:1 未安装模块：pyautogui/keyboard，请先安装')
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
    # 无限循环
    while True:
        if clicking:
            pyautogui.click()
            time.sleep(1)
        else:
            time.sleep(0.5)
else:
    ctypes.windll.shell32.ShellExecuteW(None,u'runas',sys.executable,__file__,None,1)
