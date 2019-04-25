import pyautogui as pg
import time
# import os
from PIL import ImageGrab, ImageOps
from numpy import array


def up():
    pg.keyUp("down")
    time.sleep(0.01)
    pg.press("space")
    time.sleep(0.18)
    pg.keyDown("down")


def boot():
    pg.moveTo(280, 400)
    pg.click()
    i = 15
    current_value = 497
    current_x2 = 370
    time_start = time.time()
    while 1:
        current_time = time.time() - time_start
        if current_time > i:
            i += 15
            current_x2 += 10
            current_value += 50
        box = (320, 395, current_x2, 400)

        img = ImageOps.grayscale(ImageGrab.grab(box))
        a = array(img.getcolors())
        a = int(a.sum())

        # time.sleep(0.01)
        print(a)
        # +100 with each iteration
        if a != current_value:
            up()


if __name__ == "__main__":
    boot()
