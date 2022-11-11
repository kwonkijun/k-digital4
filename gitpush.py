import pyautogui
import time

time.sleep(3)
pyautogui.write("git add .")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("git commit -m 'a'")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("git push origin master")
pyautogui.press("enter")