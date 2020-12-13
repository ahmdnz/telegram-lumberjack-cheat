import pyautogui
import pyscreenshot as ImageGrab

bbox = (1059, 0, 1060, 500)
points = [(0, 455), (0, 387), (0, 319), (0, 255), (0, 186), (0, 119)]


def play():
    pyautogui.click(1031, 645)


def click_right():
    pyautogui.click(1098, 634)


def click_left():
    pyautogui.click(960, 634)


def get_steps():
    im = ImageGrab.grab(bbox=bbox).convert('RGB')
    return [im.getpixel(s) for s in points]


play()
count = 0
while count < 200:
    for pixels in get_steps():
        if sum(pixels) == 333:
            click_left()
            click_left()
            count += 2
        else:
            click_right()
            click_right()
            count += 2
