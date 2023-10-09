import time

import pyautogui

# pyautogui.moveTo(200,400,duration=2)
# pyautogui.moveRel(200,500,duration=2)
# pyautogui.click(100,300,button='right')
# pyautogui.PAUSE = 2500
# pyautogui.vscroll(100)  # 垂直滚动，负下正
pyautogui.keyDown('alt')
pyautogui.keyDown('tab')

pyautogui.keyUp('alt')
pyautogui.keyUp('tab')
eval('time.sleep(1)')
pyautogui.keyDown('alt')
pyautogui.keyDown('tab')

pyautogui.keyUp('alt')
pyautogui.keyUp('tab')
eval('time.sleep(1)')
pyautogui.scroll(-1,1075, 357)
















