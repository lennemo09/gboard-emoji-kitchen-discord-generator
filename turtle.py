import clipboard
import pyautogui
import keyboard
import time

target = "🐢"
initial_input_field_pos = (1713, 990)
input_field_pos = (1751, 475)
emoji_pos = (1523, 570)
send_button_pos = (1874, 469)
keyboard_mode_pos = (1496, 959)
emoji_mode_pos = (1552, 948)
clipboard_selection_pos = (1690, 695)

emojis = "😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 😡 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌞 🤢 🤮 🤧 🤒 🤕 🥴 😵 🥵 🥶 😷 😇 🤠 🤑 😎 🤓 🤥 🤡 👻 💩 👽 🤖 🎃 😈 👿 ☠️ 🔥 💫 ⭐ 🌟 💯 💦 💤 🕳️ 🎉 🎊 😺 ❤️ 🧡 💛 💚 💙 💜 🤎 🖤 🤍 ♥️ 💘 💝 💖 💗 💓 💞 💕 💌 💟 ❣️ 💔 💋 🦠 💀 👁️ 💐 🌹 🌷 🌼 🌵 🌲 🌪️ ☃️ ⛄ ❄️ 🔥 ☀️ ☁️ 🌈 ⭐ 🌟 💫 🌠 🌍 🌎 🌏 🙈 🙉 🙊 🐵 🦁 🐱 🐨 🐼 🐭 🐰 🐷 🐽 🐢 🐁 🐇 🐈 🐖 🦌 🦙 🦥 🐒 🦔 🦇 🐙 🕷️ 🐝 🦠 🍍 🌶️ 🥑 🧀 🌭 🎂 🧁 ☕ 🍴 🍽️ 🎉 🎊 🎈 🎂 🎄 🎃 🎗️ 👑 💎 🕶️ 📰 💌 🔮 ❤️ 🧡 💛 💚 💙 💜 🤎 🖤 🤍 🌐 💟 ♥️"

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
