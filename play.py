import pyautogui
import pyscreenshot as ImageGrab

# select the area of screen for making the screenshot, this area must cover the 6 branches
bbox = (1059, 0, 1060, 500)
# select the Y coordinates of branches
points = [(0, 455), (0, 387), (0, 319), (0, 255), (0, 186), (0, 119)]


# the coordinates of 'Play', 'left' and 'right' buttons must be defined
def play():
    pyautogui.click(1031, 645)


def click_right():
    pyautogui.click(1098, 634)


def click_left():
    pyautogui.click(960, 634)


def get_colors():
    im = ImageGrab.grab(bbox=bbox).convert('RGB')
    return [im.getpixel(point) for point in points]


play()
count = 0  # you can define the count to control the score!
while count < 200:
    for color in get_colors():
        if sum(color) == 333:
            click_left()
            click_left()
            count += 2
        else:
            click_right()
            click_right()
            count += 2
