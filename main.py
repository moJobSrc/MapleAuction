import random
import threading
import time
import win32api
import win32con
from PIL import ImageGrab
import pyautogui
import win32gui
import tkinter

# pyautogui.MINIMUM_DURATION = 0.001
# pyautogui.MINIMUM_SLEEP = 0.001
# pyautogui.PAUSE = 0.01

global image1

# while True:
#     hwnd = win32gui.FindWindow(None, 'MapleStory')
#     win32gui.SetForegroundWindow(hwnd)
#     dimensions = win32gui.GetWindowRect(hwnd)
#     image1 = ImageGrab.grab(dimensions)


def seachClick():
    hwnd = win32gui.FindWindow(None, 'MapleStory')
    win32gui.SetForegroundWindow(hwnd)
    
    #아이템 검색
    search = pyautogui.locateCenterOnScreen('searchButton.png')
    print("검색 시작 버튼 : " + str(search))
    pyautogui.moveTo(search, duration=random.uniform(0.1, 0.2), tween=pyautogui.easeOutQuad)
    pyautogui.click()
    pyautogui.press("Enter")

    num = pyautogui.locateCenterOnScreen('null.png', confidence=0.9) #있는지 없는지 확인
    print("타입 : " + str(type(num)))
    if str(type(num)) == "<class 'NoneType'>":
        print("찾았습니다!")
        hwnd = win32gui.FindWindow(None, 'MapleStory')
        win32gui.SetForegroundWindow(hwnd)
        dimensions = win32gui.GetWindowRect(hwnd)
        image = ImageGrab.grab(dimensions)
        dir = "./capture/"+str(time.time())+".png"
        image.save(dir)
        print(dir + " 경로에 저장되었습니다.")

        #맨첫번쨰 아이템 클릭
        itemX, itemY = pyautogui.locateCenterOnScreen("itemName.png", confidence=0.9)
        pyautogui.moveTo(x=itemX, y=(itemY+51), duration=random.uniform(0.1, 0.2), tween=pyautogui.easeOutQuad)
        pyautogui.click()

        pyautogui.moveTo(pyautogui.locateCenterOnScreen("buy.png"), duration=random.uniform(0.1, 0.2), tween=pyautogui.easeOutQuad)
        pyautogui.click()
        pyautogui.press("Enter")

        time.sleep(random.uniform(0.1, 0.16))
        pyautogui.press("Enter")
    else:
        print("찾지 못했습니다")
        pyautogui.press("Enter")

    waitTime = random.uniform(5, 6.5)
    print(str(waitTime) + "초 후에 실행됩니다.\n")
    threading.Timer(waitTime, seachClick).start()


seachClick()

