import logging
import os
import threading
import time

import pyautogui
from pynput import mouse, keyboard

desktop = os.path.expanduser("~/Desktop")

# logging.basicConfig(filename="{0}/mouse_log.txt".format(desktop), level=logging.DEBUG,
#                    format="%(asctime)s: %(message)s")

# logging.basicConfig(filename="{0}/mouse_log.txt".format(desktop), level=logging.DEBUG)

file = open('/home/ctyun/Desktop/mouse_log.txt', 'w')


def try_sleep():
    global currentTime
    now = time.time()
    print('time.sleep(%s)' % (now - currentTime), file=file)
    currentTime = now


def on_move(x, y):
    # logging.info("pyautogui.moveTo(" + str(x) + ", " + str(y) + ")")
    # print('on_move' + str((x, y)))
    return


def on_click(x, y, button, pressed):
    # logging.info("pyautogui.mouseDown(button='" + str(button)[7:] + "')" if pressed
    # else "pyautogui.mouseUp(button='" + str(button)[7:] + "')")
    # print('on_click' + str((x, y, button, pressed)))
    if (pressed):
        try_sleep()
        print('pyautogui.click(x=%s, y = %s, button=\'%s\')' % (x, y, button.name), file=file)


def on_scroll(x, y, dx, dy):
    # print ("Mouse scrolled")
    # print('on_scroll' + str((x, y, dx, dy)))
    try_sleep()
    print('pyautogui.scroll(%s,%s,%s)' % (dy, x, y), file=file)


def on_press(key):
    # print('on_press' + str(key))
    try_sleep()
    print('pyautogui.keyDown(\'%s\')' % (key.name), file=file)


def on_release(key):
    # print('on_release' + str(key))
    try_sleep()
    print('pyautogui.keyUp(\'%s\')' % (key.name), file=file)


time.sleep(3)
currentTime = time.time()
mouseListener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboardListener = keyboard.Listener(on_press=on_press, on_release=on_release)
try:
    with mouseListener, keyboardListener:
        mouseListener.join()
        keyboardListener.join()
except:
    file.close()
# with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener1:
#    listener1.join()

# with keyboard.Listener(on_press=on_press) as listener2:
#    listener2.join()
