from pynput import keyboard



def on_press(key):
    global forward
    global right
    global speed
    keyPress=''
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        
        keyPress=format(key.char)
        if keyPress=='a':
            right=-1*speed
            print(str(forward) +" "+ str(right))
        if keyPress=='w':
            forward=speed
            print(str(forward) +" "+ str(right))
        if keyPress=='d':
            right=speed
            print(str(forward) +" "+ str(right))
        if keyPress=='s':
            forward=-1*speed
            print(str(forward) +" "+ str(right))
        if keyPress=='r'and speed<=255:
            speed=speed+10
        if keyPress=='f'and speed>=0:
            speed-=10
        

    except AttributeError:
        print('special key {0} pressed'.format(
            key))


        
        
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()