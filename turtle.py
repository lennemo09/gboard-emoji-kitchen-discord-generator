import clipboard
import pyautogui
import keyboard
import time

target = "๐ข"
initial_input_field_pos = (1713, 990)
input_field_pos = (1751, 475)
emoji_pos = (1523, 570)
send_button_pos = (1874, 469)
keyboard_mode_pos = (1496, 959)
emoji_mode_pos = (1552, 948)
clipboard_selection_pos = (1690, 695)

emojis = "๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐คฃ ๐ญ ๐ ๐ ๐ ๐ ๐ฅฐ ๐ ๐คฉ ๐ฅณ ๐ค ๐ ๐ ๐ ๐ ๐ ๐ ๐คญ ๐ถ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐คช ๐ค ๐คจ ๐ง ๐ ๐ ๐ค ๐  ๐ก ๐คฌ โน๏ธ ๐ ๐ ๐ ๐ฅบ ๐ณ ๐ฌ ๐ค ๐คซ ๐ฐ ๐จ ๐ง ๐ฆ ๐ฎ ๐ฏ ๐ฒ ๐ฑ ๐คฏ ๐ข ๐ฅ ๐ ๐ ๐ ๐ฃ ๐ฉ ๐ซ ๐คค ๐ฅฑ ๐ด ๐ช ๐ ๐ ๐ ๐คข ๐คฎ ๐คง ๐ค ๐ค ๐ฅด ๐ต ๐ฅต ๐ฅถ ๐ท ๐ ๐ค  ๐ค ๐ ๐ค ๐คฅ ๐คก ๐ป ๐ฉ ๐ฝ ๐ค ๐ ๐ ๐ฟ โ ๏ธ ๐ฅ ๐ซ โญ ๐ ๐ฏ ๐ฆ ๐ค ๐ณ๏ธ ๐ ๐ ๐บ โค๏ธ ๐งก ๐ ๐ ๐ ๐ ๐ค ๐ค ๐ค โฅ๏ธ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ โฃ๏ธ ๐ ๐ ๐ฆ  ๐ ๐๏ธ ๐ ๐น ๐ท ๐ผ ๐ต ๐ฒ ๐ช๏ธ โ๏ธ โ โ๏ธ ๐ฅ โ๏ธ โ๏ธ ๐ โญ ๐ ๐ซ ๐  ๐ ๐ ๐ ๐ ๐ ๐ ๐ต ๐ฆ ๐ฑ ๐จ ๐ผ ๐ญ ๐ฐ ๐ท ๐ฝ ๐ข ๐ ๐ ๐ ๐ ๐ฆ ๐ฆ ๐ฆฅ ๐ ๐ฆ ๐ฆ ๐ ๐ท๏ธ ๐ ๐ฆ  ๐ ๐ถ๏ธ ๐ฅ ๐ง ๐ญ ๐ ๐ง โ ๐ด ๐ฝ๏ธ ๐ ๐ ๐ ๐ ๐ ๐ ๐๏ธ ๐ ๐ ๐ถ๏ธ ๐ฐ ๐ ๐ฎ โค๏ธ ๐งก ๐ ๐ ๐ ๐ ๐ค ๐ค ๐ค ๐ ๐ โฅ๏ธ"

emojis_list = emojis.split()

clipboard_list = []

for emoji in emojis_list:
    clipboard_list.append(target+emoji)
    # print(pyautogui.position())

limit = 15
iteration = 0
pyautogui.moveTo(initial_input_field_pos)
pyautogui.click()
for clip in clipboard_list:
    # if iteration >= limit:
    #     break

    # pyautogui.moveTo(input_field_pos)
    # time.sleep(0.2)
    # pyautogui.click()
    print("================= New Emoji ===============")
    # print("Pressing Space")
    # keyboard.press_and_release('space')
    # time.sleep(0.25)
    # print("0.25 after Pressed Space")

    pyautogui.moveTo(initial_input_field_pos)
    pyautogui.click()
    time.sleep(0.25)

    #pyautogui.hotkey('ctrl', 'a')
    print("Copying clip")
    clipboard.copy(clip)
    time.sleep(0.25)
    print("0.25 after Copying")
    #pyautogui.hotkey('alt', 'v')
    print("Pressing Ctrl V")
    keyboard.press_and_release('ctrl+v')
    time.sleep(0.25)
    print("0.25 after Ctrl V")

    print("Mouse to clipboard selection")
    pyautogui.moveTo(clipboard_selection_pos)
    time.sleep(0.2)
    pyautogui.click()
    print("Clicked clipboard selection")

    print("Mouse to emoji mode")
    pyautogui.moveTo(emoji_mode_pos)
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    print("Finished choosing emoji mode")

    print("Pressed left")
    keyboard.press_and_release('left')
    time.sleep(0.5)
    print("Pressed right")
    keyboard.press_and_release('right')
    time.sleep(1.5)

    print("Move to emoji")
    pyautogui.moveTo(emoji_pos)
    pyautogui.click()
    print("Clicked on emoji")

    print("Move to send button")
    pyautogui.moveTo(send_button_pos)
    pyautogui.click()
    print("Clicked on mouse button")

    print("Pressed Escape")
    keyboard.press_and_release('esc')
    time.sleep(0.5)
    print("0.5s after Pressed Escape")
    iteration += 1
