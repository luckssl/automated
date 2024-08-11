import pyautogui
import time


reels = (148,389)
n = 10
pyautogui.moveTo(reels)
pyautogui.click()
time.sleep(10)
pyautogui.moveTo(1078,522)
for _ in range (n):
    pyautogui.moveTo(1340,682)
    pyautogui.click()
    pyautogui.scroll(-1)
    time.sleep(5)
