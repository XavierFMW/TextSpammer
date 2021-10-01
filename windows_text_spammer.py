from pynput.keyboard import Key, Controller
import time
import sys

keyboard = Controller()
time.sleep(5)

command_strings = ["Y so pressed"]
delay = 2

num = 7423

while num != 7501:

    for command in command_strings:

        keyboard.type(command)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(delay)

sys.exit()