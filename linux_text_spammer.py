import subprocess
import time
import sys

time.sleep(5)

command_strings = ["y!mine", "y!chop", "y!fish"]
spam_strings = ["a"]
delay = 1


while True:

    for command in spam_strings:

        subprocess.call(["xdotool", "type", command])
        subprocess.call(["xdotool", "key", "0xff0d"])

        time.sleep(delay)

