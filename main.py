import pyautogui as pg
import time
# import os
from PIL import ImageGrab, ImageOps
from numpy import array


def up():
    print('jump')
    pg.keyUp("down")
    time.sleep(0.03)
    pg.press("space")
    time.sleep(0.18)
    pg.keyDown("down")


def boot():
    pg.moveTo(480, 350)
    pg.click()
    i = 8
    current_value = 447
    current_x2 = 370
    time_start = time.time()
    pg.keyDown("down")
    while 1:
        current_time = time.time() - time_start
        if current_time > i:
            i += 8
            current_x2 += 10
            current_value += 50
        box = (330, 395, current_x2, 400)
        img = ImageOps.grayscale(ImageGrab.grab(box))
        a = array(img.getcolors())
        a = int(a.sum())
        print(a)
        # +50 with each iteration
        if a != current_value:
            up()


if __name__ == "__main__":
    boot()

# todo
# 1. Fix mistakes that sometimes occur between 0-200
# 2. test i = 9 and 10
