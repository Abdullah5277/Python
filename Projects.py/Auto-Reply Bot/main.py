import pyautogui
import time
import pyperclip

time.sleep(5)  # time to focus the window

pyautogui.click(700,200)  # activate window

pyautogui.moveTo(660,100)
pyautogui.dragTo(805,916,duration=1,button='left')

time.sleep(1)

pyautogui.hotkey('ctrl','c')

time.sleep(1)

text = pyperclip.paste()

print("Copied Text:")
print(text)
