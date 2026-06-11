import pyautogui
import time
import pyperclip

pyautogui.click(1639,1412)
time.sleep(1)

pyautogui.moveTo(679, 88)
pyautogui.dragTo(1800, 923 ,duration=1,button='left')

pyautogui.hotkey('ctrl','c')
time.sleep(1)

text=pyperclip.paste()

print(text)